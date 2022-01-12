"""Models for making sense of our data and structure."""
from datetime import timedelta
from ..data_tools.common_models import *


def calc_time_diff(scrobble_a: Track, scrobble_b: Track):
    """Calculate the difference in timestamps of two scrobbles
    
    Args:
        scrobble_a (Track): a scrobble of one track
        scrobble_b (Track): a scrobble of another track
    
    Returns:
        time_diff (timedelta): the difference of the scrobbles' timestamps
    """
    return abs(scrobble_a.date - scrobble_b.date)
    

def is_proximal(scrobble_a: Track, scrobble_b: Track, time_diff_cutoff: timedelta):
    """Determine if two scrobbles are proximal
    
    Args:
        scrobble_a (Track): a scrobble of one track
        scrobble_b (Track): a scrobble of another track
        time_diff_cutoff (timedelta): a length of time to determine if two tracks are proximal

    Returns:
        true if scrobbles are proximal, else false
    """
    time_diff = calc_time_diff(scrobble_a, scrobble_b)
    return time_diff <= time_diff_cutoff

def calc_track_time_proximity(scrobble_a: Track, library: User, time_diff_cutoff: timedelta):
    """Tracks are proximal if their timestamps are within a certain time of each other
        
    """
    
    pass

def calc_all_time_proximities(user: User, time_diff_cutoff: timedelta):
    """Calculate time proximities for all tracks in a user's library"""

    for scrobble in User.tracks:
        calc_track_time_proximity(scrobble)
    pass