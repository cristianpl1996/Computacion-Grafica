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
def recta(pantalla,o,pos1,pos2):
	pygame.draw.line(pantalla,BLANCO,Tras(t,Rot(o,pos1)),Tras(t,Rot(o,pos2)))

def Plano_cartesiano(pantalla):
	pygame.draw.line(pantalla,BLANCO,(WIDTH/2,0),(WIDTH/2,HEIGHT))
	pygame.draw.line(pantalla,BLANCO,(0,HEIGHT/2),(WIDTH,HEIGHT/2))

def main():
	pygame.init()
	pantalla = pygame.display.set_mode((WIDTH,HEIGHT))
	pygame.display.set_caption("Pygame")
	reloj=pygame.time.Clock()
	o,vo,a,b=0,0,0,0
	pos1,pos2=[],[]
	while True:
		for evento in pygame.event.get():
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()
			if evento.type == MOUSEBUTTONDOWN:
				if a==0:
					pos1=TrasMouse(t,pygame.mouse.get_pos())
					a=1
				elif a==1:
					pos2=TrasMouse(t,pygame.mouse.get_pos())
					a,b=2,1
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
			recta(pantalla,o,pos1,pos2)
		Plano_cartesiano(pantalla)
		pygame.display.flip()
		reloj.tick(100)
		pantalla.fill(NEGRO)

if __name__ == "__main__":
    main()
