import numpy as np
from flask import Flask, redirect,render_template,url_for,request
import pandas as pd 
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
# from sklearn.externals import joblib
import predictor as predict
import preprocessor as preproc
pp = preproc.preprocessor()
model = pickle.load(open('model.pkl','rb'))
# load the model from disk
# filename = 'nlp_model.pkl'
# clf = pickle.load(open(filename, 'rb'))
# cv=pickle.load(open('tranform.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
	if request.method == 'POST':
		text = request.form.get('symptoms')
		text = pp.forward(text)
		my_prediction = model.predict(text)
		my_prediction = np.array2string(my_prediction)
	return redirect(url_for("predict",prediction = my_prediction))

@app.route('/predict/<prediction>')
def predict(prediction):
	return render_template('result.html',prediction = prediction)

if __name__ == '__main__':
	app.run(debug=True)