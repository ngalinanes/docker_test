# flask_web/app.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
           return 'Estas corriendo una app de Flask en un container de Docker'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

