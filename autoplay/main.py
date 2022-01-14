"""Main module for autoplay."""
import time
from data_tools.last_fm_data import create_user


def main_example():
    last_fm_name = 'Nesdunk14'
    print(f"Getting listening history for user {last_fm_name}...")
    start_fetch = time.perf_counter()
    my_user = create_user(last_fm_name, limit=None)
    end_fetch = time.perf_counter()
    print(f"History retrieved in {end_fetch-start_fetch:0.1f} seconds.")
    print(f"Number of tracks: {len(my_user.tracks)}")


main_example()
