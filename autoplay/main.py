"""Main module for autoplay."""
from data_tools.last_fm_data import create_user

def main_example():
    last_fm_name = 'Car_door'
    print(f"Getting listening history for user {last_fm_name}...")
    my_user = create_user(last_fm_name)
    print("History retrieved.")
    print(f"Number of tracks: {len(my_user.tracks)}")

main_example()