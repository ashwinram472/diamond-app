from flask import Flask, url_for, render_template, request
import joblib
import numpy as np


#carat 1
#clarity [FL, IF, SI1 ,SI2, VS1, VS2, VVS1, VVS2] 8
#color [D, E, F, G, H, I, J, K] 8
#Shape [ AS, CU, EC, HS, MQ, OV, PR, PS, RA, RD] 10


app = Flask(__name__)
lmmodel = joblib.load('models/linear_model.pkl')



@app.route('/')
@app.route('/predict',methods = ['POST','GET'])
def predict():
    
    clarity = ['FL', 'IF', 'SI1' ,'SI2', 'VS1', 'VS2', 'VVS1', 'VVS2']
    color= ['D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
    shape =['Asscher', 'Cushion', 'Emerald', 'Heart', 'Marquise', 'Oval', 'Pear', 'Princess', 'Radiant', 'Round']
    if request.method == 'POST':
        x = request.form.get('Experience')
        ca = [int(request.form.get('caratselect'))]
        cl = request.form.get('clarityselect')
        co = request.form.get('colorselect')
        sh = request.form.get('shapeselect')
        claritylist = [1 if cl==x else 0 for x in clarity]
        colorlist = [1 if co==x else 0 for x in color]
        shapelist = [1 if sh==x else 0 for x in shape]
        final = ca + claritylist + colorlist + shapelist
        x = np.array([final])
        print(x)

        y_pred = lmmodel.predict(x)
        print(y_pred[0])
        return render_template('index.html', pred = y_pred[0],name = x,clarity = clarity, color= color, shape = shape)
    
    

    return render_template('index.html',clarity = clarity, color= color, shape = shape)
    

@app.route('/about')
def about():
    return render_template('about.html')


