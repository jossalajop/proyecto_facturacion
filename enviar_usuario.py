from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2 #pip install psycopg2 
import psycopg2.extras
 
app = Flask(__name__)
app.secret_key = "cairocoders-ednalan"
 
DB_HOST = "localhost"
DB_NAME = "sistemafactura"
DB_USER = "postgres"
DB_PASS = "56789"
 
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)

@app.route('/usuario')
def index():
    return render_template('registro.html')
 
@app.route('/user', methods=['POST'])
def insert_usuarios():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        id_user = request.form['id_usuario']
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        apellido1 = request.form['apellido1']
        apellido2 = request.form['apellido2']
        email = request.form['email']
        clave = request.form['clave']
        sector = request.form['sector']
        numero_casa= request.form['n_casa']
        calle_pri= request.form['calle_p']
        telefono= request.form['telefono']
        id_rol = request.form['id_rol']
        cur.execute("INSERT INTO usuario (id_usuario,nombre1,nombre2,apellido1,apellido2,email,clave,sectoru,numero_casau,calle_principalu,telefono_celularu,id_rol) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", 
        (id_user, nombre1,nombre2,apellido1,apellido2,email,clave,sector,numero_casa,calle_pri,telefono,id_rol))
        conn.commit()
        flash('finalizado')
        return 'el registro usuario se guardó'

if __name__ == '__main__':
    app.run(debug=True)



