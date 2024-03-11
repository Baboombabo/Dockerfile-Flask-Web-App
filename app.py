from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello World</h1>'

@app.route('/bye_world')
def bye_world():
    return '<h1>Bye bye World</h1>'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True) 