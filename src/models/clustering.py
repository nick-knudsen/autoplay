from sklearn.cluster import KMeans
import numpy as np

from ..data_tools.common_models import Track, User


def find_fully_connected_subgraphs(time_proximities: dict[Track, dict[Track, float]]):
    """Iterates over the tracks, building fully connected subgraphs
    
    Args:
        time_proximities (Dict[Track, Dict[Track, float]]): contains a metric for time proximity for pairs of tracks
        
    Returns:
        [type]: [description]    
    """
    pass