# -*- coding: utf-8 -*-
"""
Created on Fri May  1 06:47:49 2020

@author: ARMANDO
"""

bayas = {"Arándano":45, 
         "Frambuesa":67,
         "Fresa":78,
         "Grosella roja":36,
         "Zarzamora":45}

citricos = {"Limon":87,
            "Mandarina":56,
            "Naranja":43,
            "Pomelo":24}

fruta_dulce = {"Cereza":18,
               "Ciruela":34,
               "Manzana":67,
               "Melocoton":24,
               "Pera":57}

##Lista##
print("\n--Bayas--\n",bayas)
print("--Citricos--\n",citricos)
print("--Frutas dulces--\n",fruta_dulce)

##Cantidad de Frutas##

sum1 = sum(bayas[fruta] for fruta in bayas)
print("\n\nHay",sum1,"kg de bayas") 

sum2 = sum(citricos[fruta] for fruta in citricos)
print("Hay",sum2,"kg de citricos") 

sum3 = sum(fruta_dulce[fruta] for fruta in fruta_dulce)
print("Hay",sum3,"kg de Frutos dulces") 

##Total de frutas##
total = sum1+sum2+sum3
print("\nHay",total,"kg de fruta en la bodega")

##Ganancia por Manzana##
print("\n\nLa ganancia total por las manzanas es de:",
      fruta_dulce["Manzana"]*500, "$COP")

##Baya abundante##
baya_mayor = max(bayas.keys())
 
print("\nLa baya que mas abunda es:",baya_mayor,"con",bayas.get(baya_mayor))
