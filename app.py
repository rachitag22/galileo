import os
import json
from flask import Flask
from flask import Flask, request
from flask import render_template
from flask import g
from flask import redirect

app = Flask(__name__)

finalArrayData = [{
"text":"CMSC131-0508 "
"end":"2014-02-$dT16:50:00"
"id":"0"
"start":"2014-02-$dT16:00:00"
},

{
"text":"CMSC131-0508 "
"end":"2014-02-$dT16:50:00"
"id":"0"
"start":"2014-02-$dT16:00:00"
},

{
"text":"CMSC131-0508 "
"end":"2014-02-$dT16:50:00"
"id":"0"
"start":"2014-02-$dT16:00:00"
},

{
"text":"CMSC131-0508 Discussion"
"end":"2014-02-$dT15:50:00"
"id":"3"
"start":"2014-02-$dT15:00:00"
},

{
"text":"CMSC131-0508 Discussion"
"end":"2014-02-$dT15:50:00"
"id":"3"
"start":"2014-02-$dT15:00:00"
},

{
"text":"ASTR101-0108 "
"end":"2014-02-$dT12:15:00"
"id":"5"
"start":"2014-02-$dT11:00:00"
},

{
"text":"ASTR101-0108 "
"end":"2014-02-$dT12:15:00"
"id":"5"
"start":"2014-02-$dT11:00:00"
},

{
"text":"ASTR101-0108 Lab"
"end":"2014-02-$dT20:00:00"
"id":"7"
"start":"2014-02-$dT18:00:00"
},

{
"text":"ASTR101-0108 Discussion"
"end":"2014-02-$dT12:50:00"
"id":"8"
"start":"2014-02-$dT12:00:00"
},

{
"text":"CPSD100-0101 "
"end":"2014-02-$dT17:20:00"
"id":"9"
"start":"2014-02-$dT16:00:00"
},

{
"text":"MATH241-0111 "
"end":"2014-02-$dT09:50:00"
"id":"10"
"start":"2014-02-$dT09:00:00"
},

{
"text":"MATH241-0111 "
"end":"2014-02-$dT09:50:00"
"id":"10"
"start":"2014-02-$dT09:00:00"
},

{
"text":"MATH241-0111 "
"end":"2014-02-$dT09:50:00"
"id":"10"
"start":"2014-02-$dT09:00:00"
},

{
"text":"MATH241-0111 Discussion"
"end":"2014-02-$dT08:50:00"
"id":"13"
"start":"2014-02-$dT08:00:00"
},

{
"text":"MATH241-0111 Discussion"
"end":"2014-02-$dT08:50:00"
"id":"13"
"start":"2014-02-$dT08:00:00"
},

{
"text":"ENGL101S-0110 "
"end":"2014-02-$dT09:50:00"
"id":"15"
"start":"2014-02-$dT09:00:00"
},

{
"text":"ENGL101S-0110 "
"end":"2014-02-$dT09:50:00"
"id":"15"
"start":"2014-02-$dT09:00:00"
},

{
"text":"ENGL101S-0110 "
"end":"2014-02-$dT09:50:00"
"id":"15"
}]


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
    return jsdata

@app.route('/return-result', methods=['POST'])
def return_result():
    return finalArrayData

app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))

if __name__ == '__main__':
    app.run()
    app.debug = True