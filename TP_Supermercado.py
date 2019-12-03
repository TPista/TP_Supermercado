import time
import os
def nuevo_producto(diccionario):
    print("Datos del producto")
    lista=[]
    codigo=int(input("Ingrese el código: "))
    lista.insert(1,input("Ingrese la descripción: "))
    lista.insert(2,int(input("Ingrese el stock: ")))
    lista.insert(3,float(input("Ingrese el precio: ")))
    lista.insert(4,input("Ingrese la fecha de vencimiento[MM/DD/AA]: "))
    lista.insert(5,input("Ingrese el tipo: "))
    lista.insert(6,int(input("El producto está en promoción? 1=si 2=no: ")))
    lista.insert(7,0)
    dic[codigo]=lista
    grabartxt(diccionario)
    return dic

def listar(diccionario):
    for i in diccionario:
        print(i,end)
        for a in diccionario[i]:
            print (a, end)
        print()

def eliminar(diccionario):
    print("Eliminar Producto")
    codigo=int(input("Ingrese el código:"))
    del diccionario[codigo]
    grabartxt(diccionario)
    return diccionario

def actualizar_stock(diccionario):
    print("Actualizar Stock")
    codigo=int(input("Ingrese el código:"))
    if codigo in diccionario:
        stock=int(input("Ingrese el nuevo stock:"))
        diccionario[codigo][1]+=stock
    else:
        print("El codigo de producto ingresado no existe.")
    grabartxt(diccionario)
    return diccionario

def actualizar_precio(diccionario):
    print("Actualizar Precio")
    codigo=int(input("Ingrese el código:"))
    if codigo in diccionario:
        porcentaje=float(input("Ingrese el porcentaje de aumento:"))
        diccionario[codigo][2]=round(diccionario[codigo][2]*(porcentaje/100+1),2)
    else:
        print("El codigo de producto ingresado no existe.")
    grabartxt(diccionario)
    return diccionario

def venta(diccionario):
        items={}
        codigo = -1
        opcion=""
        cantidad=0
        total=0
        
        print("Modulo de ventas:")
        while codigo!=0:
            codigo=int(input("Codigo: "))
            if codigo !=0:
                print(codigo, end)
                if codigo in diccionario:
                    if codigo !=0:print(diccionario[codigo][0])
                    cantidad=int(input("Cantidad: "))
                    if codigo in items:
                        cantidad+=items[codigo]
                    while cantidad>int(diccionario[codigo][1]):
                        if cantidad>int(diccionario[codigo][1]):
                            if codigo in items:
                                print("ERROR: stock disponible:",(diccionario[codigo][1]-items[codigo]))
                            else:
                                print("ERROR: stock disponible:",diccionario[codigo][1])
                            cantidad=int(input("Cantidad: "))
                            if codigo in items:
                                cantidad+=items[codigo]
                    opcion=input("Confirmar, s/n: ")
                    if opcion=="s" or opcion=="S":
                        items[codigo]=cantidad
#                os.system("cls")
            print("Modulo de ventas:")
        encabezado()
        for i in items:
            diccionario[i][1]-=items[i]
            diccionario[i][6]+=items[i]
            espaciosi=(5-len(str(i)))*" "
            espaciosd=(30-len(diccionario[i][0]))*" "
            espaciosc=(4-len(str(items[i])))*" "
            espaciosp=(10-len(str(diccionario[i][2])))*" "
            espaciost=(10-len(str(float(items[i])*diccionario[i][2])))*" "
            descripcion = diccionario[i][0] 
            print(espaciosi,i,descripcion[:30],espaciosd,espaciosc,items[i],espaciosp,diccionario[i][2],espaciost,float(items[i])*diccionario[i][2])
            total+=float(items[i])*diccionario[i][2]
            espaciosl=(47-len(str(total)))*" "
        print(espaciosl,"Total con IVA inc: ",total)
        pie()
        grabartxt(diccionario)


def leertxtenlista(dic):
    file=open('lista_de_productos.txt','r')
    lineas=file.readlines()
    for linea in lineas:
        var=linea.split(";")
        lista=[]
        codigo=int(var[0])
        lista.insert(1,var[1])
        lista.insert(2,int(var[2]))
        lista.insert(3,float(var[3]))
        lista.insert(4,var[4])
        lista.insert(5,var[5])
        lista.insert(6,int(var[6]))
        lista.insert(7,int(var[7]))
        dic[codigo]=lista
    file.close()
    return(dic)

def grabartxt(diccionario):
    file=open('lista_de_productos.txt','w')
    for i in diccionario:
        linea=str(i)
        for a in diccionario[i]:
            linea+=";" + str(a)
        file.write(linea + "\n")
    file.close()

def producto_mas_vend(diccionario):
    cantidad=0
    mayor=0
    for i in diccionario:
        if diccionario[i][6]>cantidad:
            cantidad=diccionario[i][6]
            mayor=i        
    print(str(mayor) + ": " + str(diccionario[mayor][0]))

def encabezado():
    print("SUPERMERCADO POKEMON")
    print(68* "-")
    print("CUIT Nro: 30-88743629-0")
    print("Elcano 2448 CABA")
    print("IVA RESPONSABLE INSCRIPTO")
    print("INICIO DE ACTIVIDADES 16/06/2016")
    print("CONSUMIDOR FINAL")
    file=open('factura.txt','r')
    factura=file.readlines()
    ticket=int(factura[0])
    ticket+=1
    file.close()
    file=open('factura.txt','w')
    file.write(str(ticket))
    file.close()
    print(59*" ","Nro. ",ticket)
    print(59*" ",time.strftime("%x"))
    print(59*" ",time.strftime("%X"))
    print()

def pie():
    print()
    print(29 * "-", "GRACIAS!",29 * "-")
    
opcion=""
dic={}
leertxtenlista(dic)
while opcion!=0:
#    os.system("cls")
    print("                 _Sistemas de Supermercado_ \n1)Agregar un nuevo producto \n2)Eliminar un producto \n3)Listar productos \n4)Actualizar precio \n5)Stock \n6)Realizar una venta \n7)Producto mas vendido")
    opcion=int(input("\nIngrese la opción deseada: "))
#    os.system("cls")
    
    if opcion==1:
        dic=nuevo_producto(dic)

    elif opcion==2:
        dic=eliminar(dic)
        input("Presione una tecla para continuar")
    
    elif opcion==3:
        listar(dic)
        input("Presione una tecla para continuar")

    elif opcion==4:
        actualizar_precio(dic)
        input("Presione una tecla para continuar")  

    elif opcion==5:
        actualizar_stock(dic)
        input("Presione una tecla para continuar")

    elif opcion==6:
        venta(dic)
        input("Presione una tecla para continuar")

    elif opcion==7:
        producto_mas_vend(dic)
        input("Presione una tecla para continuar")
    encabezado()

