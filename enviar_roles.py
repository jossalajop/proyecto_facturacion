from flask import Flask, render_template, request,flash
import psycopg2 #pip install psycopg2 
import psycopg2.extras
 
from app import *
 
DB_HOST = "localhost"
DB_NAME = "sistemafactura"
DB_USER = "postgres"
DB_PASS = "56789"
 
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)

@app.route('/roles')
def roles():
    return render_template('roles.html')
 
@app.route('/rol', methods=['POST'])
def insert_roles():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        id_rol = request.form['id_rol']
        nombrer = request.form['nombrer']
        cur.execute("INSERT INTO roles (id_rol, nombrer) VALUES (%s,%s)", (id_rol, nombrer))
        conn.commit()
        return render_template('admin.html')


