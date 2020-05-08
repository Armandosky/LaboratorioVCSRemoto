# -*- coding: utf-8 -*-
"""
Created on Thu May  7 19:51:33 2020

@author: Juan Camilo Ramirez
"""

import random # importación de la librería random de Python, para generar números pseudoaleatorios
import os
from colorama import *

ponderado = {'A':1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,'J':10,'Q':10,'K':10} # Diccionario de cartas
simbolos = ['(C)','(D)','(T)','(P)']
baraja = {}
cartas_jugador = []
cartas_tallador = []
ganadas = 0
perdidas = 0
x = 0

## Creación de la lista de cartas ##
ponderado = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10} # Diccionario de cartas
simbolos = ['(C)','(D)','(T)','(P)']

def combinar(A,B): # Combina el diccionario ponderado con la lista simbolos
    R = {}
    for cA in A.keys():
        for i in range(0,len(B)):
            R.setdefault(cA + B[i],A[cA])
    return R

def revolver(A):  # Devuelve la baraja revuelta
    C = []
    R = {}
    C = [key for key in A]
    random.shuffle(C,random.random)
    for i in range(0,len(C)):
        a = C[i]
        R.setdefault(a,A[a])
    return R

def sumar_cartas(B):
    j = 0
    k = 0
    for i in range(0,len(B)):
        j += baraja.get(B[i])
        if baraja.get(B[i]) == 1:
            k = 10
    if j <= 11:
        j += k
    return j

def repartir(A):
    global ganadas
    global perdidas
    global xg
    global xp
    C = []
    C = [key for key in A]
    b = 1
    if len(cartas_jugador) == 0:
        for i in range(0,2):
            cartas_jugador.append(C[i])
            print('\t ' + cartas_jugador[i]," *\n")
    if sumar_cartas(cartas_jugador) == 21:
        ganadas += 1
        print("\t FELICITACIONES, HAS GANADO ESTA PARTIDA, TIENES 21 PUNTOS!!! \n")
        b = 0
    while b == 1:
        print("\t Deseas más cartas? ")
        b = int(input('\t 1. Si     0. No, me quedo : '))
        if b == 1:
            cartas_jugador.append(C[len(cartas_jugador)])
            print('\t ' + cartas_jugador[len(cartas_jugador)-1]," *\n")
        if sumar_cartas(cartas_jugador) > 21:
            perdidas += 1
            print("\t Lo siento, has perdido, tienes más  de 21 puntos! \n")
            b = 0
        if sumar_cartas(cartas_jugador) == 21:
            ganadas += 1
            print("\t FELICITACIONES, HAS GANADO ESTA PARTIDA, TIENES 21 PUNTOS!!! \n")
            b = 0

def repartir_tallador():
    D = []
    D = [key for key in baraja]
    if xg == ganadas and xp == perdidas: # Si ya el jugador sacó 21 o se pasó, no hay necesidad de repartir al tallador
        if len(cartas_tallador) == 0:
            for i in range(0,2):
                cartas_tallador.append(D[len(cartas_jugador)+i])
                print('\t ' + cartas_tallador[i]," $\n")
            while sumar_cartas(cartas_tallador) <= sumar_cartas(cartas_jugador):
                cartas_tallador.append(D[len(cartas_jugador)+len(cartas_tallador)])
                print('\t ' + cartas_tallador[len(cartas_tallador)-1]," $\n")
                
def mostrar():
    global ganadas
    global perdidas
    suma_jugador = sumar_cartas(cartas_jugador)
    suma_tallador = sumar_cartas(cartas_tallador)
    print("\t Total Jugador: ", suma_jugador, " \n")
    print("\t Total Tallador: ", suma_tallador, " \n")
    if suma_tallador != 0:
        if suma_tallador > 21:
            ganadas += 1
            print("\t FELICITACIONES, HAS GANADO ESTA PARTIDA, el Tallador tiene más de 21 puntos!!! \n")
        else:
            if suma_jugador > suma_tallador:
                ganadas += 1
                print("\t FELICITACIONES, HAS GANADO ESTA PARTIDA, tienes más puntos que el Tallador!!! \n")
            else:
                perdidas += 1
                print("\t Lo siento, has perdido, tienes menos puntos que el Tallador! \n")
    input('\t Pulsa una tecla para continuar...')

def menu_principal():
    os.system('cls')
    print('\t 1.  NUEVO JUEGO\n')
    print('\t 2.  MOSTRAR BARAJAS\n')
    print('\t 3.  REVOLVER DE NUEVO\n')
    print('\t 4.  MOSTRAR ESTADÍSTICAS  DEL JUEGO\n')
    print('\n\t 9.  SALIR\n')
    print('\n\t Opción: ',sep='', end=" ")

while True:
    menu_principal()
    xg = ganadas
    xp = perdidas
    x = input()
    if x == '1':
        cartas_jugador = []
        cartas_tallador = []
        baraja = combinar(ponderado,simbolos)
        baraja = revolver(baraja)
        repartir(baraja)
        repartir_tallador()
        mostrar()
    elif x == '2':
        baraja = combinar(ponderado,simbolos)
        print("\t Baraja ordenada: ",len(baraja),"\n",baraja,"\n")
        input('\t Pulsa una tecla para continuar...')
    elif x == '3':
        baraja = revolver(baraja)
        print("\t Baraja revuelta: ",len(baraja),"\n",baraja,"\n")
        input('\t Pulsa una tecla para continuar...')
    elif x == '4':
        print("\t ESTADÍSTICAS DEL JUGADOR: ganadas = ",ganadas,"   perdidas = ",perdidas," \n")
        input('\t Pulsa una tecla para continuar...')
    elif x == '9':
        break
    else:
        print("")
        input("\t Opción invalida...pulsa nuevamente ")