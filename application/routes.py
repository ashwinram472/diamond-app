from flask import Flask, url_for, render_template, request, redirect, jsonify
from application import app
import joblib
import numpy as np

from application.data import data
from application.model import Diamonds
import pandas as pd
from application.data import data



# Loading models
# Linear model
lmmodel = joblib.load('models/linear_model.pkl')
# Random Forest model
rfmodel = joblib.load('models/rf_model.pkl')
# XG Boost model
xgmodel = joblib.load('models/xg_model.pkl')

def one_hot(p,li):
    return [1 if p==x else 0 for x in li]

@app.route('/api', methods=['GET'])
def api():

    return jsonify(Diamonds.objects.count())


@app.route('/')
def index():
    return redirect(url_for('predict'))
    
@app.route('/predict',methods = ['POST','GET'])
def predict():
    
    clarity = ['FL', 'IF', 'SI1' ,'SI2', 'VS1', 'VS2', 'VVS1', 'VVS2']
    color= ['D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
    shape =['Asscher', 'Cushion', 'Emerald', 'Heart', 'Marquise', 'Oval', 'Pear', 'Princess', 'Radiant', 'Round']
    if request.method == 'POST':
        x = request.form.get('Experience')
        ca = [float(request.form.get('caratselect'))] #carat
        cl = request.form.get('clarityselect') #clarity
        co = request.form.get('colorselect') #color
        sh = request.form.get('shapeselect') #shape
        claritylist = one_hot(cl,clarity)
        colorlist = one_hot(co,color)
        shapelist = one_hot(sh,shape)
        final = ca + claritylist + colorlist + shapelist
        x = np.array([final])
        print(x)

        lm_pred = lmmodel.predict(x)[0][0]
        rf_pred = round(rfmodel.predict(x)[0],2)
        xg_pred = round(xgmodel.predict(x)[0],2)

        
        max_pred = max(lm_pred,rf_pred,xg_pred)
        min_pred = max(0,min(lm_pred,rf_pred,xg_pred))

        return render_template('index.html', lm_pred = lm_pred,rf_pred=rf_pred,xg_pred=xg_pred,max_pred = max_pred,min_pred = min_pred,name = x,clarity = clarity, color= color, shape = shape)
    
    

    return render_template('index.html',clarity = clarity, color= color, shape = shape)
    

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/carat')
def carat():
    return render_template('carat.html')
    

@app.route('/charts')
def charts():
    diamonds = data()
    dataframe= pd.json_normalize(diamonds)
    print(dataframe.shape)

    return render_template('charts.html')


