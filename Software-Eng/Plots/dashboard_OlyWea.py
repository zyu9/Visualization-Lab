import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df1 = pd.read_csv('../Datasets/Olympic2016Rio.csv')
df2 = pd.read_csv('../Datasets/Weather2014-15.csv')

app = dash.Dash()

# Bar chart data
barchart_df = df1.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
barchart_df = df1.groupby(['NOC'])['Total'].sum().reset_index()
barchart_df = df1.sort_values(by=['Total'], ascending=[False]).head(20)
data_barchart = [go.Bar(x=df1['NOC'], y=df1['Total'])]

# Stack bar chart data
stackbarchart_df = df1.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
stackbarchart_df = stackbarchart_df.groupby(['NOC']).agg(
    {'Total': 'sum','Gold':'sum', 'Silver':'sum', 'Bronze':'sum'}).reset_index()
stackbarchart_df = stackbarchart_df.sort_values(by=['Total'], ascending=[False]).head(20)
trace1_stackbarchart = go.Bar(x=stackbarchart_df['NOC'], y=stackbarchart_df['Gold'], name='Gold',
                              marker={'color': '#FFD700'})
trace2_stackbarchart = go.Bar(x=stackbarchart_df['NOC'], y=stackbarchart_df['Silver'], name='Silver',
                              marker={'color': '#9EA0A1'})
trace3_stackbarchart = go.Bar(x=stackbarchart_df['NOC'], y=stackbarchart_df['Bronze'], name='Bronze',
                              marker={'color': '#CD7F32'})
data_stackbarchart = [trace1_stackbarchart, trace2_stackbarchart, trace3_stackbarchart]

# Line Chart
line_df = df2
#line_df['Date'] = pd.to_datetime(line_df['Date'])
data_linechart = [go.Scatter(x=line_df['month'], y=line_df['actual_max_temp'], mode='lines', name='actual max temp')]

# Multi Line Chart
multiline_df = df2
#multiline_df['Date'] = pd.to_datetime(multiline_df['Date'])
trace1_multiline = go.Scatter(x=multiline_df['month'], y=multiline_df['actual_max_temp'], mode='lines', name='actual max temp')
trace2_multiline = go.Scatter(x=multiline_df['month'], y=multiline_df['actual_mean_temp'], mode='lines', name='actual mean temp')
trace3_multiline = go.Scatter(x=multiline_df['month'], y=multiline_df['actual_min_temp'], mode='lines', name='actual min temp')
data_multiline = [trace1_multiline, trace2_multiline, trace3_multiline]

# Bubble chart
bubble_df = df2.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
bubble_df = bubble_df.groupby(['month']).agg(
    {'average_min_temp': 'sum', 'average_max_temp': 'sum'}).reset_index()
data_bubblechart = [
    go.Scatter(x=bubble_df['month'],
               y=bubble_df['average_min_temp'],
               text=bubble_df['average_max_temp'],
               mode='markers',
               marker=dict(size=bubble_df['average_min_temp']/100,
               color=bubble_df['average_min_temp']/100,
               showscale=True))
]

# Heatmap
data_heatmap = [go.Heatmap(x=df2['day'],
                   y=df2['month'],
                   z=df2['record_max_temp'].values.tolist(),
                   colorscale= 'Jet')]

# Layout
app.layout = html.Div(children=[
    html.H1(children='Python Dash',
            style={
                'textAlign': 'center',
                'color': '#ef3e18'
            }
            ),
    html.Div('Web dashboard for Data Visualization using Python', style={'textAlign': 'center'}),
    html.Div('Medals of Olympic 2016 of 20 first top countries', style={'textAlign': 'center'}),
    html.Br(),
    html.Br(),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Bar chart', style={'color': '#df1e56'}),
    html.Div('This bar chart represent the total medals of Olympic 2016 of 20 first top countries.'),
    dcc.Graph(id='graph1',
              figure={
                  'data': data_barchart,
                  'layout': go.Layout(title='Total medals of Olympic 2016 of 20 first top countries', xaxis_title="Country",
                   yaxis_title="Number of Total Medals")
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Stack bar chart', style={'color': '#df1e56'}),
    html.Div(
        'This stack bar chart represent medals in the first 20 country for Olympic 2016.'),
    dcc.Graph(id='graph2',
              figure={
                  'data': data_stackbarchart,
                  'layout': go.Layout(title='Medals in the first 20 country for Olympic 2016', xaxis_title="Country",
                   yaxis_title="Number of medals", barmode= 'stack')
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Line chart', style={'color': '#df1e56'}),
    html.Div('This line chart represent the actual maximum temperature.'),
    dcc.Graph(id='graph3',
              figure={
                  'data': data_linechart,
                  'layout': go.Layout(title= 'Actual Maximum Temperature ',
                   xaxis_title= "Month", yaxis_title= "Actual Max Temp")
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Multi Line chart', style={'color': '#df1e56'}),
    html.Div(
        'This line chart represent the actual tempeature '),
    dcc.Graph(id='graph4',
              figure={
                  'data': data_multiline,
                  'layout': go.Layout(title= 'Actual Temperature',
                   xaxis_title= "Month", yaxis_title= "Actual Temperature")
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Bubble chart', style={'color': '#df1e56'}),
 html.Div(
        'This bubble chart represent the Average min and max temperature of each month .'),
    dcc.Graph(id='graph5',
              figure={
                  'data': data_bubblechart,
                  'layout': go.Layout(title= 'Average min and max temperature of each month',
                   xaxis_title="Month", yaxis_title="Average temperature")
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Heat map', style={'color': '#df1e56'}),
    html.Div(
        'This heat map represent the recorded max temperature on day of week and month of year.'),
    dcc.Graph(id='graph6',
              figure={
                  'data': data_heatmap,
                  'layout': go.Layout(title= 'Recorded max temperature on day of week and month of year',
                   xaxis_title="Day of week", yaxis_title="Month of year")
              }
              )
])

if __name__ == '__main__':
    app.run_server()
