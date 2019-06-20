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
def Rectas(pantalla,pos1,pos2,posM):
    pygame.draw.line(pantalla,BLANCO,posM,pos1)
    pygame.draw.line(pantalla,BLANCO,posM,pos2)

def main():
    pygame.init()
    pantalla = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("Pygame")
    reloj=pygame.time.Clock()
    a,b=0,0
    pos1,pos2=t,t
    while True:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == MOUSEBUTTONDOWN:
                a+=1
                if a==1:
                    pos1=pygame.mouse.get_pos()
                if a==2:
                    pos2=pygame.mouse.get_pos()
                    b=1

        if b==1:
            posM=pygame.mouse.get_pos()
            Rectas(pantalla,pos1,pos2,posM)
        pygame.display.flip()
        pantalla.fill(NEGRO)
        reloj.tick(30)

if __name__ == "__main__":
    main()
