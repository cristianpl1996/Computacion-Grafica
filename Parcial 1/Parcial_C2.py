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

def Recta(pantalla,posxy):
    pygame.draw.line(pantalla,BLANCO,t,posxy)
    m=(posxy[1]-t[1])/(posxy[0]-t[0])
    angulo=math.atan(m)
    print math.degrees(angulo)+90

def main():
    pygame.init()
    pantalla = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("Pygame")
    reloj=pygame.time.Clock()
    a=0
    posxy=t
    while True:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == MOUSEBUTTONDOWN:
                if a==0:
                    posxy=pygame.mouse.get_pos()
                    a=1
                    Recta(pantalla,posxy)

        Plano_cartesiano(pantalla)
        pygame.display.flip()
        reloj.tick(30)

if __name__ == "__main__":
	main()
