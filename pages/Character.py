import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from joblib import load
pipeline = load('assets/pipeline4.joblib')

from app import app

column1 = dbc.Col(
    [
        dcc.Markdown('## Predictions', className='mb-5'),
        dcc.Markdown('#### Lines'),
        dcc.Slider(
            id='Line_Count',
            min=0,
            max=360,
            step=1,
            value=100,
            marks={n: str(n) for n in range(0,360,1)},
            className='mb-5',
        ),
        dcc.Markdown('#### Character'),
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
        ),
    ],
    md=4,
)
column2 = dbc.Col(
    [
        html.H2('Projected Rating', className='mb-5'),
        html.Div(id='prediction-content', className='lead')
    ]
)

import pandas as pd

@app.callback(
    Output('prediction-content', 'children'),
    [Input('Line_Count', 'value'), Input('Character', 'value')],
)
def predict(Character, Line_Count):
    df = pd.DataFrame(
        columns=['Character', 'Line_Count'],
        data=[['Character', Line_Count]]
    )
    y_pred = float(pipeline4.predict(df))
    return f'Projected Rating: {y_pred:.0f} '

layout = dbc.Row([column1, column2])
