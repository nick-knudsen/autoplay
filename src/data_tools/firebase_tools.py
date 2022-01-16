from firebase_admin import credentials, initialize_app, firestore


def create_network():
    """creates connection to Firebase API

    Returns:
        Firestore DataBase Object: reference to the autoplay Firestore DB
    """
    cred = credentials.Certificate('firebase_secret.json') # Hard coded path for now
    initialize_app(cred)
    return firestore.client()


def write_artist_dict(artist_name: str, artist_dict: dict) -> None:
    """[summary]

    Args:
        artist_name (str): [description]
        artist_dict (dict): [description]
    """
    db = create_network()
    artist_name = artist_name.lower()
    