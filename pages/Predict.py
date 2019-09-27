import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from joblib import load
import pandas as pd
from app import app

pipeline = load('assets/linear.joblib')

column1 = dbc.Col(
    [
        dcc.Markdown(
        '## Prediction Imputs', className='mb-5',
        style={'textAlign': 'center', "marginTop" : '5%'}
        ),
        dcc.Markdown(
        '#### Character',
        style={'textAlign': 'center'}
        ),
        dcc.Dropdown(
            id='Character',
            options = [
                {'label': 'TASHA', 'value': 'TASHA'},
                {'label': "K'EHLEYR", 'value': "K'EHLEYR"},
                {'label': 'PICARD', 'value': 'PICARD'},
                {'label': "O'BRIEN", 'value': "O'BRIEN"},
                {'label': 'RIKER', 'value': 'RIKER'},
                {'label': 'OGAWA', 'value': 'OGAWA'},
                {'label': "JELLICO", 'value': "JELLICO"},
                {'label': 'COMPUTER', 'value': 'COMPUTER'},
                {'label': "WESLEY", 'value': "WESLEY"},
                {'label': 'PULASKI', 'value': 'PULASKI'},
                {'label': 'ALEXANDER', 'value': 'ALEXANDER'},
                {'label': "GUINAN", 'value': "GUINAN"},
                {'label': 'TROI', 'value': 'TROI'},
                {'label': "LWAXANA", 'value': "LWAXANA"},
                {'label': 'WORF', 'value': 'WORF'},
                {'label': 'DATA', 'value': 'DATA'},
                {'label': "BARCLAY", 'value': "BARCLAY"},
                {'label': 'LAFORGE', 'value': 'LAFORGE'},
                {'label': "CRUSHER", 'value': "CRUSHER"},
                {'label': 'VASH', 'value': 'VASH'},
            ],
            value = 'PICARD',
            className='mb-5',
            style={'textAlign': 'center'}
        ),


        dcc.Markdown(
        '#### Lines',
        style={'textAlign': 'center'}
        ),


        dcc.Slider(
            id='Line_Count',
            marks={
                0: '0',
                50: '50',
                100: '100',
                150: '150',
                200: '200',
                250: '250',
                300: '300',
                360: '360'
                },
            min=0,
            max=360,
            step=1,
            value=0,
            className='mb-5',
        ),

        html.Div(
        id='slider-output-container',
        style={'textAlign': 'center', 'marginTop': 0}
        ),

        dcc.Markdown(
            """
            ***

            ## Linear Regression Model

            ***

            Take a moment to explore the relationship between characters and
            line counts above.

            Just like in the exploration page, the dropdown menu has each of the top
            20 characters by line count throughout the entire seven season run.

            Adjusting the slider for the lines will result in the predicted average
            IMDb rating to be adjusted as well.

            The main takeaways we can find from the Linear Regression model
            is that the assumptions we made during exploration can be verified:

            * The more Pulaski speaks, the more likely the IMDb rating will decline
            * The more Jellico and Ogawa speak, the more likely the IMDb rating will increase
            * Picard can seemingly talk as much as he wants and it won't affect the ratings

            ***

            Once you've reviewed the code we can dive a little deeper on our analysis.

            """
        ),
        dcc.Link(
        dbc.Button('Back to Explore', color='primary'),
        href='/Explore',
        style={'marginTop': '50%'}
        ),

    ],
)
column2 = dbc.Col(
    [
        html.Div(children=[
            dcc.Markdown(
            """
            ***
            """
            ),
            html.H1('Projected Rating', className='mb-5', style={'textAlign': 'center'}),
            html.Div(id='prediction-content', className='lead', style={'marginBottom': '10%', 'textAlign': 'center'}),
            dcc.Markdown(
            """
            ***
            """
            )
            ],
            # html.Iframe(src='assets/Linear_Note.html')
            # style={'display' : 'flex'}
            ),
    html.Iframe(
        src="assets/Linear_Note.html",
        style={'width': '100%', 'height': '70%'}
    ),

    dcc.Link(
    dbc.Button('Continue to Analyze', color='primary'),
    href='/Analyze',
    style={'marginLeft' : '70%'}
    ),
    ],
     # style={'textAlign': 'center'},
    # lg=8,
)


@app.callback(
    dash.dependencies.Output('slider-output-container', 'children'),
    [dash.dependencies.Input('Line_Count', 'value')])
def update_output(value):
    return '{} Lines'.format(value)

@app.callback(
    Output('prediction-content', 'children'),
    [Input('Character', 'value'), Input('Line_Count', 'value')],
)
def predict(Character, Line_Count):
    df = pd.DataFrame(
        columns=['Character', 'Line_Count'],
        data=[[Character, Line_Count]]
    )
    y_pred = pipeline.predict(df)
    return dcc.Markdown('#### Average IMDb Rating:' + f' {y_pred[0]:.01f} '),

layout = dbc.Row([column1, column2])
