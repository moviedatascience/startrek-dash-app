import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

from app import app

"""
https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout

Layout in Bootstrap is controlled using the grid system. The Bootstrap grid has
twelve columns.

There are three main layout components in dash-bootstrap-components: Container,
Row, and Col.

The layout of your app should be built as a series of rows of columns.

We set md=4 indicating that on a 'medium' sized or larger screen each column
should take up a third of the width. Since we don't specify behaviour on
smaller size screens Bootstrap will allow the rows to wrap so as not to squash
the content.
"""

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
            ## Data is the Guide, not the Target
            ***

            We, as people trying to improve on an already great product, need to remember that the goal is not to get a great IMDb score.

            *The goal is to make a great show.*

            The higher ratings are a product of reaching our goal, but should not be confused with being the goal itself.

            ***

            Machine Learning and statistical models can aid us in the decision making process, but there is simply not enough data
            in this methodology to make decisions for us.

            ***

            "All models are wrong. Some are useful."

            ***

            """
        ),
        html.H5("All Source Code Here: "),
        dcc.Link(
        dbc.Button('Github Repo', color='primary'),
        href='https://github.com/moviedatascience/startrek-dash-app',
        # style={'marginLeft' : "20%"}
        ),
        html.H5("Raw Script Data Here: "),
        dcc.Link(
        dbc.Button('All Scripts Source', color='secondary'),
        href='http://www.chakoteya.net/StarTrek/index.html',
        # style={'marginRight' : "20%"}
        ),
        html.H5("Direct Link To Racing Bar Video: "),
        dcc.Link(
        dbc.Button('Racing Bar Graph', color='primary'),
        href='http://www.chakoteya.net/StarTrek/index.html',
        # style={'marginBottom' : "20%"}
        ),
        html.H5("Back To The Front Page: "),
        dcc.Link(
        dbc.Button('Home', color='secondary'),
        href='/',
        # style={'marginTop' : "20%"}
        ),
    ],
    md=5,
)

# gapminder = px.data.gapminder()
# fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
#            hover_name="country", log_x=True, size_max=60)

column2 = dbc.Col([
    dcc.Link(
    html.Img(
        src="assets/sitepic.jpg",
        style={'width': '100%', 'height': '100%'}
            ), href='http://www.chakoteya.net/StarTrek/index.html',)
    ]
                )

layout = dbc.Row([column1, column2])
