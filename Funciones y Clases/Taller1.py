m1=[[6,3,4],
	[6,2,5],
	[4,5,3]]

m2=[[1,3,4],
    [4,5,5],
	[4,5,3]]

m3=[5,6,7]

m4=[7,8,9]	  


def Suma_Matrices_nxn(m1,m2):
	if(len(m1)==len(m2))&(len(m1[0])==len(m2[0])):
		nfila=len(m1)
		m3=[]
		for x in range(nfila):
			m3.append(Suma_Matrices(m1[x],m2[x]))
		print m3								
	else:
		print "No se pueden sumar las matrices"		

def Suma_Matrices(m1,m2):
	ncolumna=len(m1)
	res=[]
	for x in range(ncolumna):
		res.append(m1[x]+m2[x])
	return res

def Producto_Punto(m1,m2):
	if len(m1)==len(m2):
		productoEscalar=0
		for x in range(len(m1)):
			productoEscalar+=m1[x]*m2[x]
		return productoEscalar	
										
def Multiplicacion_Matrices(m1,m2):
	if len(m1[0])==len(m2):
		nfila=len(m1)
		a=0
		m3=[]
		for x in range(nfila):
			m3.append(Multiplicar(m1[x],m2,a))
			a+=1
		return m3
	else: 
		print "No se pueden multiplicar las matrices"	
			
def Multiplicar(m1,m2,b):
	ncolumna=len(m1)
	res=[]
	a=0
	for x in m1:
		res.append(x*m2[a][b])
		a+=1
	return res	
	
def Matriz_identidad():
	n=input("Digite el numero de la matriz identidad: ")
	m1=[]
	a=0	
	for x in range(n):
		m1.append(Crear_matriz_identidad(n,a))
		a+=1
	return m1	

def Crear_matriz_identidad(n,a):
	aux=[]
	for x in range(n):		
		if x==a:
			aux.append(1)
		else:
			aux.append(0)
	return aux

def Retorne_columna_n(m1,n):
	col=[]
	nfila=len(m1)
	for x in range(nfila):
		col.append(m1[x][n-1])
	return col
	
#Funciones Principales
#Suma_Matrices_nxn(m1,m2)
#print Producto_Punto(m3,m4)
#print Multiplicacion_Matrices(m1,m2)
#print Matriz_identidad()
#print Retorne_columna_n(m1,2)
	