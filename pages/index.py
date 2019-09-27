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

            ## DATA Driven Storytelling

            The writers room for Star Trek: The Next Generation has a problem.

            They've been renewed for an eighth season, but it's been so long since
            they last wrote a script they don't know where to start. 🛸

             The producer has come to you with a simple request:

            ```"Let me know if there's any correlation between how much a character spoke and the audience reception of the episode." ```

            In order to give an informed response we need to:

            * Explore the data
            * Create a model and
            * Test the model accuracy

            ***

            View the video to understand the general line distribution for all characters
            over the course of the series, then click the Explore Data button when you are ready to begin.

            """
        ),
        dcc.Link(
        dbc.Button('Explore Data', color='primary'),
        href='/Explore',
        style={'marginLeft' : '25%'}
        )
    ],
    md=5,
)

# gapminder = px.data.gapminder()
# fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
#            hover_name="country", log_x=True, size_max=60)

column2 = dbc.Col([
    html.Iframe(
        src="https://www.youtube.com/embed/RLz025d_vJ0",
        style={'width': '100%', 'height': '80%'}
    )
    ]

)

layout = dbc.Row([column1, column2])
