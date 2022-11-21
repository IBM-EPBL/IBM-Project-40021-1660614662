import flask
from flask import request,render_template
from flask_cors import CORS
import joblib
import sklearn

app=flask.Flask(__name__,static_url_path='')
CORS(app)

@app.route('/',methods=['GET'])
def SendHomePage():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predictResult():
    a=float(request.form['age'])
    b=float(request.form['gender'])
    c=float(request.form['total_bilirubin'])
    d=float(request.form['alkaline_phosphotase'])
    e=float(request.form['alamine_aminotransferase'])
    f=float(request.form['aspartate_aminotransferase'])
    g=float(request.form['total_protiens'])
    h=float(request.form['albumin'])
    i=float(request.form['albumin_and_globulin_ratio'])

    x=[[a,b,c,d,e,f,g,h,i]]
    model=joblib.load('selected_model.pkl')
    result=model.predict(x)[0]
    if(result==2):
        res="Liver Disease Predicted"
    else:
        res="No Liver Disease Predicted"
    return render_template('predict.html',predict=res)

if __name__=='__main__':
    app.run()