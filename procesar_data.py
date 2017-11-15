import pyodbc
import pandas as pd

# Conexión a LZ, trae datos.
def get_datos(cedula):
    connec = pyodbc.connect("DSN=impala-prod", autocommit=True)
    query = ("select * from proceso.info_clientes_reto where Cedula = "+ str(cedula) +";")
    df = pd.read_sql(query,connec).astype('str')
    connec.close()
    return df

#Función que elimina espacios y separa
def sep_strings(name):
    #datosname = df[name].unique()
    winsize = 2
    valueVect = []
    #name = datosname.replace(' ','').lower()
    name = name.replace(' ','').lower()
    for i in range(0,len(name)-winsize+1):
        #para cada ventana en el texto se saca el valor total de la ventana y se va guardando en un array
        ventana = name[i:winsize+i]
        valueVect.append(ventana)
    return valueVect

def compara_texto(usuario, lista_name):
    lista_index = []
    for i in lista_name:
        if i in usuario:
            lista_index.extend((usuario.index(i), usuario.index(i) + 1))
    return lista_index

def comparafecha(fecha):
    lista_index =[]
    arr = []
    arr.append(fecha[2:4])
    arr.append(fecha[6:] + fecha[4:6])
    arr.append(fecha[4:6] + fecha[6:])
    arr.append(fecha[:4])
    for x in arr:
        if x in usuario:
            lista_index.extend(list(range(usuario.index(x), usuario.index(x) + len(x) - 1)))
    return lista_index

def compara_num(numero, usuario):
    arrced = []
    lista_index = []
    arrced.append(numero[:])
    arrced.append(numero[4:])
    arrced.append(numero[:4])
    
    for x in arrced:
        if x in usuario:
            lista_index.extend(list(range(usuario.index(x), usuario.index(x) + len(x) - 1)))
    return lista_index

def comparar(nombre,usuario, fecha, cedula, telefono):
    lista_index = []
    lista_name = sep_strings(nombre)
    lista_index.extend(compara_texto(usuario, lista_name))
    lista_index.extend(comparafecha(fecha))
    lista_index.extend(compara_num(cedula, usuario))
    lista_index.extend(compara_num(telefono, usuario))
    resultado = len(set(lista_index))/len(usuario)
    print(set(lista_index))
    return resultado


#Datos funcion
nombre = 'javier'
usuario = 'marco1234'
lista_name = sep_strings(nombre)
telefono = '1234567'
cedula = '103002350321'
fecha = '20131001'

#Llamado función
comparar(nombre,usuario, fecha, cedula, telefono)
