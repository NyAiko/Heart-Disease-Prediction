# import pandas as pd
import numpy as np
from flask import Flask,render_template,request
import pandas as pd
import pickle
import re
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/',methods=['GET','POST'])
def predict():
    if request.method =="POST":
        file_name = 'lr_.p'
        with open(file_name,'rb') as pickled:
             data = pickle.load(pickled)
             model= data['model']
             print('model loaded')
        X = [float(x) for x in request.form.values()]
        print(X)
        X = np.array(X).reshape(1,-1)
        col = ['age','cp', 'trtbps', 'chol', 'fbs', 'restecg','thalachh','exng','oldpeak','slp','caa','thall']
        X = pd.DataFrame(data=X,columns=col)
        cat_features = ['cp','fbs','restecg','exng','slp','caa','thall']
        X[cat_features]=X[cat_features].astype('category')
        Y = int(model.predict(X))
        proba = model.predict_proba(X)
        proba = str(proba[:,1][0]*100) + ' %'
        print('prediction made')
        pred = 0
    return render_template('home.html',prediction=Y,probability=proba)
if __name__=='__main__':
    app.run()