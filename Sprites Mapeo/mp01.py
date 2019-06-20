#Modulos
import pygame, sys, random, ConfigParser
from pygame.locals import *

#Constantes.
WIDTH=500
HEIGHT=500
BLANCO=(255,255,255)
NEGRO=(0,0,0)
ROJO=(255,0,0)
VERDE=(0,255,0)
AZUL=(0,0,255)
t=(WIDTH/2,HEIGHT/2)
interprete=ConfigParser.ConfigParser()
interprete.read('mapa1.map')

#Clases y Funciones.

def Recorte(imageSprite,corteX,corteY,cantidadX,cantidadY):
	matriz=[]
	for y in range(cantidadY):
		matriz.append([])
		for x in range(cantidadX):
			cuadro=imageSprite.subsurface((x*corteX),(y*corteY),corteX,corteY)
			matriz[y].append(cuadro)
	return matriz

def dibujarMapa(pantalla,mapa,m,corteX,corteY):
    i=0
    for a in range (len(mapa)):
        for e in mapa[a]:
            pos=interprete.get(e,'pos')
            posXY=pos.split(',')
            pantalla.blit(m[int(posXY[0])][int(posXY[1])],[i*corteX,a*corteY])
            i+=1
        i=0

def main():
	pygame.init()
	pantalla = pygame.display.set_mode((WIDTH,HEIGHT))
	pygame.display.set_caption("Mapa")

	nom_ar=interprete.get('nivel', 'fondo')
	imageSprite=pygame.image.load(nom_ar)
	imageWidth=imageSprite.get_rect()[2]
	imageHeight=imageSprite.get_rect()[3]
	cantidadX=32
	cantidadY=12
	corteX=imageWidth/cantidadX
	corteY=imageHeight/cantidadY
	m=Recorte(imageSprite,corteX,corteY,cantidadX,cantidadY)
	mapa=interprete.get('nivel', 'mapa')
	mapa=mapa.split('\n')
	
	reloj=pygame.time.Clock()
	while True:
		for evento in pygame.event.get():
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()

		pantalla.fill(NEGRO)
		dibujarMapa(pantalla,mapa,m,corteX,corteY)
		pygame.display.flip()
		reloj.tick(10)

if __name__ == "__main__":
    main()
