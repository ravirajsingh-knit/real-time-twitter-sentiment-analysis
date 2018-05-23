#import dash
from flask import Markup
#from flask import render_template
#import matplotlib
#matplotlib.use("Agg")
#import matplotlib.pyplot as plt
#import wikipedia
from flask import Flask, jsonify, request, make_response
#from dash.dependencies import Output, Event, Input
#import dash_core_components as dcc
#import dash_html_components as html
#import plotly
import random
#import plotly.graph_objs as go
from collections import deque
import sqlite3
import pandas as pd
app=Flask(__name__)

@app.route('/all',methods=['GET'])
def all_list():
	conn = sqlite3.connect('twitter.db')
	c = conn.cursor()
	df = pd.read_sql("SELECT id,name,category FROM prime_data", conn)
	out = df.to_json(orient='records')[1:-1].replace('},{', '},{')
	print(type(out))
	resp=make_response("["+str(out)+"]")
	resp.headers['Access-Control-Allow-Origin'] = '*'
	resp.headers['Access-Control-Allow-Methods']='GET'
	resp.headers['Access-Control-Allow-Headers']='Content-Type'
	return resp
	#return out


if __name__=='__main__':
	app.run(debug=True,port=8080)