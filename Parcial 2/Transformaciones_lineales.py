import math, pygame

#t=[-20,-10]
#p=[100,30]
#e=5
#omega=90

def Tras(t,p):
	xp=t[0]+p[0]
	yp=t[1]-p[1]
	pp=[xp,yp]
	return pp

def TrasCentro(t,p):
	xp=p[0]-t[0]
	yp=p[1]-t[1]
	pp=[xp,yp]
	return pp

def TrasOrigen(t,p):
	xp=p[0]+t[0]
	yp=p[1]+t[1]
	pp=[xp,yp]
	return pp

def TrasMouse(t,p):
	x=p[0]-t[0]
	y=-p[1]+t[1]
	pp=[x,y]
	return pp

def Rot(omega,p):
	o=math.radians(omega)
	xp=(math.cos(o)*p[0])-(math.sin(o)*p[1])
	yp=(math.sin(o)*p[0])+(math.cos(o)*p[1])
	pp=[int(round(xp)),int(round(yp))]
	return pp

def Esc(e,p):
	xp=e*p[0]
	yp=e*p[1]
	pp=[int(xp),int(yp)]
	return pp

def Conversion_polares(p):
	r=math.sqrt((p[0]**2)+(p[1]**2))
	o=math.degrees(math.acos(p[0]/r))
	p=[r,o]
	return p

def Conversion_cartesianas(r,o):
	x=r*math.cos(o)
	y=r*math.sin(o)
	p=[x,y]
	return p
