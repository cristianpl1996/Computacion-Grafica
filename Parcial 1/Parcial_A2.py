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

def Triangulo(pantalla,pos1,pos2):
    pygame.draw.line(pantalla,BLANCO,t,pos1)
    pygame.draw.line(pantalla,BLANCO,pos1,pos2)
    pygame.draw.line(pantalla,BLANCO,pos2,t)
    a,b,c=0,0,0
    a=math.sqrt(((t[0]-pos1[0])**2)+((t[1]-pos1[1])**2))
    b=math.sqrt(((t[0]-pos2[0])**2)+((t[1]-pos1[1])**2))
    c=math.sqrt(((pos2[0]-pos1[0])**2)+((pos2[1]-pos1[1])**2))
    print int(a+b+c)

def main():
    pygame.init()
    pantalla = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("Pygame")
    reloj=pygame.time.Clock()
    a=0
    pos1=[]
    pos2=[]
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
                    Triangulo(pantalla,pos1,pos2)

        Plano_cartesiano(pantalla)
        pygame.display.flip()
        reloj.tick(30)

if __name__ == "__main__":
    main()
