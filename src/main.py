"""Main module for autoplay."""
import time
import sys
from datetime import datetime, timedelta

from .data_tools.common_models import Track
from .models.models import calc_all_time_proximities
from .data_tools.last_fm_data import create_user

def main_example():
    last_fm_name = 'Car_door'
    print(f"Getting listening history for user {last_fm_name}...")
    start_fetch = time.perf_counter()
    my_user = create_user(last_fm_name, limit=20)
    end_fetch = time.perf_counter()
    print(sys.getsizeof(my_user))
    print(f"History retrieved in {end_fetch-start_fetch:0.1f} seconds.")
    print(f"Number of tracks: {len(my_user.tracks)}")


def clustering_example():
    last_fm_name = "Nesdunk14"
    print(f"Getting listening history for user {last_fm_name}...")
    start_fetch = time.perf_counter()
    my_user = create_user(last_fm_name, limit=500)
    end_fetch = time.perf_counter()
    print(f"History retrieved in {end_fetch-start_fetch:0.1f} seconds.")
    print(f"Number of tracks: {len(my_user.tracks)}")
    start_calc = time.perf_counter()
    time_proximities = calc_all_time_proximities(my_user, timedelta(seconds=3600))
    end_calc = time.perf_counter()
    print(f"Time proximities calculated in {end_calc-start_calc:0.1f} seconds.")
    print(time_proximities[Track("Cosmic Sans", "Motivational Music for the Syncopated Soul", "Cory Wong", [], datetime(2021, 11, 1))])
