import os # to access ports
from flask import Flask
from flask import render_template
from flask import request
from other_file import otherFileFunction

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def handle_input():
	form1 = makeUpper(request.form['inp1'])
	form2 = request.form['inp2']
	return render_template('results.html', temp1=form1, temp2=form2)



if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 3000)),debug=True)
