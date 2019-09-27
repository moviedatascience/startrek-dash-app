import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

from app import app

layout = html.Div([
    html.Div([html.H1("Impact and Importance of Relational Dialogue in TNG")], style={'textAlign': "center", 'marginTop': '5%'}),
    html.Div([
        dcc.Markdown(
        """
        ***
        ## Our Model R^2 Value:
        ### .06
         AKA 'Not Great'

         Ultimately the use case for this model is as a general guide for qualitative decision making. This should not be used as a means to determine exactly how many lines a character
         should be limited to in order to achieve a high IMDb score.

         However, we can still increase accuracy with the data we already have. 
        """
        ),
        dcc.Markdown(
        """
        ***
        """
        ),
        html.H4("Dialogue Conventions: "),
        dcc.Markdown(
        """
        We understand that there is a set amount of time for each episode. In the case of Star Trek: The Next Generation,
        that time frame is a single hour. Within that single hour there is an average of 360 lines spoken in a given episode.

        `(That's why the slider caps out at 360 on the predictions page)`

        What is also important to understand is that for every line spoken from a character, that is an opportunity cost of a line for
        another character in the series.

        We can analyze this dynamic in effect across the series in a broad sense with the three graphs below:

        """
        ),
        ], style={'textAlign': "center", 'marginTop': 10}),


        html.Div([
            html.H4("Picard VS O'Brien: "),
            html.Img(
                src="assets/op.jpg",
                style={'width': '100%', 'height': '100%', 'display': 'flex', 'marginBottom': 10}
                ),
            html.H4("Picard VS Crusher: "),
            html.Img(
                src="assets/crusher_picard.jpg",
                style={'width': '100%', 'height': '100%', 'display': 'flex', 'marginBottom': 10}
                ),
            html.H4("Crusher vs Data: "),
            html.Img(
                src="assets/data_crusher.jpg",
                style={'width': '100%', 'height': '100%', 'display': 'flex', 'marginBottom': 10}
                ),
            dcc.Markdown(
            """
            We can see from the Picard vs O'Brien graph that the trendline tilts upward,
            meaning that as Picard speaks more often, it tends to mean that O'Brien speaks less.

            However, this is not always the case. For instance, the trendline is fairly flat
            when comparing lines between Picard and Crusher. Practically, this means that these
            two characters are probably exchanging lines of dialogue between one another throughout
            the show.

            And alternatively we see that Crusher has a negative correlation to Data when it comes to
            dialogue lines spoken.


            For the Enterprise-ing young producer there may be many avenues to approach relational feature engineering to raise our R^2 score and
            find some high correlation predictive metrics.

            Whether that would yeild a return on the time and energy investment will ultimately be your decision.


            """
            ),
                ],),
    html.Div([
        dcc.Link(
        dbc.Button('Return to Predictions', color='primary'),
        href='/Predict',
        # style={'marginRight' : '75%', 'marginTop': 5}
        ),
        dcc.Link(
        dbc.Button('Continue to Conclusions', color='primary'),
        href='/Conclusions',
        style={'marginLeft' : '65%'}
        )
        ]),

    # html.Div([
    #     dcc.Link(
    #     dbc.Button('Predict', color='primary'),
    #     href='/Predict',
    #     style={'marginLeft' : '75%', 'marginTop': 5})
    #     ]),

]),
