from distutils.log import debug
from flask import Flask, render_template
from enviar_roles import *


app = Flask(__name__)


@app.route('/admi')
def index():
    return render_template('admin.html')


if __name__ == '__main__':
    app.run(debug=True)
    
