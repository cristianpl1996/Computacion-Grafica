#Modulos
import pygame, sys
from pygame.locals import *
from Transformaciones_lineales_taller1 import *

#Constantes.
WIDTH=700
HEIGHT=700
BLANCO=(255,255,255)
NEGRO=(0,0,0)
ROJO=(255,0,0)
VERDE=(0,255,0)
AZUL=(0,0,255)
t=(WIDTH/2,HEIGHT/2)

#Clases y Funciones.
def circulos(pantalla,x=0,y=0):
	pygame.draw.circle(pantalla,BLANCO,Tras(t,(50+x,50+x)),10)
	pygame.draw.circle(pantalla,BLANCO,Tras(t,(-50-x,50+x)),10)
	pygame.draw.circle(pantalla,BLANCO,Tras(t,(-50-x,-50-x)),10)
	pygame.draw.circle(pantalla,BLANCO,Tras(t,(50+x,-50-x)),10)
	
def Plano_cartesiano(pantalla):
	pygame.draw.line(pantalla,BLANCO,(WIDTH/2,0),(WIDTH/2,HEIGHT))
	pygame.draw.line(pantalla,BLANCO,(0,HEIGHT/2),(WIDTH,HEIGHT/2))

def main():
	pygame.init()
	pantalla = pygame.display.set_mode((WIDTH,HEIGHT))
	pygame.display.set_caption("Pygame")
	reloj=pygame.time.Clock()
	x,y=0,0
	vx,vy=0,0
	while True:	
		for evento in pygame.event.get():
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()
			if evento.type == KEYDOWN:
				if evento.key == K_UP:
					vx=5
				if evento.key == K_DOWN:
					x,vx=0,0
													
		pantalla.fill(NEGRO)			
		x+=vx
		y+=vy
		#Llamado de las funciones	
		Plano_cartesiano(pantalla)
		circulos(pantalla,x,y)		
		pygame.display.flip()
		reloj.tick(30)

if __name__ == "__main__":
    main()