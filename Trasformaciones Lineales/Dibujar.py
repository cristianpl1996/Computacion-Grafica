#Modulos
import pygame, sys
from pygame.locals import *

#Constantes.
WIDTH=500
HEIGHT=500
BLANCO=(255,255,255)
NEGRO=(0,0,0)
ROJO=(255,0,0)
VERDE=(0,255,0)
AZUL=(0,0,255)

#Clases y Funciones.
def Triangulo(pantalla,x=0,y=0,z=0):
	pygame.draw.line(pantalla,BLANCO,(200+x,100),(100+x,200))
	pygame.draw.line(pantalla,BLANCO,(100,200+y),(300,200+y))	
	pygame.draw.line(pantalla,BLANCO,(200+z,100),(300+z,200))
	
def main():
	pygame.init()
	pantalla = pygame.display.set_mode((WIDTH,HEIGHT))
	pygame.display.set_caption("Pygame")
	reloj=pygame.time.Clock()
	x,y,z=0,0,0
	while True:	
		for evento in pygame.event.get():
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()
			if evento.type == KEYDOWN:
				if evento.key == K_LEFT:
					x-=5
				if evento.key == K_RIGHT:
					z+=5
				if evento.key == K_DOWN:
					y+=5		
		pantalla.fill(NEGRO)			
		Triangulo(pantalla,x,y,z)		
		pygame.display.flip()
		reloj.tick(30)

if __name__ == "__main__":
    main()