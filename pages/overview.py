import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from joblib import load
import pandas as pd
import plotly.graph_objs as go
from app import app

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('assets/df')

character_names = df['Character'].unique()

app.layout = html.Div([
    html.Div([
        dcc.Dropdown(
            id='character-names-option'
            options=[{'label' : i, 'value' : i} for i in character_names]
            value='PICARD'
            )
        dcc.Graph(id='graph-with-slider'),
        dcc.Slider(
            id='seasons--slider',
            min=df['Seasons'].min(),
            max=df['Seasons'].max(),
            value=df['Seasons'].min(),
            marks={str(season): str(season) for season in df['Seasons'].unique()}
        ),
    ],
    style={'width': '100%', 'display': 'inline-block'}),
])

@app.callback(
    Output('graph-with-slider', 'figure'),
    [Input('seasons--slider', 'value'),
    Input('character-names-option', 'value')])
def update_graph(selected_character, selected_season):
    df_each_season = df[df['Seasons'] == selected_season]
    df_each_character = df[df['Character'] == selected_character]
    line_values = []
    df_each_rating = df_each_season.groupby('Episode')['Rating'].mean().reset_index()
        line_values.append(go.Scatter(
            x=df_rating_by_ep['Episode'],
            y=df_rating_by_ep['Rating'],
            connectgaps = True
        ))

    return {'data': line_values}
