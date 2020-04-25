# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 20:59:26 2020

@author: Juan Camilo Ramirez
"""

##Librerias##
import numpy as np
import random as rn

#Class#
class Names_Dictionary(dict):
    def __missing__(self, key):
        return "Indefenido"
    
###Funciones###
def generador(ran = (0,0), x = (4,12)):

    logapan = np.zeros((4,12))
    
    for filas in range(0, 4):   #Filas
        for columnas in range(0, 12):    #Columnas
            logapan[filas, columnas] = rn.randint(ran[0], ran[1]) 
    return logapan
ingresos = generador((100,180)) 
egresos = generador((60,130))
print("Ingresos = " + str(ingresos)+ "\n" + "Egresos = " + str(egresos))
generador()

def imprimir(ar_2d, nm_fl=Names_Dictionary(), nm_cl=Names_Dictionary()):
    "Impresion de un array"

    ar_fil, ar_col = np.shape(ar_2d)
    
    for f in range(0,ar_fil,1): #Filas nombradass
        print("\n--"+str(nm_fl[f])+"--") 
        for c in range(0,ar_col,1): #Columnas nombradas
            print("    "+str(nm_cl[c])+": "+str(int(ar_2d[f,c]))+"M $COP")
            
def imprimir_personalizado(ar_2d,rango=(0,1), nm_fl=Names_Dictionary(), nm_cl=Names_Dictionary()):
    "Impresion de un rango de valores en un array bidimensional"
    
    #Verify
    ar_tam = np.shape(ar_2d, nm_fl=Names_Dictionary(), nm_cl=Names_Dictionary())
    if rango[0] < 0 or rango[1] > ar_tam[1]: #Tamaño de rango
        print("\n\nERROR: El rango es demasiado grande\n\n")
        return
    
    for f in range(0,ar_tam[0],1): #Filas con nombre asignado
        print("\n--"+str(nm_fl[f])+"--")
        for c in range(rango[0]-1,rango[1]+1,1): #Columnas con nombre asignado
            print("    "+str(nm_cl[c])+": "+str(int(ar_2d[f,c]))+"M $COP")
            
def promedio(br_ng, br_gr, br_gn, nm_fl=Names_Dictionary()): 
    "Calcula el promedio de una fila de valores en tres"
    
    
    #Verify
    ar_tam = np.shape(br_ng)
    if(ar_tam[0] != np.shape(br_gr)[0] or ar_tam[0] != np.shape(br_gn)[0]):
        print("\n\nERROR: Los arrays son de tamaños diferentes\n\n")
        return
    
    
    for f in range(0,ar_tam[0],1):
        print("\n--"+str(nm_fl[f])+"--")
        
        sum = 0
        for c in range(0,ar_tam[1],1):
            sum += br_ng[f,c]
        print("Ingresos: "+ str(round(sum/ar_tam[1],2))+"M $COP")
        
        sum = 0
        for c in range(0,np.shape(br_gr)[1],1):
            sum += br_gr[f,c]
        print("Egresos: "+ str(round(sum/np.shape(br_gr)[1],2))+"M $COP")
        
        sum = 0
        for c in range(0,np.shape(br_gn)[1],1):
            sum += br_gn[f,c]
        print("Ganancias: "+ str(round(sum/np.shape(br_gn)[1],2))+"M $COP")
     
def promedio_2(br_ng, br_gr, br_gn, nm_fl=Names_Dictionary()): 
    "Calcula el promedio de una fila de valores en tres array bidimensional"
    
    #Verify
    ar_tam = np.shape(br_ng)
    if(ar_tam[0] != np.shape(br_gr)[0] or ar_tam[0] != np.shape(br_gn)[0]): #Simetria
        print("\n\nERROR: Los arrays son de tamaños diferentes\n\n")
        return
    
    #Orden de variables
    np.sort(br_ng)
    np.sort(br_gr)
    np.sort(br_gn)
    
    for f in range(0,ar_tam[0],1):
        print("\n--"+str(nm_fl[f])+"--")
        
        sum = 0
        for c in range(1,ar_tam[1]-1,1):
            sum += br_ng[f,c]
        print("Ingresos: "+ str(round(sum/ar_tam[1],2))+"M $COP")
        
        sum = 0
        for c in range(1,np.shape(br_gr)[1]-1,1):
            sum += br_gr[f,c]
        print("Egresos: "+ str(round(sum/np.shape(br_gr)[1],2))+"M $COP")
        
        sum = 0
        for c in range(1,np.shape(br_gn)[1]-1,1):
            sum += br_gn[f,c]
        print("Ganancias: "+ str(round(sum/np.shape(br_gn)[1]-2,2))+"M $COP")     
     
def restador(br_mn,br_st): 
    "Resta dos arrays bidimensionales del mismo tamaño en la forma minuendo-sustraendo"
    
    #Check
    if np.shape(br_mn) != np.shape(br_st): #Simetria
        print("\n\nERROR: Los arrays son de tamaños diferentes\n\n")
        return np.zeros((2,2))
    
    #Declaración de variables
    ar_fil, ar_col = np.shape(br_mn)
    ar_resul = np.zeros((ar_fil,ar_col))
    
    for f in range(0,ar_fil,1): #Asignación de la resta de arrays ingresados al array de resultado, Filas
        for c in range(0,ar_col,1): #Columnas
            ar_resul[f,c] = int(br_mn[f,c]-br_st[f,c])            
    return ar_resul
        
def mejor_Ciudad(ar_2d, cl = -1, ps = False): 
    "Encuentra la fila de mayor valor en un array bidimensional"
    "y devuelve de manera opcional una posición para un nombre especifico"
     
    #Declaración de variables
    ar_fil, ar_col = ar_2d.shape
    pos = 0
    sl_max = 0
    
    if cl > -1 and ar_col-1 >= cl: #Bloque para la selección de columna por el usuario
        for f in range(0,ar_fil,1): #Comparación de valores en una columna
            if sl_max < ar_2d[f,cl]:
                sl_max = ar_2d[f,cl]
                pos = f
        if ps == True:
            return pos
        return sl_max
    elif cl > -1:
        print("ERROR: Tamaño de columnas invalido")
        return
    
    for f in range(0,ar_fil,1):
        sum = 0
        
        for c in range(0,ar_col,1): #Suma de valores en un fila
            sum += ar_2d[f,c]
            
        if sl_max < sum:
            sl_max = sum
            pos = f
            
    if ps == True:
        return pos
    return sl_max
    
def peor_Ciudad(ar_2d, cl = -1, ps = False): 
    "Encuentra la fila de menor valor en un array bidimensional"
    "y devuelve de manera opcional una posición para un nombre especifico"
    
    #Declaración de variables#
    ar_fil, ar_col = ar_2d.shape
    pos = 0
    sl_min = 9999
    
    if cl > -1 and ar_col-1 >= cl: #Bloque para la selección de columna por el usuario
        for f in range(0,ar_fil,1): #Comparación de valores en una columna
            if sl_min > ar_2d[f,cl]:
                sl_min = ar_2d[f,cl]
                pos = f
        if ps == True:
            return pos
        return sl_min
    elif cl > -1:
        print("ERROR: Tamaño de columnas invalido")
        return
    
    for f in range(0,ar_fil,1):
        sum = 0
        
        for c in range(0,ar_col,1): #Suma de valores en un fila
            sum += ar_2d[f,c]
            
        if sl_min > sum:
            sl_min = sum
            pos = f
            
    if ps == True:
        return pos
    return sl_min
    
def mejor_Mes(ar_2d, fl = -1, ps = False, nm_fl=Names_Dictionary(), nm_cl=Names_Dictionary()):
    "Encuentra la columna de mayor valor en un array bidimensional y devuelve un nombre especifico"
    
    #Declaración de variables#
    ar_fil, ar_col = ar_2d.shape
    sl_col = 0
    sl_max = 0
    
    if fl > -1 and ar_fil-1 >= fl: #Bloque para la selección de fila por el usuario
        for c in range(0,ar_col,1): #Comparación de valores en una fila
            if sl_max < ar_2d[fl,c]:
                sl_max = ar_2d[fl,c]
                sl_col = c
                
        if ps == True:
            return sl_col
        return sl_max
    elif fl > -1:
        print("ERROR: Tamaño de fila invalido")
        return
    
    for f in range(0,ar_fil,1):
        for c in range(0,ar_col,1): #Comparación de valores en una fila
            if sl_max < ar_2d[f,c]:
                sl_max = ar_2d[f,c]
                sl_col = c
                
        if ps == True:
            print(str(nm_fl[f])+": "+ str(nm_cl[sl_col]))
            
def peor_Mes(ar_2d, fl = -1, ps = False, nm_fl=Names_Dictionary(), nm_cl=Names_Dictionary()):
    "Encuentra la columna de menor valor en un array bidimensional y devuelve un nombre especifico"
    
    #Declaración de variables
    ar_fil, ar_col = ar_2d.shape
    sl_col = 0
    sl_max = 0
    
    if fl > -1 and ar_fil-1 >= fl: #Bloque para la selección de fila por el usuario
        for c in range(0,ar_col,1): #Comparación de valores en una fila
            if sl_max > ar_2d[fl,c]:
                sl_max = ar_2d[fl,c]
                sl_col = c
                
        if ps == True:
            return sl_col
        return sl_max
    elif fl > -1:
        print("ERROR: Tamaño de fila invalido")
        return
    
    for f in range(0,ar_fil,1):
        for c in range(0,ar_col,1): #Comparación de valores en una fila
            if sl_max > ar_2d[f,c]:
                sl_max = ar_2d[f,c]
                sl_col = c
                
        if ps == True:
            print(str(nm_fl[f])+": "+ str(nm_cl[sl_col]))

#######################Programa Principal#######################
#Declaración de variables#
ingresos =  generador((100,180),(4,12))
egresos = generador((60,130),(4,12))
ganancias = restador(ingresos,egresos)
sucursales = Names_Dictionary({0: "Buracamanga", 1: "Floridablanca", 2: "Girón", 3: "Piedecuesta"})
meses = Names_Dictionary({0: "Enero", 1: "Febrero", 2: "Marzo", 3: "Abril", 4: "Mayo", 
                          5: "Junio", 6: "Julio", 7: "Agosto", 8: "Septiembre", 9: "Octubre",
                          10: "Noviembre", 11: "Diciembre"})

print("----Ingresos por sucursal en meses----",end = "")
imprimir(ingresos, sucursales, meses)

print("\n\n----Egresos por sucursal en meses----",end = "")
imprimir(egresos, sucursales, meses)

print("\n\n----Ganancias y/o perdidas por sucursal en meses----",end = "")
imprimir(ganancias, sucursales, meses)

print(sucursales[mejor_Ciudad(ganancias, -1, True)])
print(sucursales[peor_Ciudad(ganancias, -1, True)])
mejor_Mes(ganancias, -1, True, sucursales, meses)
peor_Mes(ganancias, -1, True, sucursales, meses)

print("\n\n----Promedio #1 anual de cada sucursal----",end = "")
promedio(ingresos, egresos, ganancias, sucursales)

print("\n\n----Promedio #2 anual de cada sucursal----",end = "")
promedio_2(ingresos, egresos, ganancias, sucursales)