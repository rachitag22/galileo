import os
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
    
app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))