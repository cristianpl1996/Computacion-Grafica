class Matriz:
	def __init__(self, m):
		self.m = m

	def retornar_Fila_n(self,n):
		print self.m[n-1]

	def retornar_Columna_n(self,n):
		self.res=[]
		for x in range(len(self.m)):
			self.res.append(self.m[x][n-1])
		print self.res	
	def retornar_Dimension(self):
		fila=0
		columna=0
		for x in range(len(self.m)):
			fila+=1
		for x in range(len(self.m[0])):
			columna+=1	
		print "la matriz es de dimension",fila,"x",columna	

	def aggFila(self,fila):
		self.m.append(fila)
		print self.m

	def aggColumna(self,columna):
		for x in range(len(self.m)):
			self.m[x].append(columna[x])
		print self.m				
		
m=[[1,2,3],[4,5,6],[7,8,9]]
matriz=Matriz(m)
matriz.retornar_Fila_n(2)
matriz.retornar_Columna_n(2)
matriz.retornar_Dimension()
matriz.aggColumna([1,1,1])
matriz.aggFila([1,1,1])				