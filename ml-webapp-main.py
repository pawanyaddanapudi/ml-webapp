#pip install numpy
#pip install pandas
#pip install xlrd
#pip install sklearn
import numpy as OSnp
import pandas as OSpd
import os
from sklearn import linear_model as OSlm
from sklearn.metrics import mean_squared_error
from flask import Flask, render_template, request
from pandas.io.json import json_normalize

flaskapp = Flask(__name__)

# Run or refresh model
def model(x):
    if x == 1:
        OSdata = OSpd.read_excel(
            'basket_ball.xlsx')
    else:
        OSdata = OSpd.read_excel(
            'basket_ball2.xlsx')

    OSdataX = OSdata[['height_ft', 'weight_pd', 'successfieldgoals%', 'successfreethrows%']]
    OSdataY = OSdata['avg_points']

    global OSLM
    OSLM = OSlm.LinearRegression()
    global bbmodel
    OSLM.fit(OSdataX, OSdataY)
    bbpred = OSLM.predict(OSdataX)
    rmse = mean_squared_error(OSdataY, bbpred)
    return OSLM, rmse


# Predict from the model build
@flaskapp.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        input_values = request.form

    inputX = OSpd.DataFrame(json_normalize(input_values))
    input = inputX[['height_ft', 'weight_pd', 'successfieldgoals%', 'successfreethrows%']]
    predval = OSLM.predict(input)
    input['predval'] = predval
    input.columns = ['Height (feet)', 'Weight (pounds)', 'Field Success (%)', 'Free Success (%)', 'Predicted Avg Score']
    return render_template('predict.html', tables=[input.to_html()], titles=input.columns.values)


# Home page that renders for every web call
@flaskapp.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 9000))
    global OSLM, Error
    OSLM, Error = model(1)
    flaskapp.run(host='0.0.0.0', port=port, debug=True)

