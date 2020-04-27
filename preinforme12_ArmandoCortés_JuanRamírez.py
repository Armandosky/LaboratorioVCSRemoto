# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 11:33:24 2020

@author: ARMANDO
"""
#%% Punto 1
lista = [110.06, 107.89, 108.45, 108.49, 109.03, 110.11, 109.87, 119.38, 119.35, 116.34, 117.73, 120.01, 118.19, 119.53, 117.09, 118.03, 118.65, 117.47, 117.49, 109.65, 110.44, 110.51, 107.38, 109.26, 106.18, 109.36, 106.61, 105.16, 110.11, 105.48, 108.37, 107.59, 108.91, 108.35, 109.57, 122.56, 124.44, 125.97, 121.03, 121.22, 122.41, 122.15, 124.52, 123.35, 125.76, 121.08, 122.29, 105.42, 110.67, 107.73, 105.76, 107.85]

#%% Punto 2
mayor = lista[0]
menor = lista[0]
for i in range(0, len(lista)):
    if (lista[i] > mayor):
        mayor = lista[i]
    if (lista[i] < menor):
        menor = lista[i]

print("La diferencia entre la mayor y la menor presión promedio semanal registrada es de " + str(float(mayor)-float(menor)))

#%% Punto 3

newlista = [110.06, 107.89, 108.45, 108.49, 109.03, 110.11, 109.87, 119.38, 119.35, 116.34, 117.73, 120.01, 118.19, 119.53, 117.09, 118.03, 118.65, 117.47, 117.49, 109.65, 110.44, 110.51, 107.38, 109.26, 106.18, 109.36, 106.61, 105.16, 110.11, 105.48, 108.37, 107.59, 108.91, 108.35, 109.57, 122.56, 124.44, 125.97, 121.03, 121.22, 122.41, 122.15, 124.52, 123.35, 125.76, 121.08, 122.29, 105.42, 110.67, 107.73, 105.76, 107.85]

media = (sum(newlista))/(len(newlista))
print("La media es " + str(media))

long = len(newlista)
orden = 0
for i in range(0,long):
    for j in range(0,long-1):
        if newlista[j] > newlista[j+1]:
            orden = newlista[j]
            newlista[j] = newlista[j+1]
            newlista[j+1] = orden
      
mediana = (newlista[25]+newlista[26])/2

print("La mediana es " + str(mediana))
print("la diferencia entre la mediana y la media es de " + str(media-mediana))

#%% Punto 4

mayores = []
menores = []

for i in lista:
    if i > media:
        mayores.append(i)
    else:
        menores.append(i)
        
print("La cantidad de semanas en las que fue mayor la presión al promedio semanal fue de" , str(len(mayores)), "y la cantidad de las semanas que fueron menores al promedio fue de",str(len(menores)))

#%% Punto 6.1
V = 510
n = 17.16
R = 0.082

listaP = []
for i in newlista:
    listaP.append(i /101.325)
    
listaTemp = []

for i in listaP:
    listaTemp.append((i*V)/(n*R))
media2 = (sum(listaTemp))/(len(listaTemp))

print("La temperatura promedio semanal es de", listaTemp, "y el promedio de la temperatura promedio semanal es de", media2 )
#Se sacaron dos valores debido a que no supe a que se refería con promedio semanal, por lo que hice una lista de los promedios y un promedio total.
#%% Punto 6.2
import statistics
desviaciónStand = statistics.stdev(listaTemp)
print("La desviación estándar de las temperaturas es de",desviaciónStand)

#%% Punto 6.3
mayor = []
menor = []
for i in listaTemp:
    if i > media2:
        mayor.append(i)
    else: 
        if i < media2:
            menor.append(i)
        
print("La temperatura de las semanas en las que fue mayor la presión al promedio semanal fue de" , str(mayor), "y la temperatura de las semanas que fueron menores al promedio fue de",str(menor))

#%% Punto 6.4
desviaciónStand2 = statistics.stdev(mayor)
print("La desviación estandar de las temperaturas de las semanas en las que fue mayor la presión al promedio semanal es de",desviaciónStand2)

desviaciónStand3 = statistics.stdev(menor)
print("La desviación estandar de las temperaturas de las semanas en las que fue menor la presión al promedio semanal es de",desviaciónStand3)

#%% Punto 6.5
media3 = (desviaciónStand2+desviaciónStand3)/2
print("La media entre las semanas en las que las temperaturas fue mayor y menor al promedio es de",media3)
print("La diferencia entre la media de las desviaciones estándar del punto 6.4 y la del punto 6.2 es de", (desviaciónStand-media3))























