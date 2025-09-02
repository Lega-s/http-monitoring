from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
from datetime import datetime, timedelta
import textwrap
import csv
import os

dateparse = lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
df = pd.read_csv('data.csv', parse_dates=['timestamp'], date_parser=dateparse)

app = Dash()

TIME_OPTIONS = {
    "Last 5 minutes": timedelta(minutes=5),
    "Last 30 minutes": timedelta(minutes=30),
    "Last 1 hour": timedelta(hours=1),
    "Last 5 hours": timedelta(hours=5),
    "Last 24 hours": timedelta(days=1),
    "Last 72 hours": timedelta(days=3),
    "All time": None
}

app.layout = html.Div([
    html.H1(children='Google Monitoring'),
    html.H3(id='average-latency', children='Durchschnittslatenz: wird geladen...'),
    dcc.Dropdown(
        id='dropdown-selection',
        options=[{'label': label, 'value': label} for label in TIME_OPTIONS],
        value='All time'
    ),
    dcc.Graph(id='graph'),
    dcc.Interval(id='interval-component', interval=180*1000, n_intervals=0),
    dcc.Store(id='interval-store', data=120000)
])

@callback(
    Output('graph', 'figure'),
    Output('average-latency', 'children'),
    [Input('dropdown-selection', 'value'),
     Input('interval-component', 'n_intervals')]
)

def update_graph(selected_range, n_intervals):
    df = pd.read_csv('data.csv', parse_dates=['timestamp'], date_parser=dateparse)
    now = datetime.now()

    if TIME_OPTIONS[selected_range] is not None:
        min_time = now - TIME_OPTIONS[selected_range]
        dff = df[(df['timestamp'] >= min_time) & (df['latency_ms'].notna())]
    else:
        dff = df[df['latency_ms'].notna()]

    if dff.empty:
        fig = px.line(title="No data in selected time range")
        fig.update_layout(
            plot_bgcolor='#1e1e1e',
            paper_bgcolor='#1e1e1e',
            font=dict(color='white'),
            xaxis=dict(color='white', gridcolor='#444'),
            yaxis=dict(color='white', gridcolor='#444')
        )
        avg_text = "No data in current Timeoption"
    else:
        dff['error_wrapped'] = dff['error'].fillna('').apply(
            lambda e: '<br>'.join(textwrap.wrap(str(e), width=50))
        )


        fig = px.line(
            dff,
            x='timestamp',
            y='latency_ms',
            color='client_id',
            hover_data={'error_wrapped': True},
            title=f"Response Time ({selected_range})",
            markers=True
        )
        fig.update_layout(
            plot_bgcolor='#1e1e1e',
            paper_bgcolor='#1e1e1e',
            font=dict(color='white'),
            xaxis=dict(color='white', gridcolor='#444'),
            yaxis=dict(color='white', gridcolor='#444')
        )
        avg_latency = dff['latency_ms'].mean()
        avg_text = f"Average Latency: {avg_latency:.2f} ms"

    return fig, avg_text
        

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8050, debug=True)
