import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle

app = Flask(__name__, template_folder="templates")
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predicts')
def predicts():
    return render_template('predictor.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    
    if request.method == "POST":
        age = float(request.form["age"])
        trestbps = float(request.form["trestbps"])
        chol = float(request.form["chol"])
        thalach = float(request.form["thalach"])
        oldpeak = float(request.form["oldpeak"])


        sex = request.form["sex"]
        if (sex == 'sex_0'):
            sex0 = 1
            sex1 = 0

        elif (sex == 'sex_1'):
            sex0 = 0
            sex1 = 1

        else:
            sex0 = 0
            sex1 = 0


        cp = request.form["cp"]
        if (cp == 'cp_0'):
            cp0 = 1
            cp1 = 0
            cp2 = 0
            cp3 = 0

        elif (cp == 'cp_1'):
            cp0 = 0
            cp1 = 1
            cp2 = 0
            cp3 = 0

        elif (cp == 'cp_2'):
            cp0 = 0
            cp1 = 0
            cp2 = 1
            cp3 = 0

        elif (cp == 'cp_3'):
            cp0 = 0
            cp1 = 0
            cp2 = 0
            cp3 = 1

        else:
            cp0 = 0
            cp1 = 0
            cp2 = 0
            cp3 = 0

        fbs = float(request.form["fbs"])

        restecg = request.form["restecg"]
        if (restecg == 'restecg_0'):
            restecg_0 = 1
            restecg_1 = 0 
            restecg_2 = 0

        elif (restecg == 'restecg_1'):
            restecg_0 = 0
            restecg_1 = 1 
            restecg_2 = 0

        elif (restecg == 'restecg_2'):
            restecg_0 = 0
            restecg_1 = 0 
            restecg_2 = 1

        else:
            restecg_0 = 0
            restecg_1 = 0 
            restecg_2 = 0

        exang = request.form["exang"]
        if (exang == 'exang_0'):
            exang_0 = 1
            exang_1 = 0

        elif (exang == 'exang_1'):
            exang_0 = 0
            exang_1 = 1

        else:
            exang_0 = 0
            exang_1 = 0

        slope = request.form["slope"]
        if (slope == 'slope_0'):
            slope_0 = 1
            slope_1 = 0
            slope_2 = 0

        elif (slope == 'slope_1'):
            slope_0 = 0
            slope_1 = 1
            slope_2 = 0

        elif (slope == 'slope_2'):
            slope_0 = 0
            slope_1 = 0
            slope_2 = 1

        else:
            slope_0 = 0
            slope_1 = 0
            slope_2 = 0

        ca = request.form["ca"]
        if (ca == 'ca_0'):
            ca_0 = 1
            ca_1 = 0
            ca_2 = 0

        elif (ca == 'ca_1'):
            ca_0 = 0
            ca_1 = 1
            ca_2 = 0

        elif (ca == 'ca_2'):
            ca_0 = 0
            ca_1 = 0
            ca_2 = 1

        else:
            ca_0 = 0
            ca_1 = 0
            ca_2 = 0


        thal = request.form["thal"]
        if (thal == 'thal_1'):
            thal_1 = 1
            thal_2 = 0
            thal_3 = 0

        elif (thal == 'thal_2'):
            thal_1 = 0
            thal_2 = 1
            thal_3 = 0

        elif (thal == 'thal_3'):
            thal_1 = 0
            thal_2 = 0
            thal_3 = 1

        else:
            thal_1 = 0
            thal_2 = 0
            thal_3 = 0




    
        prediction = model.predict([[age,trestbps
                                    ,chol
                                    ,thalach,
                                    oldpeak,
                                    sex0,sex1,cp0,cp1,cp2,cp3,fbs,
                                    restecg_0,restecg_1,restecg_2,
                                    exang_0,exang_1,slope_0,slope_1,
                                    slope_2,ca_0,ca_1,ca_2,thal_1
                                    ,thal_2,thal_3
                                    ]])
        output=prediction
        if output == 1:
            return render_template('has_disease.html')
        else:
            return render_template('disease.html')
            
            
    return render_template('result.html')

if __name__ == "__main__":
    app.run(debug=True)
