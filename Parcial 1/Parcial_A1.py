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
def Plano_cartesiano(pantalla,x=0,y=0):
    pygame.draw.line(pantalla,BLANCO,((WIDTH/2)+x,0+y),((WIDTH/2)+x,HEIGHT+y))
    pygame.draw.line(pantalla,BLANCO,(0+x,(HEIGHT/2)+y),(WIDTH+x,(HEIGHT/2)+y))

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
            if evento.type == MOUSEBUTTONDOWN:
                Plano_cartesiano(pantalla)
                z=1
            if evento.type == KEYDOWN:
                if evento.key == K_LEFT:
                    x-=5
                if evento.key == K_RIGHT:
                    x+=5
                if evento.key == K_DOWN:
                    y+=5
                if evento.key == K_UP:
                    y-=5
        pantalla.fill(NEGRO)
        if z==1:
            Plano_cartesiano(pantalla,x,y)
        pygame.display.flip()
        reloj.tick(30)

if __name__ == "__main__":
    main()
