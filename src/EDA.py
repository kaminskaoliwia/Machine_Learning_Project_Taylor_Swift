import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

from album_config import new_albums, album_colors, features01

PRINT = False
output_dir = "hist"
os.makedirs(output_dir, exist_ok=True)

songs = pd.read_csv("../data/taylor_songs_no_TV.csv")

##plt.scatter(songs['energy'], songs['valence'])
##plt.show()

##print(songs[songs['energy'] == songs['energy'].min()]["name"].values)
##print(songs[songs['energy'] == songs['energy'].max()]["name"].values)

##print(songs[songs['valence'] == songs['valence'].min()]["name"].values)
##print(songs[songs['valence'] == songs['valence'].max()]["name"].values)

for album in new_albums:

    mask = songs['album'] == album
    for feature in features01:
        plt.hist(songs[mask][feature], color=album_colors[album])
        plt.title(f"{album} - {feature}")
        filename = f"{album}_{feature}.png"
        plt.savefig(os.path.join(output_dir, filename))
        plt.clf()

##        print(album, feature, songs[mask][feature].describe())
        print(songs[songs[feature] == songs[feature].min()]["name"].values)
        print(songs[songs[feature] == songs[feature].max()]["name"].values)
