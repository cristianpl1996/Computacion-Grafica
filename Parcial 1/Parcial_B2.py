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
t=(WIDTH/2,HEIGHT/2)

#Clases y Funciones.
def Plano_cartesiano(pantalla):
    pygame.draw.line(pantalla,BLANCO,(WIDTH/2,0),(WIDTH/2,HEIGHT))
    pygame.draw.line(pantalla,BLANCO,(0,HEIGHT/2),(WIDTH,HEIGHT/2))

def Recta(pantalla,pos1,pos2,b=0):
    distancia1,distancia2=0,0
    if b==0:
        pygame.draw.line(pantalla,BLANCO,pos1,pos2)
        distancia1=math.sqrt((pos1[1]-(HEIGHT/2))**2)
        distancia2=math.sqrt((pos2[1]-(HEIGHT/2))**2)
        print distancia1,distancia2
    if b==1:
        print "hola"
        pygame.draw.line(pantalla,BLANCO,(pos1[0],pos1[1]+(HEIGHT/2)+distancia1),(pos2[0],pos2[1]+(HEIGHT/2)+distancia2))

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
                    Recta(pantalla,pos1,pos2)
            if evento.type == KEYDOWN:
                if evento.key == K_SPACE:
                    b=1
                    Recta(pantalla,pos1,pos2,b)

        Plano_cartesiano(pantalla)
        pygame.display.flip()
        reloj.tick(30)

if __name__ == "__main__":
    main()
