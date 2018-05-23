import dash
from flask import Markup
from flask import render_template
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import wikipedia
from flask import Flask, jsonify, request
from dash.dependencies import Output, Event, Input
import dash_core_components as dcc
import dash_html_components as html
import plotly
import random
import plotly.graph_objs as go
from collections import deque
import sqlite3
import pandas as pd
app=Flask(__name__)

@app.route('/all',methods=['GET'])
def all_list():
	conn = sqlite3.connect('twitter.db')
	c = conn.cursor() 
	df = pd.read_sql("SELECT id,name,category FROM prime_data", conn)
	out = df.to_json(orient='records')[1:-1].replace('},{', '} {')
	return out



@app.route('/id/<string:id>',methods=['GET'])
def wiki(id):
	print(id)
	conn = sqlite3.connect('twitter.db')
	c = conn.cursor() 
	df = pd.read_sql("SELECT wikipedia_search,image_file FROM prime_data where id="+str(id), conn)
	ny=wikipedia.page(list(df.wikipedia_search)[0])
	print(ny.content.split("\n\n")[0])
	l=[]
	l.append(ny.content.split("\n\n")[0])
	l.append(list(df.image_file)[0])
	return jsonify(l)



@app.route('/pie/<string:id>',methods=['GET'])
def pie(id):
	conn=sqlite3.connect('twitter.db')
	c=conn.cursor()
	labels = ['POSITIVE', 'NEGATIVE', 'NEUTRAL']
	pf=pd.read_sql("SELECT name FROM prime_data where id="+str(id),conn)
	print(str(list(pf.name)[0]))
	df = pd.read_sql("SELECT pos,neg,neu FROM sentiment_data WHERE name='"+str(list(pf.name)[0])+"'", conn)
	
	sizes = [int(df.pos),int(df.neg),int(df.neu)]
	print(sizes)
	colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
	#plt.pie(sizes, labels=labels, colors=colors,
    #              autopct='%1.1f%%', shadow=True, startangle=140)
	#plt.axis('equal')
	return render_template('chart.html', set=zip(sizes, labels, colors))


	#return plt



spp = dash.Dash(__name__,server=app)
spp.layout = html.Div(
    [   html.H2('Live Twitter Sentiment'),
        dcc.Graph(id='live-graph', animate=False),
        dcc.Location(id='url', refresh=True),
        dcc.Interval(
            id='graph-update',
            interval=1*1000
        ),
    ]
)
@spp.callback(Output('live-graph', 'figure'),
				[Input('url', 'pathname')],
              events=[Event('graph-update', 'interval')])
def update_graph_scatter(pathname):
	try:
		id=int(pathname.split('/')[2])
		conn = sqlite3.connect('twitter.db')
		c = conn.cursor()
		pf=pd.read_sql("SELECT name FROM prime_data WHERE id="+str(id),conn)
		name=list(pf.name)[0]
		temp=name.lower()
		name=""
		for i in temp:
			if i=="(" or i==")" or i=="." or i=="'" :
				continue
			elif i!=" ":
				name+=i
			else:
				name+="_"
		print(name)
		df = pd.read_sql("SELECT * FROM "+name+" ORDER BY unix DESC LIMIT 1000", conn)
		#print(list(df))
		df.sort_values('unix', inplace=True)
		df['sentiment_smoothed'] = df['sentiment'].rolling(int(len(df)/2)).mean()
		df['date'] = pd.to_datetime(df['unix'],unit='ms')
		df.set_index('date', inplace=True)
		df.dropna(inplace=True)
	  #  df=df.resampling('1s').mean
		X = df.index[-100:]
		Y = df.sentiment_smoothed[-100:]
		data = plotly.graph_objs.Scatter(
	            x=X,
	            y=Y,
	            name='Scatter',
	            mode= 'lines+markers'
	            )
		return {'data': [data],'layout' : go.Layout(xaxis=dict(range=[min(X),max(X)]),
	                                                yaxis=dict(range=[min(Y),max(Y)]),)}
	except Exception as e:
		with open('errors.txt','a') as f:
			f.write(str(e))
			f.write('\n')
dcc.Link('/rts/', href='/rts/{}'.format(12))



if __name__=='__main__':
	app.run(debug=True,port=8080)	