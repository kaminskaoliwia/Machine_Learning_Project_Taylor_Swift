import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report

from album_config import features, new_albums

songs = pd.read_csv("../data/taylor_songs_no_TV.csv")
songs = songs.set_index(["name"])
songs['new_taylor'] = songs['album'].isin(new_albums)

X = songs[features].values
y = songs['new_taylor'].values

scaler = StandardScaler()
X = scaler.fit_transform(X)

songs_train, songs_test = train_test_split(songs, test_size=0.2, random_state=14)

X_train = songs_train[features].values
X_test = songs_test[features].values
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)
y_train = songs_train['new_taylor'].values
y_test = songs_test['new_taylor'].values

neighbors = np.arange(1,13)
train_accuracies = {}
test_accuracies = {}
predictions = []

for neighbor in neighbors:
    knn = KNeighborsClassifier(n_neighbors=neighbor)
    knn.fit(X_train,y_train)
    train_accuracies[neighbor] = knn.score(X_train, y_train)
    test_accuracies[neighbor] = knn.score(X_test, y_test)

##plt.plot(neighbors, train_accuracies.values(), label="Training Accuracy")
##plt.plot(neighbors, test_accuracies.values(), label="Testing Accuracy")
##plt.legend()
##plt.show()

knn2 = KNeighborsClassifier(n_neighbors=11)
knn2.fit(X_train, y_train)
y_pred = knn2.predict(X_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

joblib.dump(knn2, '../models/knn_model.joblib')
joblib.dump(scaler, '../models/scaler_knn.joblib')
##errors_mask = y_pred != y_test
##errors_df = songs_test[errors_mask].copy()
##errors_df['predicted_is_new'] = y_pred[errors_mask]
##print(errors_df[['album', 'new_taylor', 'predicted_is_new']])
