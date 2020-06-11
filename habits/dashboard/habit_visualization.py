import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from plotly.offline import plot
import plotly.graph_objs as go
import plotly.express as px
import logging

from dashboard.models import Activity
from dashboard.models import Category


def weekly_report():
    activity = Activity.objects.select_related('category')
    activity_values = activity.values("date", "category__name")
    frequency_df = pd.DataFrame(list(activity_values))

    logging.warning(activity.query)
    logging.warning(frequency_df.head())


    frequency_df.insert(2, "frequency", 1)
    frequency_df['date'] = pd.to_datetime(frequency_df['date'], errors='coerce')
    frequency_df = frequency_df.sort_values('date').sort_values('category__name')
    frequency_df['date'] = frequency_df['date'].dt.strftime("%a")
    frequency_df = frequency_df.set_index(['category__name', 'date'])

    frequency_by_activity = frequency_df.groupby(level=0).sum().reset_index()
    frequency_by_date = frequency_df.groupby(level=1).sum().reset_index()

    frequency_df = frequency_df.reset_index()
    frequency_by_both = frequency_df.groupby(['category__name', 'date']).sum()

    activity_types = frequency_by_both.index.get_level_values(0).unique()
    logging.warning(frequency_by_activity.head())
    fig = px.bar(frequency_by_activity, x='category__name', y='frequency')
    #bar = go.bar(frequency_by_activity, x='category__name', y='frequency')
    #fig.add_trace(bar)
    plt_div = plot(fig, output_type='div')
    return plt_div