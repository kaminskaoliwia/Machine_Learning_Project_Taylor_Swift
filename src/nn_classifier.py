import pandas as pd
import numpy as np
import joblib
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

from album_config import features, new_albums

songs = pd.read_csv("../data/taylor_songs_no_TV.csv")
songs = songs.set_index(["name"])
songs['new_taylor'] = songs['album'].isin(new_albums).astype(int)

X = songs[features].values
y = songs['new_taylor'].values

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=13)

input_shape = (len(features),)
early_stopping_monitor = EarlyStopping(patience=5, restore_best_weights=True)

model = Sequential()
model.add(Dense(32, activation='relu', input_shape=input_shape))
model.add(Dense(16, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(X_train, y_train,
          validation_data=(X_test, y_test),
          epochs=30,
          callbacks=[early_stopping_monitor],
          verbose=0)

model.save('../models/new_taylor_NN.keras')
joblib.dump(scaler, '../models/scaler_NN.joblib')

y_pred_prob = model.predict(X_scaled)
y_pred = (y_pred_prob > 0.5).astype(int).flatten()
results = pd.DataFrame({
    'Song': songs.index,
    'Actual': y,
    'Predicted': y_pred,
    'Confidence': y_pred_prob.flatten()
})

errors = results[results['Actual'] != results['Predicted']]
print("Piosenki, które pomyliły model:")
print(errors[['Song', 'Actual', 'Predicted', 'Confidence']])
