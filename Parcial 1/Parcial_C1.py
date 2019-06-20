#Modulos
import pygame, sys, math
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
def circulo(pantalla,posxy,r=0):
    pygame.draw.circle(pantalla,BLANCO,posxy,r)

def main():
    pygame.init()
    pantalla = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("Pygame")
    reloj=pygame.time.Clock()
    a,r=0,0
    posxy=[0,0]
    while True:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == MOUSEBUTTONDOWN:
                if a==0:
                    posxy=pygame.mouse.get_pos()
                    a=1
            if evento.type == KEYDOWN:
                if evento.key == K_RIGHT:
                    r+=10
                if evento.key == K_LEFT:
                    r-=10
                    if r<0:
                        r=0

        circulo(pantalla,posxy,r)
        pygame.display.flip()
        reloj.tick(30)
        pantalla.fill(NEGRO)

if __name__ == "__main__":
    main()
