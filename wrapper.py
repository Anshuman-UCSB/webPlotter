import dash 
from dash.dependencies import Output, Input
import dash_core_components as dcc 
import dash_html_components as html 
import plotly 
import random 
import plotly.graph_objs as go
import csv
filename = "data.csv"


X = [1]
Y = [1]

app = dash.Dash(__name__) 

app.layout = html.Div( 
	[ 
		dcc.Graph(id = 'live-graph', animate = False), 
		dcc.Interval( 
			id = 'graph-update', 
			interval = 500, 
			n_intervals = 0
		), 
	] 
) 

@app.callback( 
	Output('live-graph', 'figure'), 
	[ Input('graph-update', 'n_intervals') ] 
) 

def update_graph_scatter(n): 
	X = []
	Y = []
	with open(filename,'rt') as f:
		data = csv.reader(f)
		for row in data:
				X.append(int(row[0]))
				Y.append(int(row[1]))
	data = plotly.graph_objs.Scatter( 
			x=list(X), 
			y=list(Y), 
			name='Scatter', 
			mode= 'lines+markers'
	) 

	return {'data': [data], 
			'layout' : go.Layout(xaxis=dict(range=[min(X),max(X)]),yaxis = dict(range = [min(Y),max(Y)]),)} 

if __name__ == '__main__': 
	app.run_server()
