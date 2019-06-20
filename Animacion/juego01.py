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

    def update(self):
        self.rect.x+=self.vel_x
        self.rect.y+=self.vel_y

class Rival(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([20,20])
        self.image.fill(ROJO)
        self.rect=self.image.get_rect()
        self.vel_x=0

    def update(self):
        if self.rect.x>(WIDTH-self.rect.width):
            self.vel_x=-1*self.vel_x
        if self.rect.x<0:
            self.vel_x=-1*self.vel_x
        self.rect.x+=self.vel_x

def main():
    #Inicializacion
    pygame.init()
    pantalla = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("Pygame")

    jugadores=pygame.sprite.Group()
    j1=Jugador()
    j1.rect.x=100
    jugadores.add(j1)

    rivales=pygame.sprite.Group()
    for x in range(10):
        r=Rival()
        r.rect.x=random.randrange(WIDTH)
        r.rect.y=random.randrange(HEIGHT)
        r.vel_x=random.randrange(1,4)
        rivales.add(r)

    reloj=pygame.time.Clock()
    salud=200
    #Ciclo del juego
    while True:
        #Captura de eventos
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == KEYDOWN:
                if evento.key == K_UP:
                    j1.vel_y=-2
                if evento.key == K_DOWN:
                    j1.vel_y=2
                if evento.key == K_LEFT:
                    j1.vel_x=-2
                if evento.key == K_RIGHT:
                    j1.vel_x=2
            if evento.type == KEYUP:
                if evento.key == K_UP:
                    j1.vel_y=0
                if evento.key == K_DOWN:
                    j1.vel_y=0
                if evento.key == K_LEFT:
                    j1.vel_x=0
                if evento.key == K_RIGHT:
                    j1.vel_x=0

        #Logica del juego
        ls_colision=pygame.sprite.spritecollide(j1,rivales,False)
        for e in ls_colision:
            salud-=1
            print salud

        jugadores.update()
        rivales.update()
        #Refresco de Pantalla
        pantalla.fill(NEGRO)
        jugadores.draw(pantalla)
        rivales.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)


if __name__ == "__main__":
    main()
