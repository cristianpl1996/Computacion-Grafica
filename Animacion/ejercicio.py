#Modulos	
import pygame, sys, random	
from pygame.locals import *	
from Transformaciones_lineales import *

#Constantes.	
WIDTH=600	
HEIGHT=700	
BLANCO=(255,255,255)	
NEGRO=(0,0,0)	
ROJO=(255,0,0)	
VERDE=(0,255,0)	
AZUL=(0,0,255)
AMARILLO=(246,255,51)	
t=(WIDTH/2,HEIGHT/2)

#Clases y Funciones.	
class Jugador(pygame.sprite.Sprite):	
    def __init__(self):	
        pygame.sprite.Sprite.__init__(self)	
        self.image=pygame.image.load("imagenes/nave.png")	
        self.rect=self.image.get_rect()	
        self.vel_x=0	
        #3 Vidas	
        self.salud=[10,HEIGHT-20,100,10]

    def update(self):	
        if self.rect.x<0:	
            self.rect.x=0	
        if self.rect.x>(WIDTH-self.rect.width):	
            self.rect.x=(WIDTH-self.rect.width)	
        self.rect.x+=self.vel_x	

class Rival(pygame.sprite.Sprite):	
    def __init__(self):	
        pygame.sprite.Sprite.__init__(self)	
        self.image=pygame.image.load("imagenes/naveE.png")	
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
        self.image=pygame.image.load("imagenes/misil.png")	
        self.rect=self.image.get_rect()	
        self.vel_y=-7

    def update(self):	
        self.rect.y+=self.vel_y

def main():	
    #Inicializacion	
    pygame.init()	
    pantalla = pygame.display.set_mode((WIDTH,HEIGHT))	
    pygame.display.set_caption("Game Nave")	
    fondo=pygame.image.load("imagenes/fondo.png")	
    informacion=(0,HEIGHT-40,WIDTH,40)	
    vida=VERDE			
    a=0
    eDestruidos=0
    termino=True	
    #Jugador	
    jugadores=pygame.sprite.Group()	
    j1=Jugador()	
    j1.rect.x=0
    j1.rect.y=HEIGHT-j1.rect.height-40	
    jugadores.add(j1)	
    #Balas y balas enemigas	
    balas=pygame.sprite.Group()	
    balasE=pygame.sprite.Group()	
    #Rivales	
    rivales=pygame.sprite.Group()	
    for x in range(15):	
        r=Rival()	
        r.rect.x=random.randrange(WIDTH-64)	
        r.rect.y=random.randrange(HEIGHT-j1.rect.height-110)	
        r.vel_x=random.randrange(1,4)	
        rivales.add(r)

    reloj=pygame.time.Clock()	
    #Ciclo del juego	
    while termino:	
        #Captura de eventos	
        for evento in pygame.event.get():	
            if evento.type == QUIT:	
                pygame.quit()	
                sys.exit()	
            if evento.type == KEYDOWN:	
                if evento.key == K_LEFT:	
                    j1.vel_x=-10	
                if evento.key == K_RIGHT:	
                    j1.vel_x=10       	
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
                eDestruidos+=1     	
            if b.rect.y<-10:	
                balas.remove(b)

        for r in rivales:	
            if r.temp<=0:	
                balae=Bala()	
                balae.rect.x=r.rect.x+((r.rect.width/2)-(balae.rect.width/2))	
                balae.rect.y=r.rect.y	
                balae.vel_y=7	
                balae.image=pygame.image.load("imagenes/misilE.png") 	
                balasE.add(balae)	
                r.temp=random.randrange(180)

        for b in balasE:	
            b_col=pygame.sprite.spritecollide(b,jugadores,False)	
            for e in b_col:	
                balasE.remove(b)	
                if a==0:	
                    j1.salud[2]=66	
                    vida=AMARILLO	
                if a==1:	
                    j1.salud[2]=33	
                    vida=ROJO	
                if a==2:	
                    j1.salud[2]=0	
                    vida=NEGRO	   	
                a+=1            	
            if b.rect.y>HEIGHT-90:	
                balasE.remove(b)

        if j1.salud[2]==0:   
            jugadores.remove(j1)
            termino=False            
        if eDestruidos==15:   
            termino=False        
        	
        #Refresco de Pantalla	
        pygame.draw.rect(pantalla,NEGRO,informacion)	
        pygame.draw.rect(pantalla,vida,j1.salud)	
        jugadores.update()	
        rivales.update()	
        balas.update()	
        balasE.update()	
        jugadores.draw(pantalla)	
        rivales.draw(pantalla)	
        balas.draw(pantalla)	
        balasE.draw(pantalla)	
        pygame.display.flip()	
        pantalla.fill(NEGRO)	
        pantalla.blit(fondo,(0,0))	
        reloj.tick(50)

    if eDestruidos==15:	
        print "Winner Jugador"	
    else:	
        print "Losser Jugador"	
    pygame.time.wait(200)		    	

if __name__ == "__main__":	
    main() 