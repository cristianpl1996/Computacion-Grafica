# Modulos
import pygame, sys
from pygame.locals import *

# Constantes.
WIDTH=400
HEIGHT=400

# Clases y Funciones.
def main():
	pygame.init()
	pantalla = pygame.display.set_mode((WIDTH,HEIGHT))
	pygame.display.set_caption("Pygame")
	pygame.draw.line(pantalla,(255,255,255),(100,0),(0,100))
	pygame.draw.line(pantalla,(255,255,255),(0,100),(200,100))
	pygame.draw.line(pantalla,(255,255,255),(100,0),(200,100))
	pygame.draw.rect(pantalla,(255,255,255),(150,150,50,50))
	pygame.draw.polygon(pantalla,(255,255,255),((300,300),(350,300),(350,350),(300,350),(400,350),(350,400)))
	pygame.draw.circle(pantalla,(255,255,255),(70,300),50)
	pygame.draw.ellipse(pantalla,(255,255,255),(150,300,100,50))
	while True:	
		for evento in pygame.event.get():
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()

		pygame.display.flip()

if __name__ == "__main__":
    main()
