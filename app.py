from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def pig_latin():
	inp1 = request.form['inp1']
	inp2 = request.form['inp2']
	return "succesful post! %s : %s" % (inp1, inp2)

# @app.route('/hello/')
# @app.route('/hello/<name>')
# def hello(name=None):
#     return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
