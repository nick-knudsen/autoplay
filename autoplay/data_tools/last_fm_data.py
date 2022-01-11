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
    """Get up to tags_kept tags for a track if possible

    Args:
        scrobble (NamedTuple): LastFM (pylast) class of song (PlayedTrack)
        tags_kept (int): The number of top tags to keep

    Returns:
        a list of dicts: the tag (key) and its weight (value)
    """
    track = scrobble.track
    top_tags = []
    top_tags.extend(track.get_top_tags(limit=tags_kept))
    """Slows down scraping significantly, commented out until a faster method is found"""
    # Add more tags from album and artist if not enough
    # if len(top_tags) < tags_kept:
    #     try:
    #         top_tags.extend(track.get_album().get_top_tags(limit = tags_kept - len(top_tags)))
    #     # cannot find album via track, search for it
    #     except (AttributeError, pl.WSError) as e:
    #         network = create_network()
    #         try:
    #             network.search_for_album(scrobble.album).get_next_page()[0].get_top_tags(limit = tags_kept - len(top_tags))
    #         # no results found for search
    #         except IndexError:
    #             print(scrobble.album)
    #             pass
    # if len(top_tags) < tags_kept:
    #     top_tags.extend(track.get_artist().get_top_tags(limit = tags_kept - len(top_tags)))
    
    # parse tag data
    parsed_tags = []
    for tag in top_tags:
        parsed_tags.append({str(tag.item): tag.weight})

    return parsed_tags


def normalize_scrobble(scrobble: NamedTuple):
    """Parse data we care about out of scrobble class.

    Args:
        scrobble (NamedTuple): LastFM (pylast) class of song (scrobble)

    Returns:
        [type]: [description]
    """
    parsed_date = datetime.strptime(scrobble.playback_date, LAST_FM_TIMESTAMP_FORMAT)
    #top_tags = get_top_tags(scrobble)
    top_tags=[]
    try:
        artist, title = str(scrobble.track).split(" - ", 1)
    except ValueError:
        print(str(scrobble.track))
    normalized = [title, str(scrobble.album), artist, top_tags, parsed_date]

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



def create_user(username: str, limit: int = None):
    """Create a common user class from LastFM username.

    Args:
        username (str): LastFM username
        limit (int): The number of scrobbles to fetch
    """
    scrobbles = get_scrobbles(username, limit)
    normalized = normalize_scrobbles(scrobbles)

    return User(username, normalized)
