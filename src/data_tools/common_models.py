"""Module for classes / functions that are commmon (not specific to Apple Music or LastFM."""

from __future__ import annotations
from datetime import datetime


class Track:
    """Internal track class."""
    def __init__(self, title: str, album: str, artist: str, tags: list[dict], date: datetime):
        """Instantiate one of our internal track classes.

        Args:
            title (str): title of track
            album (str): album name the track belongs to
            artist (str): the name of the artist of the track
            tags (list[dict{str: int}]): a list of dicts containing a tag and a weight
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


class User:
    """Internal user class."""
    def __init__(self, username: str, tracks: list[list]):
        """Instantiate one of our internal user classes.

        Args:
            username (str): user / username
            tracks (list[list]): list of track objects (timeseries)
        """
        self.username = username
        self._update_play_history(tracks)

    def _update_play_history(self, tracks: list[list]):  # also needs some brainstorming - not most efficient but don't have a better way without complete database
        """Update user to latest version of pulled tracks."""
        self.tracks = [Track(*track) for track in tracks]


    def filter_tracks_date(self, time_from: datetime, time_to: datetime):
        """Filter user tracks into a specific time bin.

        Args:
            time_from (datetime): start cutoff time
            time_to (datetime): end cutoff time
        """
        if time_from is None:
            time_from = self.tracks[-1].date
        if time_to is None:
            time_to = self.tracks[0].date

            self.tracks = [track for track in self.tracks if time_from <= tack.date <= time_to]

    def filter_artists_date(self, time_from: datetime, time_to: datetime):
        """Filter user tracks into a specific time bin.

        Args:
            time_from (datetime): start cutoff time
            time_to (datetime): end cutoff time
        """
        pass   # TODO: needs special implementation and refactor of get_artists

    @property
    def tracks_frequency_dict(self):
        """Create a frequency dictionary of the tracks."""
        frequency = {}
        for track in self.tracks:
            if track in frequency:
                frequency[track] += 1
            else:
                frequency[track] = 1

        return frequency

    @property
    def artists_frequency_dict(self):
        """Create a frequency dictionary of the artists."""
        raise NotImplementedError
        frequency = {}
        for artist in self.artists:
            frequency[artist] = artist.user_plays

        return frequency
