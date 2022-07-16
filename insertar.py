import psycopg2  

conexion=psycopg2.connect( 
        host='localhost', 
        user='postgres', 
        password='56789', 
        database='sistemafactura' 
) 
cursor=conexion.cursor()
sql='INSERT INTO usuario (id_usuario,nombre1,nombre2,apellido1,apellido2,email,clave,sectoru,numero_casau,calle_principalu,telefono_celularu,id_rol) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

id_usuario=input('ingrese el id')
nombre1=input('ingrese el primer nombre:')
nombre2=input('ingrese el segundo nombre:')
apellido1=input('ingrese el primer apellido:')
apellido2=input('ingrese el segundo apellido:')
email=input('ingrese su email:')
clave=input('ingrese su clave:')
sector=input('sector:')
numero_casa=input('numero de casa:')
calle_principal=input('calle principal:')
telefono_celular=input('telefono celular:')
id_rol=input('id rol:')

datos=(id_usuario,nombre1,nombre2,apellido1,apellido2,email,clave,sector,numero_casa,calle_principal,telefono_celular,id_rol)

cursor.execute(sql,datos)

conexion.commit()

registro=cursor.rowcount

print('registro ingresado: {registro}')

cursor.close()
conexion.close()