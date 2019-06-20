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
def Fondo(x,y,lim_izq,lim_der,lim_arr,lim_aba):
	x1,y1=pygame.mouse.get_pos()
	if x1<lim_izq:
		x+=5
	if x1>lim_der:
		x-=5
	if y1<lim_arr:
		y+=5
	if y1>lim_aba:
		y-=5
	return x,y    

def Limites_pantalla(x,y,ancho,alto):
    if y<0:
        y=0
    if y>(HEIGHT-alto):
        y=(HEIGHT-alto)
    if x<0:
        x=0
    if x>(WIDTH-ancho):
        x=(WIDTH-ancho)
    return x,y     

def Scrolling(x,y):
    if x>WIDTH:
        x=-64
    if x<-64:
        x=WIDTH
    if y>HEIGHT:
        y=-64
    if y<-64:
        y=HEIGHT
    return x,y 

def main():
    pygame.init()
    pantalla = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("Pygame")
    reloj=pygame.time.Clock()
    nave=pygame.image.load("nave.png")
    propiedades_nave= nave.get_rect()
    ancho=propiedades_nave[2]
    alto=propiedades_nave[3]
    fondo=pygame.image.load("fondo.png")
    x,y=0,0
    vx,vy=0,0
    lim_izq=50
    lim_der=WIDTH-50
    lim_arr=50
    lim_aba=HEIGHT-50
    while True:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == KEYDOWN:
                if evento.key == K_UP:
                    vy=-1
                if evento.key == K_DOWN:
                    vy=1
                if evento.key == K_LEFT:
                    vx=-1
                if evento.key == K_RIGHT:
                    vx=1
            if evento.type == KEYUP:
                if evento.key == K_UP:
                    vy=0
                if evento.key == K_DOWN:
                    vy=0
                if evento.key == K_LEFT:
                    vx=0
                if evento.key == K_RIGHT:
                    vx=0                 
        #x,y=Scrolling(x,y)
        #x,y=Limites_pantalla(x,y,ancho,alto)
        #x,y=Fondo(x,y,lim_izq,lim_der,lim_arr,lim_aba)
        #NOTA:Para mover el fondo poner una tupla (x,y) en vez de (0,0) y poner en comentarios el blit de la nave.
        pantalla.blit(fondo,(0,0))
        pantalla.blit(nave,(x,y))
        x+=vx
        y+=vy  
        pygame.display.flip()
        pantalla.fill(NEGRO)
        reloj.tick(60)

if __name__ == "__main__":
    main()
