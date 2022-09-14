import numpy as np
from flask import Flask,render_template,url_for,request
import pandas as pd 
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
# from sklearn.externals import joblib
import predictor as predict

# load the model from disk
# filename = 'nlp_model.pkl'
# clf = pickle.load(open(filename, 'rb'))
# cv=pickle.load(open('tranform.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/nextpage')
def print():
	return render_template('result.html')
# @app.route('/submit', methods=['POST','GET'])
# def submit():
# 	if(request.method==['post']):
# 		text=request.form['Symptoms']
# 		disease_predicted=predict(text)
# 		predictlist=list(disease_predicted)
# 		return render_template('result.html', disease = predictlist[0])

if __name__ == '__main__':
	app.run(debug=True)