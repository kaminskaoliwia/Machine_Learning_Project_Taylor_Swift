# Import
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report

from album_config import features

songs = pd.read_csv("../data/taylor_songs_no_TV.csv")
songs['is_red'] = songs['album'] == 'red'
songs_red = songs.drop(['album', 'name'], axis=1)

X = songs_red[features].values
y = songs_red['is_red'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2,
                                                    random_state=56)

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

knn2 = KNeighborsClassifier(n_neighbors=6)
knn2.fit(X_train,y_train)
y_pred = knn2.predict(X_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
