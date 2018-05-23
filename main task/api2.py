import dash
import math
from flask import Markup
from flask import render_template
import matplotlib.pyplot as plt
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


@app.route('/alltrends',methods=['GET'])
def all_list():
	print("inter")
	conn = sqlite3.connect('twitter4.db')
	c = conn.cursor() 
	df = pd.read_sql("SELECT * FROM  world_trend_data", conn)
	out = df.to_json(orient='records')[1:-1].replace('},{', '} {')
	print("compl")
	print(out)
	return out

@app.route('/<string:name>',methods=['GET'])
def bar(name):
	conn=sqlite3.connect('twitter4.db')
	c=conn.cursor()
	pf=pd.read_sql("SELECT name,tweet_volume FROM "+name,conn)
	name=list(pf.name)
	tweet_volume=list(pf.tweet_volume)
	labels=[]
	values=[]
	#print(tweet_volume)
	for x in range(0,len(name)):
		if math.isnan(tweet_volume[x])==False:
			labels.append(name[x])
			values.append(tweet_volume[x])
	print(labels)
	print(values)
	#labels = ["January","February","March","April","May","June","July","August"]
	#values = [10,9,8,7,6,4,7,8]
	return render_template('bar.html', values=values, labels=labels)

@app.route('/place/<string:name>',methods=['GET'])
def all_data(name):
	conn=sqlite3.connect('twitter4.db')
	c=conn.cursor()
	df=pd.read_sql("SELECT name,query,tweet_volume FROM "+name,conn)
	out = df.to_json(orient='records')[1:-1].replace('},{', '} {')
	return out

if __name__=='__main__':
	app.run(debug=True,port=8080)	