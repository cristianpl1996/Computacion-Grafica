#Modulos

import pygame, sys, random, ConfigParser, json
from pygame.locals import *

with open ('mapa2.json') as archivo:
    base = json.load(archivo)

#Constantes.
WIDTH=1000
HEIGHT=640
BLANCO=(255,255,255)
NEGRO=(0,0,0)
ROJO=(255,0,0)
VERDE=(0,255,0)
AZUL=(0,0,255)
t=(WIDTH/2,HEIGHT/2)
mapa = base['layers'][1]['data']
mapeo=[]

for j in range(10):
	fila=[]
	for i in range(35):
		fila.append(mapa[i+(j*35)])
	
	mapeo.append(fila)

print mapeo
#Clases y Funciones.

def Recorte(imageSprite,corteX,corteY,cantidadX,cantidadY):
	matriz=[]
	for y in range(cantidadY):
		matriz.append([])
		for x in range(cantidadX):
			cuadro=imageSprite.subsurface((x*corteX),(y*corteY),corteX,corteY)
			matriz[y].append(cuadro)
	return matriz

def dibujarMapa(pantalla,m,corteX,corteY):
	i=0
	for a in range (len(mapeo)):
		for e in mapeo[a]:
			c=e-1
			if (not(c <= 0)):
				posXY=[(c/4),(c%4)]			
				pantalla.blit(m[int(posXY[0])][int(posXY[1])],[i*corteX,a*corteY])
			i+=1
		i=0

def main():
	pygame.init()
	pantalla = pygame.display.set_mode((WIDTH,HEIGHT))
	pygame.display.set_caption("Mapa")
	imageFondo=pygame.image.load("mapa2.png")
	imageSprite=pygame.image.load("ts64a.png")
	imageWidth=imageSprite.get_rect()[2]
	imageHeight=imageSprite.get_rect()[3]
	cantidadX=4
	cantidadY=2
	corteX=imageWidth/cantidadX
	corteY=imageHeight/cantidadY
	m=Recorte(imageSprite,corteX,corteY,cantidadX,cantidadY)

	reloj=pygame.time.Clock()
	while True:
		for evento in pygame.event.get():
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()

		pantalla.blit(imageFondo,(0,0))
		dibujarMapa(pantalla,m,corteX,corteY)
		pygame.display.flip()
		reloj.tick(10)

if __name__ == "__main__":
    main()