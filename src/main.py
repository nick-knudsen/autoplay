"""Main module for autoplay."""
import time
import sys
from .data_tools.last_fm_data import create_user
# from .data_tools.spotify_data import 


def main_example():
    """[summary]
    """
    last_fm_name = 'Car_door'
    print(f"Getting listening history for user {last_fm_name}...")
    start_fetch = time.perf_counter()
    my_user = create_user(last_fm_name, limit=None)
    end_fetch = time.perf_counter()
    print(sys.getsizeof(my_user))
    print(f"History retrieved in {end_fetch-start_fetch:0.1f} seconds.")
    print(f"Number of tracks: {len(my_user.tracks)}")


def track_pipeline_example():
    """[summary]
    """
    last_fm_name = 'Car_door'
    print(f"Getting listening history for user {last_fm_name}...")
    start_fetch = time.perf_counter()
    my_user = create_user(last_fm_name, write_data=False, scrobble_limit=1)
    end_fetch = time.perf_counter()
    print(f"History retrieved in {end_fetch-start_fetch:0.1f} seconds.")
    print(f"Number of tracks: {len(my_user.tracks)}")
    print(f"Number of artists: {len(my_user.artists)}")
    artist_names = [artist.name for artist in my_user.artists]
    # for name in artist_names:
    
