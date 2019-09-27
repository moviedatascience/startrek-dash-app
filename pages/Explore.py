import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
from app import app
import plotly.graph_objs as go

df = pd.read_csv('assets/df')
acc = pd.read_csv('assets/acc')

character_names = df['Character'].unique()

layout = html.Div([
    html.Div([html.H1("Character Line Counts and Average Ratings Per Episode")], style={'textAlign': "center", 'marginTop': '5%'}),
    html.Div([
    html.Div([
        dcc.Dropdown(
            id='character-names-option',
            options=[{'label' : i, 'value' : i} for i in character_names],
            value='PICARD',
            style={'align': 'center', 'textAlign': "center", 'width' : '50%', 'marginTop': 10, 'marginBottom': 10, 'marginLeft' : '25%'}
            ),
            ]),
        dcc.Graph(id='graph-with-slider'),
        html.Div([html.H4("Season #: ")], style={'textAlign': "center", 'marginTop': 10}),
        dcc.Slider(
            id='seasons--slider',
            min=df['Seasons'].min(),
            max=df['Seasons'].max(),
            value=df['Seasons'].min(),
            marks={str(season): str(season) for season in df['Seasons'].unique()},),

            ]),

    html.Div([
    html.Div([html.H2("KMeans Clustered Line Counts With OLS Line For Each Character:")], style={'textAlign': "center", 'marginTop': '5%'}),
        html.Img(
                src="assets/trendline.jpg",
                style={'width': '100%', 'height': '50%', 'marginTop': 50, 'display': 'flex', 'marginBottom': 10}
                ),
        dcc.Markdown(
        """
        ***
        ### Key Takeaways:
        * The more Pulaski speaks, the more likely the IMDb rating will decline
        * The more Jellico and Ogawa speak, the more likely the IMDb rating will increase
        * Picard can seemingly talk as much as he wants and it won't affect the ratings
        """
        ),
            ]),
    html.Div([
        dcc.Link(
        dbc.Button('Back Home', color='primary'),
        href='/',
        # style={'marginRight' : '75%', 'marginTop': 5}
        ),
        dcc.Link(
        dbc.Button('Continue to Predict', color='primary'),
        href='/Predict',
        style={'marginLeft' : '75%'}
        )
        ]),

    # html.Div([
    #     dcc.Link(
    #     dbc.Button('Predict', color='primary'),
    #     href='/Predict',
    #     style={'marginLeft' : '75%', 'marginTop': 5})
    #     ]),

]),


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
        # title="Ratings for Each Episode and How Much The Selected Character Spoke",
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
