from flask import Flask, request, render_template, session, redirect
import pickle
import pandas as pd
model =  pickle.load(open('Churnfinalized_model(2).sav', 'rb'))

X = pd.read_csv('input_download.csv').iloc[:, 1:]

result = model.predict(X)
X['Churn'] = result
#print(X)
#print(len(result))

app = Flask(__name__)

@app.route('/', methods=("POST", "GET"))
def churn():
    return  X.to_html(header="true", table_id="table")

if (__name__ == '__main__'):
    app.run(port = 5500)