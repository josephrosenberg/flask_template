import os # to run to the port
from flask import Flask
from flask import render_template
from flask import request
from upper import makeUpper

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def pig_latin():
	form1 = makeUpper(request.form['inp1'])
	form2 = request.form['inp2']
	return render_template('results.html', temp1=form1, temp2=form2)

# @app.route('/hello/')
# @app.route('/hello/<name>')
# def hello(name=None):
#     return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 3000)),debug=True)
