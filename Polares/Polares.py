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

def Polares(pantalla,o):
	r1,o1=Conversion_polares((100,30))
	r2,o2=Conversion_polares((150,20))
	pygame.draw.line(pantalla,BLANCO,Tras(t,(0,0)),Tras(t,Rot(o1+o,(r1,0))))
	pygame.draw.line(pantalla,BLANCO,Tras(t,(0,0)),Tras(t,Rot(o2+o,(r2,0))))

def Mouse_polares():
	posxy=TrasMouse(t,pygame.mouse.get_pos())
	r,o=Conversion_polares(posxy)
	print "r:",int(r),"o:",int(o)	

def Rosa_polares(pantalla,o):
    a=100
    n=3
    r=a*math.cos(n*math.radians(o))
    x,y=Conversion_cartesianas(r,math.radians(o))
    pygame.draw.circle(pantalla,BLANCO,Tras(t,(int(x),int(y))),1)
    pygame.draw.line(pantalla,BLANCO,Tras(t,(0,0)),Tras(t,(x,y)))
   
def Figura_pitagorica(pantalla,n):
    r=100
    o=360/n
    c=o
    polygon=[]
    for a in range(n):
        posxy=Conversion_cartesianas(r,math.radians(o))
        polygon.append(Tras(t,posxy))
        o+=c   
    pygame.draw.polygon(pantalla,BLANCO,polygon)            

def main():
    pygame.init()
    pantalla = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("Pygame")
    reloj=pygame.time.Clock()
    posxy=0
    o=0
    while True:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == MOUSEBUTTONDOWN:
            	Mouse_polares()       
        o+=1       
        Plano_cartesiano(pantalla)
        #Figura_pitagorica(pantalla,5)
        #Rosa_polares(pantalla,o)
        #Polares(pantalla,o)
        pygame.display.flip()
        reloj.tick(1000)

if __name__ == "__main__":
    main()
