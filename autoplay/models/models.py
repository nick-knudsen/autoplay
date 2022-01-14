"""Models for making sense of our data and structure."""
# standard imports
from datetime import timedelta
from time import time
from typing import List
# third-party imports
import numpy as np
# local imports
import data_tools.common_models as autoplay


def calc_time_diff(scrobble_a: autoplay.Track, scrobble_b: autoplay.Track):
    """Calculate the difference in timestamps of two scrobbles
    
    Args:
        scrobble_a (Track): a scrobble of one track
        scrobble_b (Track): a scrobble of another track
    
    Returns:
        time_diff (timedelta): the difference of the scrobbles' timestamps
    """
    time_diff = abs(scrobble_a.date - scrobble_b.date)
    return time_diff

def is_proximal(scrobble_a: autoplay.Track, scrobble_b: autoplay.Track, time_diff_cutoff: timedelta):
    """Determine if two scrobbles are proximal
    
    Args:
        scrobble_a (Track): a scrobble of one track
        scrobble_b (Track): a scrobble of another track
        time_diff_cutoff (timedelta): a time window within which tracks are proximal

    Returns:
        true if scrobbles are proximal, else false
    """
    time_diff = calc_time_diff(scrobble_a, scrobble_b)
    return time_diff <= time_diff_cutoff

def calc_track_time_proximity(scrobble_a: autoplay.Track, library: List[autoplay.Track], time_diff_cutoff: timedelta):
    """Tracks are proximal if their timestamps are within a certain time of each other
    Calculate the timedeltas for all scrobbles in the time window from scrobble_a

    Args:
        scrobble_a (Track): a scrobble of the given base track
        library (List[Track]): a list of scrobbles
        time_diff_cutoff (timedelta): a time window within which tracks are proximal

    Returns:
        time_diff_sums ({Track: [timedelta, int]}): a dict containing the sum of the time differentials and counts for all tracks in the window
    """
    # filter out only proximal scrobbles
    proximal_scrobbles = list(filter(lambda x: (x.date > scrobble_a.date - time_diff_cutoff and x.date < scrobble_a.date + time_diff_cutoff), library))
    time_diff_sums = {}
    # calculate time diff sums
    for scrobble_b in proximal_scrobbles:
        # ignore track if it is the same as the central track
        if scrobble_a == scrobble_b:
            continue
        # calculate time diff for each proximal track
        time_diff = calc_time_diff(scrobble_a, scrobble_b)
        # add calculated time diff to time_diff_sums, increment track listen count by one
        if scrobble_b in time_diff_sums.keys():
            time_diff_sums[scrobble_b] = np.add(time_diff_sums[scrobble_b], [time_diff, 1])
        else:
            time_diff_sums[scrobble_b] = [time_diff, 1]

    return time_diff_sums

def calc_all_time_proximities(user: autoplay.User, time_diff_cutoff: timedelta):
    """Calculate time proximities for all tracks in a user's library

    Args:
        user (User): a user for which to calculate the time proximities
        time_diff_cutoff (timedelta): a time window within which tracks are proximal
    
    Returns:
        track_time_proximities ({Track: {Track: float}}): a dict containing time proximities for all tracks in the users library
    """

    overall_time_diff_sums = {}
    
    for track_b in user.tracks:
        # calculate time diffs for each scrobble in user library
        scrobble_time_diff_sums = calc_track_time_proximity(track_b, user.tracks, time_diff_cutoff)
        # add time diffs to relevant track
        if track_b in overall_time_diff_sums.keys():
            for track_a, sum_and_count in scrobble_time_diff_sums.items():
                if track_a in overall_time_diff_sums[track_b][0].keys():
                    overall_time_diff_sums[track_b][0][track_a] = np.add(overall_time_diff_sums[track_b][0][track_a], sum_and_count)
                else:
                    overall_time_diff_sums[track_b][0][track_a] = sum_and_count
            # increment track listen count by one
            overall_time_diff_sums[track_b][1] += 1
        else:
            # new track, initialize values for time diff sums and track listen count
            overall_time_diff_sums[track_b] = [scrobble_time_diff_sums, 1]

    # perform calculations to get proximities for all proximal tracks

    # will hold results of all calculations
    track_time_proximities = {}
    num_scrobbles_overall = len(user.tracks)
    for track_b, count_and_proximals in overall_time_diff_sums.items():
        # will hold results of calculations for track b
        track_time_proximities[track_b] = {}
        for track_a, sum_and_count in count_and_proximals[0].items():
            # the total number of scrobbles of track a in the user's library
            num_scrobbles_a = overall_time_diff_sums[track_a][1]\
            # the number of scrobbles of track a that are proximal to track b
            num_scrobbles_a_prox_to_b = sum_and_count[1]
            # the total time diff between proximal tracks a and b
            time_diff_sum = sum_and_count[0]
            # time proximity calculation
            proximity = num_scrobbles_overall*time_diff_sum/(num_scrobbles_a*num_scrobbles_a_prox_to_b)
            # scaling the result
            track_time_proximities[track_b][track_a] = proximity.total_seconds()/10000

    return track_time_proximities