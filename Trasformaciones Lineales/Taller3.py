# Modulos
import pygame, sys
from pygame.locals import *
from Transformaciones_lineales_taller1 import *

# Constantes.
WIDTH=400
HEIGHT=400

# Clases y Funciones.
def main():
	pygame.init()
	pantalla = pygame.display.set_mode((WIDTH,HEIGHT))
	pygame.display.set_caption("Pygame")
	pygame.draw.line(pantalla,(255,255,255),(100,0),(0,100))
	pygame.draw.line(pantalla,(255,255,255),(0,100),(100,100))
	pygame.draw.line(pantalla,(255,255,255),(100,0),(100,100))

	while True:	
		for evento in pygame.event.get():
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()
			if evento.type == KEYDOWN:
				pantalla.fill((0,0,0))
				t=(100,100)
				pygame.draw.line(pantalla,(255,255,255),Tras(t,(100,0)),Tras(t,(0,100)))
				pygame.draw.line(pantalla,(255,255,255),Tras(t,(0,100)),Tras(t,(100,100)))
				pygame.draw.line(pantalla,(255,255,255),Tras(t,(100,0)),Tras(t,(100,100)))
				omega=90
				pygame.draw.line(pantalla,(255,255,255),Tras(t,Rot(omega,(100,0))),Tras(t,Rot(omega,(0,100))))
				pygame.draw.line(pantalla,(255,255,255),Tras(t,Rot(omega,(0,100))),Tras(t,Rot(omega,(100,100))))
				pygame.draw.line(pantalla,(255,255,255),Tras(t,Rot(omega,(100,0))),Tras(t,Rot(omega,(100,100))))
				e=2
				pygame.draw.line(pantalla,(255,255,255),Esc(e,(100,0)),Esc(e,(0,100)))
				pygame.draw.line(pantalla,(255,255,255),Esc(e,(0,100)),Esc(e,(100,100)))
				pygame.draw.line(pantalla,(255,255,255),Esc(e,(100,0)),Esc(e,(100,100)))

		pygame.display.flip()

if __name__ == "__main__":
    main()
