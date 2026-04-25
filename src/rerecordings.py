### Imports
##import pandas as pd
##import numpy as np
##
##songs = pd.read_csv('taylor_swift_spotify.csv')
##
### Dropping irrelevant information
##songs_info = songs.drop(['Unnamed: 0', 'release_date', 'track_number',
##                             'id', 'uri'], axis=1)
##
##album_tv_full_names = ["1989 (Taylor's Version) [Deluxe]", "Speak Now (Taylor's Version)",
##            "Red (Taylor's Version)", "Fearless (Taylor's Version)"]
##
##songs_info = songs_info[songs_info['album'].isin(album_full_names)]
##album_tv_short = ["1989 tv", "speak now tv", "red tv", "fearless tv"]
##
##album_dict = dict(zip(album_tv_full_names, album_short_names))
##songs_info['album'] = songs_info['album'].replace(album_dict)
##
##
##print(songs['album'].unique())
