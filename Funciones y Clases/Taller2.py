from Funciones_taller1 import *
import random, math

def Numero_aleatorios():
	m1=[]
	for x in range(5):
		m1.append(random.randrange(50))	
	print m1

def Triangulo_rectangulo():
	cateto1=input("digite cateto 1: ")
	cateto2=input("digite cateto 2: ")
	alpha=math.degrees(math.atan(cateto1/cateto2))
	betha=math.degrees(math.atan(cateto2/cateto1))
	hipotenusa= math.hypot(cateto1, cateto2)
	print alpha
	print betha
	print hipotenusa

m=[[1,2,3],[4,5,6],[7,8,9]]

def multiplicar_matriz_por_identidad(m1):
	m2=[[1,0,0],[0,1,0],[0,0,1]]
	print Multiplicacion_Matrices(m1,m2)

def crear_mostrar():
	m1=Matriz_identidad()
	n=input("Digite numero de la columna: ")
	print Retorne_columna_n(m1,n)

#Funciones Principales
#Numero_aleatorios()
#Triangulo_rectangulo()
#multiplicar_matriz_por_identidad(m)
#crear_mostrar()