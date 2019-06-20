#Modulos
import pygame, sys
from pygame.locals import *
from Transformaciones_lineales import *

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

def Rosa_polares(pantalla,o):
    a=100
    n=3
    r=a*math.cos(n*math.radians(o))
    x,y=Conversion_cartesianas(r,math.radians(o))
    x1,y1=Conversion_cartesianas(-r,math.radians(o))
    pygame.draw.circle(pantalla,BLANCO,Tras(t,(int(x),int(y))),1)
    pygame.draw.circle(pantalla,BLANCO,Tras(t,(int(x1),int(y1))),1)

def linea(pantalla,posxy,sigma):
    pygame.draw.line(pantalla,BLANCO,posxy[0],Rot(sigma,posxy[1]))

def main():
    pygame.init()
    pantalla = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("Pygame")
    reloj=pygame.time.Clock()
    limite=0
    posxy=[]
    a,b,c,o=0,0,0,0
    sigma=0
    while True:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == MOUSEBUTTONDOWN:
            	limite=pygame.mouse.get_pos()
                if (limite[0]>t[0] and limite[1]>t[1]):
                    if c==0:
                        posxy.append(Tras(t,TrasMouse(t,pygame.mouse.get_pos())))
                        a+=1
                    if a>=2:
                        b,c=1,1
            if c==1:            
                if evento.type == KEYDOWN:
                    sigma+=5                  
        o+=1       
        Plano_cartesiano(pantalla)
        Rosa_polares(pantalla,o)
        if b==1:
            linea(pantalla,posxy,sigma)
        pygame.display.flip()
        reloj.tick(1000)

if __name__ == "__main__":
    main()
