#Modulos
import pygame, sys
from pygame.locals import *
from Transformaciones_lineales import *

#Constantes.
WIDTH=500
HEIGHT=500
BLANCO=(255,255,255)
NEGRO=(0,0,0)
ROJO=(255,0,0)
VERDE=(0,255,0)
AZUL=(0,0,255)
t=(WIDTH/2,HEIGHT/2)

#Clases y Funciones.
def Plano_cartesiano(pantalla):
	pygame.draw.line(pantalla,BLANCO,(WIDTH/2,0),(WIDTH/2,HEIGHT))
	pygame.draw.line(pantalla,BLANCO,(0,HEIGHT/2),(WIDTH,HEIGHT/2))

def Polygon(pantalla,posxy,o):
	pygame.draw.polygon(pantalla,BLANCO,Rot_pointlist(posxy,o))

def Rot_pointlist(posxy,o):
	polygon=[]
	for x in posxy:
		polygon.append(Tras(t,Rot(o,x)))
	return polygon			

def main():
	pygame.init()
	pantalla = pygame.display.set_mode((WIDTH,HEIGHT))
	pygame.display.set_caption("Pygame")
	reloj=pygame.time.Clock()
	o,vo,a,b,c=0,0,0,0,0
	posxy=[]
	while True:
		for evento in pygame.event.get():
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()
			if evento.type == MOUSEBUTTONDOWN:
				#Click izquierdo
				if evento.button == 1:
					posxy.append(TrasMouse(t,pygame.mouse.get_pos()))
					a+=1
				#Click derecho y el poligono debe tener al menos 3 lados	
				if evento.button == 3:
					if a>=3:
						b,c=1,1
			if c==1:					
				if evento.type == KEYDOWN:
					if evento.key == K_UP:
						vo=2	
					if evento.key == K_DOWN:
						vo=-2	
				if evento.type == KEYUP:
					if evento.key == K_UP:
						vo=0	
					if evento.key == K_DOWN:
						vo=0

		o+=vo			
		if b==1:
			Polygon(pantalla,posxy,o)
		Plano_cartesiano(pantalla)
		pygame.display.flip()
		reloj.tick(100)
		pantalla.fill(NEGRO)

if __name__ == "__main__":
    main()