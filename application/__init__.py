from flask import Flask, url_for, render_template, request, redirect
import joblib
import numpy as np


#carat 1
#clarity [FL, IF, SI1 ,SI2, VS1, VS2, VVS1, VVS2] 8
#color [D, E, F, G, H, I, J, K] 8
#Shape [ AS, CU, EC, HS, MQ, OV, PR, PS, RA, RD] 10


app = Flask(__name__)
lmmodel = joblib.load('models/linear_model.pkl')
rfmodel = joblib.load('models/rf_model.pkl')
xgmodel = joblib.load('models/xg_model.pkl')




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
        # ca = [int(request.form.get('caratselect'))]
        ca = [3]
        cl = request.form.get('clarityselect')
        co = request.form.get('colorselect')
        sh = request.form.get('shapeselect')
        claritylist = [1 if cl==x else 0 for x in clarity]
        colorlist = [1 if co==x else 0 for x in color]
        shapelist = [1 if sh==x else 0 for x in shape]
        final = ca + claritylist + colorlist + shapelist
        x = np.array([final])
        print(x)

        lm_pred = lmmodel.predict(x)[0][0]
        rf_pred = round(rfmodel.predict(x)[0],2)
        xg_pred = round(xgmodel.predict(x)[0],2)
        max_pred = max(lm_pred,rf_pred,xg_pred)
        min_pred = min(lm_pred,rf_pred,xg_pred)
        return render_template('index.html', lm_pred = lm_pred,rf_pred=rf_pred,xg_pred=xg_pred,max_pred = max_pred,min_pred = min_pred,name = x,clarity = clarity, color= color, shape = shape)
    
    

    return render_template('index.html',clarity = clarity, color= color, shape = shape)
    

@app.route('/about')
def about():
    return render_template('about.html')


