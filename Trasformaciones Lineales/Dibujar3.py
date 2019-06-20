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
def recta(pantalla):
	#Ejemplo 1: 300x+300y=3000
	pygame.draw.line(pantalla,ROJO,Tras(t,(0,300)),Tras(t,(300,0)))
	#Ejemplo 2: 300y=3000+300x
	pygame.draw.line(pantalla,VERDE,Tras(t,(0,300)),Tras(t,(-300,0)))
	
def Plano_cartesiano(pantalla):
	pygame.draw.line(pantalla,BLANCO,(WIDTH/2,0),(WIDTH/2,HEIGHT))
	pygame.draw.line(pantalla,BLANCO,(0,HEIGHT/2),(WIDTH,HEIGHT/2))

def Triangulo(pantalla,x=0):
	#Triangulo sin traslacion
	pygame.draw.line(pantalla,BLANCO,(100-x,0),(0-x,100))
	pygame.draw.line(pantalla,BLANCO,(0,100+x),(200,100+x))	
	pygame.draw.line(pantalla,BLANCO,(100+x,0),(200+x,100))
	#Triangulo con traslacion
	pygame.draw.line(pantalla,BLANCO,Tras(t,(20,20-x)),Tras(t,(220,20-x)))
	pygame.draw.line(pantalla,BLANCO,Tras(t,(20-x,20)),Tras(t,(120-x,120)))
	pygame.draw.line(pantalla,BLANCO,Tras(t,(220+x,20)),Tras(t,(120+x,120)))
	
def main():
	pygame.init()
	pantalla = pygame.display.set_mode((WIDTH,HEIGHT))
	pygame.display.set_caption("Pygame")
	reloj=pygame.time.Clock()
	vx,x=0,0
	while True:	
		for evento in pygame.event.get():
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()
			if evento.type == KEYDOWN:
				if evento.key == K_UP:
					vx=5
				if evento.key == K_DOWN:
					vx,x=0,0
									
		pantalla.fill(NEGRO)			
		x+=vx
		#Llamado de las funciones	
		Triangulo(pantalla,x)
		recta(pantalla)
		Plano_cartesiano(pantalla)		
		pygame.display.flip()
		reloj.tick(30)

if __name__ == "__main__":
    main()