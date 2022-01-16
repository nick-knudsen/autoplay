from plotly import graph_objects as go
import plotly.express as px


from .models import generic_overlap, ComparisonLevel


def test_overlap(user_a, user_b):
    generic_overlap(user_a, user_b, ComparisonLevel.SONG)