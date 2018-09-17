import MySQLdb
import time
fecha = time.strftime("%y/%m/%d")#esta nos dara la fecha siempre actualizada sincronisada con la PC

db = MySQLdb.connect(host="localhost",    # tu host, usualmente localhost
                     user="root",         # tu usuario
                     passwd="123456",     # tu password
                     db="heladeriaf")      # el nombre de la base de datos


cur = db.cursor()
def saborescono():#Funcion De sabores conos
        cur.execute("SELECT * FROM sabor")

        for sabor in cur.fetchall():
           codigo=sabor[0]
           nombre=sabor[1]
           print "ID: ", codigo, "\t|", "sabor: ", nombre 
    
def menu():#Funcion De MENU
        cur.execute("SELECT * FROM helado")

        for helado in cur.fetchall():
           codigo=helado[0]
           nombre=helado[1]
           precio=helado[2]
           print "ID: ", codigo,"\t|", "Nombre: ", nombre,"", "\t|Precio: $",precio
def jefe():#Funcion De JEFE
        print "Bienvenido Jefe"
        while True:
                jefe=int(input("""
1-)Ver Inventario
2-)Ver Ventas
3-)Ver Promedio de venta y total de productos
4-)Vender Helados
> """))
                
                if jefe==1:#si el jefe da la opcion i vera el inventario
                        cur.execute("SELECT * FROM inventario")
                        for hela in cur.fetchall():
                                nombre=hela[1]
                                cantidad_max=hela[2]
                                cantidad_dis=hela[3]
                                print "Nombre:  ", nombre, "\t|", "Cantidad Maxima: ", cantidad_max, "\t|", "Cantidad Disponible", cantidad_dis
                        print "------------------------------------------"
                        pregunta=input("Jefe desea actualizar el inventario? 1-)si y 2-)no: ")#pregunta para alctualizar el inventario en mysql
                        if pregunta== 1:
                                sql=("UPDATE inventario SET cantidad_dis=200")
                                cur.execute(sql)
                                db.commit()
                                pre=input("Decea hacer algo mas jefe? 1-)si y 2-)no: ")
                                if pre==1:
                                        print " "

                                else:
                                        print "Hazta luego jefe"
                                        break

                        else:
                                pre=input("Quiere usar alguna otra funion? 1-)si y 2-)no: ")
                                if pre==1:
                                        print' '
                                else:
                                        print "bye"
                                        break 
                               
                                        
                if jefe==2:#Funcion de jefe para ver la venta
                        cur.execute("SELECT * FROM venta")
                        for fact in cur.fetchall():
                                idi=fact[0]
                                codigo_hela=fact[1]
                                fechao=fact[2]
                                CantidadCom=fact[3]
                                sabor=fact[4]
                                print "ID de venta: ", idi, "\t|", "Codigo De helado: ", codigo_hela, "\t|",  "Fecha de venta: ", fechao, "\t|", "Cantidad de helados: ", CantidadCom, "\t|", "Sabor del helado", sabor
                        pre=input("Quiere usar alguna otra funion? 1-)si y 2-): ")
                        if pre==1:
                                print' '
                        else:
                                print "bye"
                                break  

                if jefe==3:#Funcion de promedio de la ventas
                        cur.execute("SELECT * FROM promedio")
                        for fac in cur.fetchall():
                                print "Promedio: ", fac[0]
                                print "Cantidad: ", fac[1]
                        prea=input("Desea hacer algo mas? 1-)si y 2-)no ")
                        if prea==1:
                                print " "

                        else:
                                print "Hazta luego jefe"
                                break
                if jefe==4:#Funcion de veder
                        print "Funcion vender"
                        usuario()

def usuario():
        IDL=input("Ingrese su id: ")
        if IDL==0:
                jefe()
        else:
                print "Bienvenido/a"
                # Mostramos el menu
                while True:
                        menu()
                        print"------------------------------------------"
                        saborescono()
                        # solicituamos una opción al usuario
                        Codigo = input("ingrese el id de el helado: ")
                        codigo_sabor = input("ingrese el codigo del sabor: ")
                        total = input("ingrese la cantidad de helado que quiere: ")
                        sql="INSERT INTO VENTA(Codigo, fecha, total, Codigo_sabor) VALUES (%d, '%s', %d, %d)" % (Codigo, fecha, total, codigo_sabor)  
                        cur.execute(sql)
                        db.commit()
                        prr=("Select * from venta")
                        cur.execute(prr)
                        for cod in cur.fetchall():
                                codigo1=cod[0]
                        sql=("Select precio, nombre from helado where codigo=%d") % (Codigo)
                        cur.execute(sql)
                        for hel in cur.fetchall(): #todo el procedimiento de facturacion
                                precio=hel[0]
                                nombre=hel[1]
                                sqlk=("select nombre from sabor where codigo=%d") % (codigo_sabor)
                                cur.execute(sqlk)
                                for hel in cur.fetchall():
                                        sabor=hel[0]
                                        print """--**********YOUNG FAST**********--
***** \t ID Factura\t        ---> %d \t *****
***** \t Nombre del helado\t---> %s \t *****
***** \t Sabor del helado\t---> %s \t*****
***** \t Total a pagar\t        ---> %d \t*****
--*******************************--""" % (codigo1, nombre, sabor, precio*total)
                        pre=raw_input("Desea algo mas?: ")
                        if pre=="si":
                                print "Que deseas"
                        else:
                                
                                print "Gracias por preferirnos"
                                break
        
registrar=input("""Bienvendio a la heladeria young fast
esta es la mejor heladeria del mundo
\t1-)Iniciar sesion
--> """)
if registrar==1:#Funcion para vender 
        usuario()
        

        
