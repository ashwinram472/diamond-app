import joblib
import numpy as np

lmmodel = joblib.load('models/linear_model.pkl')
xgmodel = joblib.load('models/xgboost.pkl')

x_test = np.array([[0.98,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 1.0,
 0.0,
 0.0,
 0.0,
 1.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 1.0]])


y_pred = lmmodel.predict(x_test)
y_pred1 = xgmodel.predict(x_test)
print("The prediced price  for linear model is :" , y_pred)
print("The prediced price  for xgboost model is :" , y_pred1)

