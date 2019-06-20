#Modulos
import pygame, sys, random
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
class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([40,40])
        self.image.fill(BLANCO)
        self.rect=self.image.get_rect()
        self.vel_x=0
        self.vel_y=0
        self.muros=pygame.sprite.Group()
    def update(self):
        self.rect.x+=self.vel_x
        self.rect.y+=self.vel_y
        ls_col=pygame.sprite.spritecollide(self,self.muros,False)
        for m in ls_col:
            if self.vel_x>0:
                self.rect.right=m.rect.left
            if self.vel_x<0:
                self.rect.left=m.rect.right
            if self.vel_y<0:
                self.rect.top=m.rect.bottom
            if self.vel_y>0:
                self.rect.bottom=m.rect.top




class Muros(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([100,200])
        self.image.fill(ROJO)
        self.rect=self.image.get_rect()

def main():
    #Inicializacion
    pygame.init()
    pantalla = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("Pygame")

    muros=pygame.sprite.Group()
    m=Muros()
    m.rect.x=(WIDTH/2)-100
    m.rect.y=(HEIGHT/2)-200
    muros.add(m)

    jugadores=pygame.sprite.Group()
    j1=Jugador()
    j1.muros=muros
    jugadores.add(j1)

    reloj=pygame.time.Clock()
    #Ciclo del juego
    while True:
        #Captura de eventos
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == KEYDOWN:
                if evento.key == K_LEFT:
                    j1.vel_x=-5
                if evento.key == K_RIGHT:
                    j1.vel_x=5
                if evento.key == K_UP:
                    j1.vel_y=-5
                if evento.key == K_DOWN:
                    j1.vel_y=5
            if evento.type == KEYUP:
                if evento.key == K_LEFT:
                    j1.vel_x=0
                if evento.key == K_RIGHT:
                    j1.vel_x=0
                if evento.key == K_UP:
                    j1.vel_y=0
                if evento.key == K_DOWN:
                    j1.vel_y=0

        #Logica del juego

        #Refresco de Pantalla
        pantalla.fill(NEGRO)
        jugadores.update()
        muros.update()
        jugadores.draw(pantalla)
        muros.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)

if __name__ == "__main__":
    main()
