"""Module for getting and organizing data from LastFM API."""

import toml
import os
import pylast as pl
from datetime import datetime
from typing import NamedTuple
import logging
from .common_models import Track, User


LAST_FM_TIMESTAMP_FORMAT = '%d %b %Y, %H:%M'

def get_secrets():
    """Get secret contents of secrets.toml in outer dir. Do not commit this file."""
    expected_secret_path = 'secrets.toml'
    secrets = toml.load(expected_secret_path)
    api_key = secrets['secrets']['api_key']
    secret = secrets['secrets']['secret']
    return api_key, secret


def create_network():
    """Create a pylast network for accessing the LastFM API"""
    api_key, secret = get_secrets()
    network = pl.LastFMNetwork(
        api_key=api_key,
        api_secret=secret
    )
    return network


def get_scrobbles(username: str, limit: int = None):
    """Get the scrobbles for a given user.

    Args:
        username (str): LastFM username
        limit (int): the number of scrobbles to get
    """
    network = create_network()
    user = network.get_user(username)
    scrobbles = user.get_recent_tracks(limit=limit)

    return scrobbles


def get_top_tags(scrobble: NamedTuple, tags_kept: int = 15):
    """Get up to NUM_TAGS_KEPT tags for a track if possible

    Args:
        scrobble (NamedTuple): LastFM (pylast) class of song (scrobble)
        tags_kept (int): The number of top tags to keep

    Returns:
        a list of tags
    """

    network = create_network()
    track = network.get_track(scrobble.artist, scrobble.track)

    top_tags = []
    top_tags.append(track.get_top_tags(limit=tags_kept))
    # Add more tags from album and artist if not enough
    if len(top_tags) < tags_kept:
        top_tags.append(track.get_album().get_top_tags(limit = tags_kept - len(top_tags)))
    if len(top_tags) < tags_kept:
        top_tags.append(track.get_artist().get_top_tags(limit = tags_kept - len(top_tags)))

    return top_tags


def normalize_scrobble(scrobble: NamedTuple):
    """Parse data we care about out of scrobble class.

    Args:
        scrobble (NamedTuple): LastFM (pylast) class of song (scrobble)

    Returns:
        [type]: [description]
    """
    parsed_date = datetime.strptime(scrobble.playback_date, LAST_FM_TIMESTAMP_FORMAT)
    top_tags = get_top_tags(scrobble)
    normalized = [str(scrobble.track), str(scrobble.album), str(scrobble.artist), top_tags, parsed_date]

    return normalized


def normalize_scrobbles(scrobbles: list):
    """Normalize a scrobble into something we can pass to Track class.

    Args:
        scrobbles (list): list of user scrobbles
    """
    normalized = []
    for scrobble in scrobbles:
        normalized.append(normalize_scrobble(scrobble))

    return normalized



def create_user(username: str):
    """Create a common user class from LastFM username.

    Args:
        username (str): LastFM username
    """
    scrobbles = get_scrobbles(username)
    normalized = normalize_scrobbles(scrobbles)

    return User(username, normalized)
