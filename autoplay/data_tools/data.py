"""Module for getting and organizing data from LastFM API."""
import toml
import os
import pylast as pl
import logging


def get_secrets():
    """Get secret contents of secrets.toml in outer dir. Do not commit this file."""
    expected_secret_path = os.path.join(os.pardir, os.pardir, 'secrets.toml')
    secrets = toml.load(expected_secret_path)
    api_key = secrets['secrets']['api_key']
    secret = secrets['secrets']['secret']
    return api_key, secret


def get_scrobbles(username: str):
    """Get the scrobbles for a given user.

    Args:
        username (str): LastFM username
    """
    api_key, secret = get_secrets()
    network = pl.LastFMNetwork(
        api_key=api_key,
        api_secret=secret
    )

    user = network.get_user(username)
    scrobbles = user.get_recent_tracks(limit=None)

    return scrobbles


def normalize_scrobbles(scrobbles: list):
    pass


if __name__ == '__main__':
    nick = 'Nesdunk14'
    carter = 'Car_door'
    get_data(carter)