"""Module for classes / functions that are commmon (not specific to Apple Music or LastFM."""

from typing import List
from datetime import datetime


class Track:
    """Internal track class."""
    def __init__(self, title: str, album: str, artist: str, tags: List[dict], date: datetime):
        """Instantiate one of our internal track classes.

        Args:
            title (str): title of track
            album (str): album name the track belongs to
            artist (str): the name of the artist of the track
            tags (List[dict{str: int}]): a list of dicts containing a tag and a weight
            date (datetime): datetime that the track was listened to
        """
        self.title = title
        self.album = album
        self.artist = artist
        self.tags = tags
        self.date = date

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other_track):
        if isinstance(other_track, Track):
            return self.__key() == other_track.__key()
        return NotImplemented

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        data = [self.title, self.album, self.artist, str(self.date)]
        return ", ".join(data)

    def __key(self):
        return (self.title, self.album, self.artist)

    def get_extra_features(self):  # this function will need some brainstorming but will leave as template for now
        """Will go through some sort of API to get extra features associated with a track."""
        pass


class Artist:
    """[summary]
    """
    def __init__(self, name: str, user_plays:int) -> None:
        self.name = name
        self.user_plays = user_plays


class User:
    """Internal user class."""
    def __init__(self, username: str, tracks: List[list], artists: List[list]):
        """Instantiate one of our internal user classes.

        Args:
            username (str): user / username
            tracks (List[list]): list of track objects (timeseries)
        """
        self.username = username
        self._update_play_history(tracks, artists)

    def _update_play_history(self, tracks: List[list], artists: List[list]):  # also needs some brainstorming - not most efficient but don't have a better way without complete database
        """Update user to latest version of pulled tracks."""
        self.tracks = [Track(*track) for track in tracks]
        self.artists = [Artist(*artist) for artist in artists]
