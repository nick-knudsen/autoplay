"""Module for classes / functions that are commmon (not specific to Apple Music or LastFM."""

from typing import List
from datetime import datetime


class Track:
    """Internal track class."""
    def __init__(self, title: str, album: str, artist: str, date: datetime):
        """Instantiate one of our internal track classes.

        Args:
            title (str): title of song/track
            album (str): album name the song/track belongs to
            date (datetime): datetime that the track was listened to
        """
        self.title = title
        self.album = album
        self.artist = artist
        self.date = date

    def get_extra_features(self):  # this function will need some brainstorming but will leave as template for now
        """Will go through some sort of API to get extra features associated with a track."""

        # get track top tags
        

    def equals(self, other_track):
        """Check to see if this track and another are the same track"""
        return self.title == other_track.title and self.album == other_track.album and self.artist == other_track.artist
    


class User:
    """Internal user class."""
    def __init__(self, username: str, tracks: List[list]):
        """Instantiate one of our internal user classes.

        Args:
            username (str): user / username
            tracks (List[list]): list of track objects (timeseries)
        """
        self.username = username
        self._update_play_history(tracks)

    def _update_play_history(self, tracks: List[list]):  # also needs some brainstorming - not most efficient but don't have a better way without complete database
        """Update user to latest version of pulled tracks."""
        self.tracks = [Track(*track) for track in tracks]
