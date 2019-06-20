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
t=(WIDTH/2,HEIGHT/2)

#Clases y Funciones.
def recorte(imagen,ancho,alto):
	lista=[]
	for i in range(0,8):
		lista.append([])
		for j in range(0,12):
			cuadro=imagen.subsurface(j*ancho,i*alto,ancho,alto)
			lista[i].append(cuadro)
	return lista

def main():
	pygame.init()
	pantalla = pygame.display.set_mode((WIDTH,HEIGHT))
	pygame.display.set_caption("Terreno")
	reloj=pygame.time.Clock()
	ter=pygame.image.load("imagenes/animals.png")
	lista=recorte(ter,32,32)
	i=0
	while True:
		for evento in pygame.event.get():
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()

		pantalla.fill(NEGRO)
		pantalla.blit(lista[1][i],(0,0))
		pygame.display.flip()
		reloj.tick(10)
		if i<2:
			i+=1
		else:
			i=0
if __name__ == "__main__":
    main()