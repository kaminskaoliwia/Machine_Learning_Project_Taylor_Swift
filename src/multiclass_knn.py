# Import
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

from album_config import features, albums, album_colors

songs = pd.read_csv("../data/taylor_songs_no_TV.csv")
album_scores = []

songs_dummy = pd.get_dummies(songs, prefix="", prefix_sep="")

for album in albums:
    X = songs_dummy[features].values
    y = songs_dummy[f'{album}'].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2,
                                                    random_state=13)

    knn = KNeighborsClassifier(n_neighbors=8)
    knn.fit(X_train, y_train)
    album_scores.append(knn.score(X_test, y_test))

album_dict = dict(zip(albums, album_scores))
colors = [album_colors[a] for a in albums]

plt.figure(figsize=(12, 6))
plt.bar(albums, album_scores, color=colors)
plt.title('KNN for each Taylor Swift album')
plt.xlabel=('Album')
plt.ylabel=('Accuracy Score')
plt.xticks(rotation=45)
plt.show()
