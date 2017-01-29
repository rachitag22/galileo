import os
import json
from flask import Flask
from flask import Flask, request
from flask import render_template
from flask import g
from flask import redirect

app = Flask(__name__)



@app.route('/')
def main():
    return render_template('index.html')

@app.route('/results')
def results():
    return render_template('results.html')
    
@app.route('/test')
def test():
    return render_template('test.html')
    
@app.route('/compute-result',methods=['POST'])
def compute():
    jsdata = str(request.form)
    print jsdata
    print jsdata[0]['classes']
    return jsdata

@app.route('/return-result', methods=['POST'])
def return_result():
    return finalArrayData

app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))

if __name__ == '__main__':
    app.run()
    app.debug = True