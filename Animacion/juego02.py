#Modulos
import pygame, sys, random
from pygame.locals import *
from Transformaciones_lineales import *
r=lambda: random.randrange(0,255)

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
        self.an=10
        self.image=pygame.Surface([self.an,self.an])
        self.image.fill((r(),r(),r()))
        self.rect=self.image.get_rect()

    def update(self):
        self.image=pygame.Surface([self.an,self.an])
       	self.image.fill((r(),r(),r()))
        self.rect=self.image.get_rect()
        self.rect.x,self.rect.y=pygame.mouse.get_pos()

class Rivales(pygame.sprite.Sprite):
    def __init__(self):
        self.vel_x=0
        self.vel_y=0

    def update(self):
        if self.rect.x>(WIDTH-self.rect.width):
            self.vel_x=-1*self.vel_x
        if self.rect.x<0:
            self.vel_x=-1*self.vel_x
        if self.rect.y>(HEIGHT-self.rect.height):
            self.vel_y=-1*self.vel_y
        if self.rect.y<0:
            self.vel_y=-1*self.vel_y
        self.rect.x+=self.vel_x     
        self.rect.y+=self.vel_y    

class Rival(Rivales):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([20,20])
        self.image.fill(VERDE)
        self.rect=self.image.get_rect()

class Rival2(Rivales):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([25,25])
        self.image.fill(ROJO)
        self.rect=self.image.get_rect()            
	
def main():
    #Inicializacion
    pygame.init()
    pantalla = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("Pygame")
    reloj=pygame.time.Clock()
    jugadores=pygame.sprite.Group()
    j1=Jugador()
    jugadores.add(j1)
    rivales=pygame.sprite.Group()
    for x in range(10):
        r,r2=Rival(),Rival2()
        r.rect.x,r2.rect.x=random.randrange(WIDTH),random.randrange(WIDTH)
        r.rect.y,r2.rect.y=random.randrange(HEIGHT),random.randrange(WIDTH)
        r.vel_x,r.vel_y=random.randrange(1,4),random.randrange(1,4)
        r2.vel_x,r2.vel_y=random.randrange(1,4),random.randrange(1,4)
        rivales.add(r,r2)
    #Ciclo del juego
    while True:
        #Captura de eventos
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()

        #Logica del juego
        ls_colision=pygame.sprite.spritecollide(j1,rivales,True)
        for x in ls_colision:
            if isinstance(x,Rival):
            	j1.an+=5
            else:
            	if j1.an<5:
            		j1.an=0
            	else:	
            		j1.an-=5	

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
