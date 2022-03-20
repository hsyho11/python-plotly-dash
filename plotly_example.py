'''
Terminal
!pip install dash==0.26.5  # The core dash backend
!pip install dash-html-components==0.12.0  # HTML components
!pip install dash-core-components==0.28.0  # Supercharged components
!pip install dash_bootstrap_components==0.13.1
'''

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
# create dash
app = Dash(__name__)

colors = {
    'background': '#FFFFFF',
    'text': '#288CC2'
}

### bar chart example 
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})
fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
fig.update_layout(
    #plot_bgcolor=colors['background'],
    #paper_bgcolor=colors['background'],
    font_color=colors['text']
)

### scatter plot example
df2 = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')
fig2 = px.scatter(df2, x="gdp per capita", y="life expectancy",
                 size="population", color="continent", hover_name="country",
                 log_x=True, size_max=60)

fig2.update_layout(
	font_color=colors['text'])

### violin plot example 1
df3 = pd.DataFrame(
    {'x':np.tile(['no', 'yes'], 80000),
     'y':np.random.normal(0, 1, 160000), 
     'cl':np.repeat([0, 1], 80000)

    }
)

fig3 = px.violin(df3, x="x", y="y", color='cl', box=True, hover_data=df3.columns)
fig4 = px.violin(df3, y="y", color='cl',
                violinmode='overlay', # draw violins on top of each other
                # default violinmode is 'group' as in example above
                hover_data=df3.columns)


### violin plot example 2
df4 = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/violin_data.csv")

fig5 = go.Figure()

fig5.add_trace(go.Violin(x=df4['day'][ df4['smoker'] == 'Yes' ],
                        y=df4['total_bill'][ df4['smoker'] == 'Yes' ],
                        legendgroup='Yes', scalegroup='Yes', name='Yes',
                        side='negative',
                        line_color='blue')
             )
fig5.add_trace(go.Violin(x=df4['day'][ df4['smoker'] == 'No' ],
                        y=df4['total_bill'][ df4['smoker'] == 'No' ],
                        legendgroup='No', scalegroup='No', name='No',
                        side='positive',
                        line_color='orange')
             )
fig5.update_traces(meanline_visible=True) # orientation='h' -> horizontal
fig5.update_layout(violingap=0, violinmode='overlay')

### subplot example
df5 = px.data.iris()
fig6 = make_subplots(rows=1,
                    cols=2,
                    subplot_titles=[
                        'Fruit',  # 1. subplot title
                        'City'  # 2. subplot title
])

fig6.add_trace(go.Bar(x=df['Fruit'], y=df['Amount']),row=1, col=1)

fig6.add_trace(go.Bar(x=df['City'], y=df['Amount'], text=df['Amount'],
            textposition='auto',), row=1, col=2)

fig6.update_layout(title='Count', title_x=0.5)


# set the web layout
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    
    html.H1(
        children='Hello Dash',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Dash: A web application framework for your data.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='example-graph-1',
        figure=fig
    ),

    dcc.Graph(
        id='example-graph-2',
        figure=fig2
    ),

    dcc.Graph(
		id='example-graph-3',
		figure=fig3
	),

    
    dcc.Graph(
        id='example-graph-5',
        figure=fig5
    ),

    dcc.Graph(
        id='example-graph-6',
        figure=fig6
    ),

])

if __name__ == '__main__':
    app.run_server(debug=True)
