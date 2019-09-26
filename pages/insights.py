import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
from app import app
import plotly.graph_objs as go

df = pd.read_csv(r'C:\Users\Eric\startrek-dash-app\assets\df')

character_names = df['Character'].unique()

layout = html.Div([
    html.Div([html.H1("Character Line Counts and Average Ratings Per Episode")], style={'textAlign': "center"}),
    html.Div([
        dcc.Dropdown(
            id='character-names-option',
            options=[{'label' : i, 'value' : i} for i in character_names],
            value='PICARD'
            ),
        dcc.Graph(id='graph-with-slider'),
        dcc.Slider(
            id='seasons--slider',
            min=df['Seasons'].min(),
            max=df['Seasons'].max(),
            value=df['Seasons'].min(),
            marks={str(season): str(season) for season in df['Seasons'].unique()},
        ),
        #text that I want

        dcc.Graph(id='new'),
        dcc.Input(id='dummy', value='dummy')
    ],
    style={'width': '100%', 'display': 'inline-block'})
])

@app.callback(
    Output('new', 'figure'),
    [Input('dummy', 'value')]
)

def explore_new(dummy):
    traces = go.Scatter(x=df['Line_Count'], y=df['Rating'], trendline='ols', color='Character'),
    return {'data': traces}

@app.callback(
    Output('graph-with-slider', 'figure'),
    [Input('seasons--slider', 'value'),
    Input('character-names-option', 'value')])

def update_graph(selected_season, selected_character):
    df_each_season = df[df['Seasons'] == selected_season]
    df_each_character = df_each_season[df_each_season['Character'] == selected_character]
    df_each_lines = df_each_character.groupby('Episode')['Line_Count'].mean().reset_index()
    df_each_rating = df_each_season.groupby('Episode')['Rating'].mean().reset_index()
    bar_values = go.Bar(
        x=df_each_lines['Episode'],
        y=df_each_lines['Line_Count'],
        name='Character Lines Per Episode'
    )
    line_values = go.Scatter(
            x=df_each_rating['Episode'],
            y=df_each_rating['Rating'],
            yaxis="y2",
            xaxis="x",
            mode='lines+markers',
            name='Episode Ratings',
            connectgaps = True
    )
    traces = [bar_values, line_values]
    layout = go.Layout(
        title="Ratings for Each Episode and How Much The Selected Character Spoke",
        margin={"l": 100, "r": 100},
        colorway=["#287D95", "#EF533B"],
        yaxis={'title': f'Lines Per Episode', "range": [0, 200]},
        yaxis2={'title': f'Rating Per Episode', 'overlaying': 'y', 'side': 'right',
                "range": [0, 10], "showgrid": False},
        xaxis={"title": "Episode Number"}
    )

    fig = go.Figure(data=traces, layout=layout)
    return fig

# layout = dbc.Row([column2])
