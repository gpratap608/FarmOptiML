from flask import Flask,jsonify 
import numpy as np
import pandas as pd
from flask import url_for
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return "<h1> Hello, World </h1>"

@app.route("/urea/<n>/<m>")
def urea(n:int,m:float):
    dataset = pd.read_csv("dataset/Nitrogen.csv")
    X = dataset.iloc[:,1:-1].values
    y = dataset.iloc[:,-1].values
    from sklearn.ensemble import  RandomForestRegressor
    regressor = RandomForestRegressor(n_estimators=10,random_state=0)
    regressor.fit(X,y)
    pred=regressor.predict([[n,m]])
    pred=float(pred)
    predstr=str(pred)
    result={
        "prediction":predstr,
    }
    return jsonify(result)


@app.route("/phosphate/<n>/<m>")
def phosphate(n:int,m:float):
    dataset = pd.read_csv("dataset/phosphate.csv")
    X = dataset.iloc[:,1:-1].values
    y = dataset.iloc[:,-1].values
    from sklearn.ensemble import  RandomForestRegressor
    regressor = RandomForestRegressor(n_estimators=10,random_state=0)
    regressor.fit(X,y)
    pred = regressor.predict([[n,m]])
    pred=float(pred)
    predstr=str(pred)
    result={
        "prediction":predstr,
    }
    return jsonify(result)


@app.route("/potash/<n>/<m>")
def potash(n:int,m:float):
    dataset = pd.read_csv("dataset/potash.csv")
    X = dataset.iloc[:,1:-1].values
    y = dataset.iloc[:,-1].values
    from sklearn.ensemble import  RandomForestRegressor
    regressor = RandomForestRegressor(n_estimators=10,random_state=0)
    regressor.fit(X,y)
    pred = regressor.predict([[n,m]])
    pred=float(pred)
    predstr=str(pred)
    result={
        "prediction":predstr,
    }
    return jsonify(result)


with app.test_request_context():
    print(url_for('hello_world'))
    print(url_for('urea',n=11,m=9))
    print(url_for('phosphate',n=11,m=9))
    print(url_for('potash',n=11,m=9))

if (__name__ == "__main__"):
    app.run(debug = True, port = 8080, host='0.0.0.0')