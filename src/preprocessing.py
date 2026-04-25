# Imports
import pandas as pd
import numpy as np

PRINT = False
songs = pd.read_csv('data/taylor_swift_spotify.csv')

# Dropping irrelevant information
songs_info = songs.drop(['Unnamed: 0', 'release_date', 'track_number',
                             'id', 'uri'], axis=1)

# Only voice notes have popularity equal 0
songs_info = songs_info[songs_info['popularity'] != 0]
# print(songs_info[songs_info['popularity'] == 0])
                        
# Selecting albums and changing their names
album_full_names = ['THE TORTURED POETS DEPARTMENT: THE ANTHOLOGY','Midnights (3am Edition)', 'evermore (deluxe version)', 'folklore (deluxe version)',
                    'Lover', 'reputation', '1989 (Deluxe)', 'Red', 'Speak Now', 'Fearless (Platinum Edition)', 'Taylor Swift (Deluxe Edition)']

songs_info = songs_info[songs_info['album'].isin(album_full_names)]

album_short_names = ['ttpd', 'midnights', 'evermore', 'folklore', 'lover', 'rep', '1989', 'red', 'speak now', 'fearless', 'debut']
album_dict = dict(zip(album_full_names, album_short_names))
songs_info['album'] = songs_info['album'].replace(album_dict)
songs_info.to_csv("data/taylor_songs_no_TV.csv")

# print(songs_info['album'].unique())
# print(songs_info.isna().sum())









                                        
