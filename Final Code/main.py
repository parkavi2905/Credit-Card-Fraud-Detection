from flask import Flask, render_template, request
import joblib
import pandas as pd
import random

app = Flask(__name__)

df = pd.read_csv('final.csv')
df2 = pd.read_csv('onlinepayment.csv')

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/validate', methods = ['POST','GET'])
def validate():
    if request.method == 'POST':
        if request.form.get('uname') == 'abc' and request.form.get('upass') == '123':
            return render_template('index.html')
        else:
            return render_template('login.html', msg = 'Invalid')

@app.route('/model')
def model():
    model = joblib.load('model.pkl')


@app.route('/predict', methods = ['POST','GET'])
def predict():
    if request.method == 'POST':
        card_no = int(request.form.get('card_no'))
        df1 = df.loc[df['Card No'] == card_no]
        location = df1['Location']
        for i in location:
            location = i
        classes = df1['Class']
        value = ['Fraud','Non Fraud']
        c = 0
        for i in classes:
            c = i
        c = value[c]

        return render_template('result.html',card = card_no, cla = c, las = (random.randint(20,50))*100, loc = location)

if __name__ == '__main__':
    app.run(debug = True,port=2587)
