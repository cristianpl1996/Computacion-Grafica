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
	
def Cardioide_polares(pantalla,o):
    a=50
    b=100
    r=a+(b*math.cos(math.radians(o)))
    x,y=Conversion_cartesianas(r,math.radians(o))
    pygame.draw.circle(pantalla,BLANCO,Tras(t,(int(x),int(y))),1)  
   
def Figura_pitagorica(pantalla,n,vertice):
    r=40
    o=360/n
    c=o
    polygon=[]
    for a in range(n):
        posxy=Conversion_cartesianas(r,math.radians(o))
        polygon.append(Tras((vertice[0]-40,vertice[1]),posxy))
        o+=c   
    pygame.draw.polygon(pantalla,BLANCO,polygon)            

def main():
    pygame.init()
    pantalla = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("Pygame")
    reloj=pygame.time.Clock()
    posxy=0
    bandera=True
    o=0
    while True:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == MOUSEBUTTONDOWN:
				if bandera:
					posxy=pygame.mouse.get_pos()
					if (posxy[0]>t[0] and posxy[1]<t[1]):
					    vertice=Tras(t,TrasMouse(t,posxy))
					    Figura_pitagorica(pantalla,6,vertice)
					    bandera=False
        o+=1       
        Plano_cartesiano(pantalla)
        Cardioide_polares(pantalla,o)
        pygame.display.flip()
        reloj.tick(60)

if __name__ == "__main__":
    main()
