from flask import Flask, render_template, request,flash, session
import psycopg2 #pip install psycopg2 
import psycopg2.extras
 
from app import *

DB_HOST = "localhost"
DB_NAME = "sistemafactura"
DB_USER = "postgres"
DB_PASS = "56789"
 
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)



@app.route('/log')
def login():
    return render_template('login.html')

@app.route('/valid', methods=['POST'])
def valid_user():
    cursor=conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        email = request.form['email']
        passw = request.form['pass']
        id = request.form['id']
    
        cursor.execute('SELECT * FROM usuario WHERE email = %s AND clave =%s AND id_rol=%s', (email, passw,id))
        acount = cursor.fetchone()
       
    if acount:
      
        return render_template('admin.html')
    else:
        return render_template('login.html')
    

    
       
        
