from distutils.log import debug
from flask import Flask, render_template
from enviar_roles import *
from app import *

@app.route('/admi')
def admi():
    return render_template('admin.html')




    
