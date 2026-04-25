
import pandas as pd
import numpy as np

# Album names
album_full_names = ['THE TORTURED POETS DEPARTMENT: THE ANTHOLOGY', 'Midnights (3am Edition)', 'evermore (deluxe version)', 'folklore (deluxe version)',
                    'Lover', 'reputation', '1989 (Deluxe)', 'Red', 'Speak Now', 'Fearless (Platinum Edition)', 'Taylor Swift (Deluxe Edition)']

album_short_names = ['ttpd', 'midnights', 'evermore', 'folklore', 'lover', 'rep', '1989', 'red', 'speak now', 'fearless', 'debut']
albums = album_short_names

# Album categories
new_albums = albums[:6]
old_albums = albums[6:]

# Album colors
colors = ['dimgrey', 'midnightblue', 'saddlebrown', 'lightgray',
          'pink', 'black', 'skyblue', 'maroon', 'rebeccapurple',
          'gold', 'turquoise']

album_colors = dict(zip(album_short_names, colors))

# Relevant features
features = ['acousticness', 'danceability', 'energy',
            'loudness', 'speechiness', 'tempo', 'valence']

# Features with a scale from 0 to 1
features01 = [f for f in features if f not in ('loudness', 'tempo')]
