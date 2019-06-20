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
        self.an=40
        self.image=pygame.Surface([self.an,self.an])
        self.image.fill(BLANCO)
        self.rect=self.image.get_rect()
        self.vel_x=0

    def update(self):
        if self.rect.x<0:
            self.rect.x=0
        if self.rect.x>(WIDTH-self.rect.width):
            self.rect.x=(WIDTH-self.rect.width)
        self.rect.x+=self.vel_x

class Rival(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([20,20])
        self.image.fill(ROJO)
        self.rect=self.image.get_rect()
        self.vel_x=0
        self.temp=random.randrange(180)

    def update(self):
        if self.rect.x>(WIDTH-self.rect.width):
            self.vel_x=-1*self.vel_x
        if self.rect.x<0:
            self.vel_x=-1*self.vel_x
        self.rect.x+=self.vel_x
        self.temp-=1

class Bala(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.an,self.al=10,15
        self.image=pygame.Surface([self.an,self.al])
        self.image.fill(VERDE)
        self.rect=self.image.get_rect()
        self.vel_y=-7

    def update(self):
        self.rect.y+=self.vel_y

def main():
    #Inicializacion
    pygame.init()
    pantalla = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("Pygame")

    jugadores=pygame.sprite.Group()
    j1=Jugador()
    j1.rect.x,j1.rect.y=150,HEIGHT-j1.rect.height
    jugadores.add(j1)

    balas=pygame.sprite.Group()
    balasE=pygame.sprite.Group()

    rivales=pygame.sprite.Group()
    for x in range(15):
        r=Rival()
        r.rect.x=random.randrange(WIDTH)
        r.rect.y=random.randrange(HEIGHT-j1.rect.height)
        r.vel_x=random.randrange(1,4)
        rivales.add(r)

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
                if evento.key == K_SPACE:
                    bala=Bala()
                    bala.rect.x=j1.rect.x+((j1.rect.width/2)-(bala.rect.width/2))
                    bala.rect.y=j1.rect.y
                    balas.add(bala)
            if evento.type == KEYUP:
                if evento.key == K_LEFT:
                    j1.vel_x=0
                if evento.key == K_RIGHT:
                    j1.vel_x=0

        #Logica del juego
        for b in balas:
            b_col=pygame.sprite.spritecollide(b,rivales,True)
            for e in b_col:
                balas.remove(b)
            if b.rect.y<-10:
                balas.remove(b)

        for r in rivales:
            if r.temp<=0:
                balae=Bala()
                balae.rect.x=r.rect.x+((r.rect.width/2)-(balae.rect.width/2))
                balae.rect.y=r.rect.y
                balae.vel_y=7
                balae.image=pygame.Surface([5,10])
                balae.image.fill(AZUL)
                balasE.add(balae)
                r.temp=random.randrange(180)

        for b in balasE:
            b_col=pygame.sprite.spritecollide(b,jugadores,True)
            for e in b_col:
                balasE.remove(b)
            if b.rect.y>HEIGHT+10:
                balasE.remove(b)

        #Refresco de Pantalla
        jugadores.update()
        rivales.update()
        balas.update()
        balasE.update()
        jugadores.draw(pantalla)
        rivales.draw(pantalla)
        balas.draw(pantalla)
        balasE.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)
        pantalla.fill(NEGRO)


if __name__ == "__main__":
    main()