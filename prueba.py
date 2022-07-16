import psycopg2  
try: 
 
 conexion=psycopg2.connect( 
     host='localhost', 
        user='postgres', 
        password='56789', 
        database='sistemafactura' 
) 
 print('conexion exit ') 
 cursor=conexion.cursor() 
 cursor.execute("SELECT version()") 
 row=cursor.fetchone() 
 print(row) 
 cursor.execute("SELECT * FROM usuario") 
 row=cursor.fetchall() 
 for row in row: 
    print(row) 
except Exception as ex:  
    print(ex) 
finally: 
    conexion.close() 
    print("conexion dos")



