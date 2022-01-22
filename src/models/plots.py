from plotly import graph_objects as go
import plotly.express as px


from .models import generic_overlap, ComparisonLevel


def test_overlap(user_a, user_b):
    ratio = generic_overlap(user_a, user_b, ComparisonLevel.SONG)

    return ratio
