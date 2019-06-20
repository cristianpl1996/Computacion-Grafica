#Modulos
import pygame, sys, random
from pygame.locals import *
from Transformaciones_lineales import *

#Constantes.
WIDTH=1000
HEIGHT=540
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
        #self.image=pygame.image.load("imagenes/nave.png")
        self.nave1=pygame.image.load("imagenes/nave1.png")
        self.nave2=pygame.image.load("imagenes/nave2.png")
        self.nave3=pygame.image.load("imagenes/nave3.png")
        self.nave4=pygame.image.load("imagenes/nave4.png")
        self.imagenes=[self.nave1,self.nave2,self.nave3,self.nave4]
        self.n=2
        self.image=self.imagenes[self.n]
        self.rect=self.image.get_rect()
        self.vel_x=0
        self.vel_y=0
        self.muros=pygame.sprite.Group()
        self.salud=300

    def limitesJugador(self):
        if self.rect.x<0:
            self.rect.x=0
        if self.rect.x>(WIDTH-self.rect.width):
            self.rect.x=(WIDTH-self.rect.width)
        if self.rect.y<0:
            self.rect.y=0
        if self.rect.y>(HEIGHT-40-self.rect.height):
            self.rect.y=(HEIGHT-40-self.rect.height)

    def limitesMuros(self):
        ls_col=pygame.sprite.spritecollide(self,self.muros,False)
        for m in ls_col:
            if self.vel_x>0:
                self.rect.right=m.rect.left
            if self.vel_x<0:
                self.rect.left=m.rect.right
            if self.vel_y>0:
                self.rect.bottom=m.rect.top       
            if self.vel_y<0:  
                self.rect.top=m.rect.bottom       

    def update(self):
        self.rect.x+=self.vel_x
        self.rect.y+=self.vel_y
        self.limitesJugador()
        self.limitesMuros()
        self.image=self.imagenes[self.n]                      

class Muros(pygame.sprite.Sprite):
    def __init__(self,w,h):
        pygame.sprite.Sprite.__init__(self)
        self.w=w
        self.h=h
        self.image=pygame.Surface([self.w,self.h])
        self.image.fill(ROJO)
        self.rect=self.image.get_rect()

class Salud(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([300,10])
        self.color=VERDE
        self.image.fill(self.color)
        self.rect=self.image.get_rect()
        self.rect.x=20
        self.rect.y=HEIGHT-25

    def actualizar(self,salud):
        self.image=pygame.Surface([salud,10])
        self.image.fill(self.color)
                   
class Rival(pygame.sprite.Sprite):
    def __init__(self,m3,m5,bandera): 
        pygame.sprite.Sprite.__init__(self) 
        self.image=pygame.image.load("imagenes/naveE1.png")
        self.rect=self.image.get_rect()
        self.vel_x=0
        self.vel_y=0   
        self.temp=random.randrange(5)
        self.m3=m3
        self.m5=m5
        self.bandera=bandera

    def update(self):
    	if self.bandera==0:
    		if self.rect.right>(self.m3.rect.left):
    			self.vel_x=-1*self.vel_x
    		if self.rect.x<0:
    			self.vel_x=-1*self.vel_x
    	if self.bandera==1:
    		if self.rect.y>(HEIGHT-40-self.rect.height):
    			self.vel_y=-1*self.vel_y
    		if self.rect.y<0:
    			self.vel_y=-1*self.vel_y
    	if self.bandera==2:
    		if self.rect.left<(self.m5.rect.right):
    			self.vel_x=-1*self.vel_x
    		if self.rect.x>WIDTH-self.rect.width:
    			self.vel_x=-1*self.vel_x			
        self.rect.x+=self.vel_x
        self.rect.y+=self.vel_y
        self.temp-=1

class Bala(pygame.sprite.Sprite):
    def __init__(self): 
        pygame.sprite.Sprite.__init__(self) 
        self.image=pygame.image.load("imagenes/misil.png")  
        self.rect=self.image.get_rect() 
        self.vel_y=0
        self.vel_x=0

    def update(self):   
        self.rect.y+=self.vel_y
        self.rect.x+=self.vel_x          

def main():
    #Inicializacion
    pygame.init()
    pantalla = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("Pygame")
    reloj=pygame.time.Clock()
    fondo=pygame.image.load("imagenes/fondo.png")
    meta=pygame.image.load("imagenes/meta.png")
    pygame.mixer.music.load("imagenes/fondo.wav")
    pygame.mixer.music.play()
    sonido=pygame.mixer.Sound("imagenes/sonido.wav")
    informacion=(0,HEIGHT-40,WIDTH,40)
    termino=True
    #Muros
    muros=pygame.sprite.Group()
    m1=Muros(200,70)
    m1.rect.x=0
    m1.rect.y=200
    m1.image=pygame.image.load("imagenes/m1.png")
    m2=Muros(70,200)
    m2.rect.x=350
    m2.rect.y=0
    m2.image=pygame.image.load("imagenes/m2.png")
    m3=Muros(70,50)
    m3.rect.x=350
    m3.rect.y=(HEIGHT-m3.rect.height-80)
    m3.image=pygame.image.load("imagenes/m3.png")
    m4=Muros(70,100)
    m4.rect.x=550
    m4.rect.y=0
    m4.image=pygame.image.load("imagenes/m4.png")
    m5=Muros(70,350)
    m5.rect.x=550
    m5.rect.y=150
    m5.image=pygame.image.load("imagenes/m5.png")
    m6=Muros(200,70)
    m6.rect.x=750
    m6.rect.y=300
    m6.image=pygame.image.load("imagenes/m6.png")
    muros.add(m1,m2,m3,m4,m5,m6)
    #Jugador
    jugadores=pygame.sprite.Group()
    j1=Jugador()
    j1.muros=muros
    jugadores.add(j1)
    #Rivales
    rivales=pygame.sprite.Group()
    r1=Rival(m3,m5,0)
    r1.rect.x=0
    r1.rect.y=HEIGHT-r1.rect.height-80
    r1.vel_x=5 
    r2=Rival(m3,m5,1)
    r2.rect.x=470
    r2.rect.y=0
    r2.vel_y=5
    r2.image=pygame.image.load("imagenes/naveE2.png")
    r3=Rival(m3,m5,2)
    r3.rect.x=700
    r3.rect.y=HEIGHT-r3.rect.height-80
    r3.vel_x=5
    rivales.add(r1,r2,r3)
    #Salud del jugador
    saludJ=pygame.sprite.Group()
    saludj1=Salud()
    saludJ.add(saludj1)
    #Balas enemigas
    balasE=pygame.sprite.Group()
    #Ciclo del juego
    while termino:
        #Captura de eventos
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == KEYDOWN:
                if evento.key == K_LEFT:
                    j1.vel_x=-5
                    j1.n=3
                if evento.key == K_RIGHT:
                    j1.vel_x=5
                    j1.n=1
                if evento.key == K_UP:
                    j1.vel_y=-5
                    j1.n=0
                if evento.key == K_DOWN:
                    j1.vel_y=5
                    j1.n=2
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
        if r1.rect.left>m1.rect.right:
            if r1.temp<=0:   
                balae=Bala()    
                balae.rect.x=r1.rect.x+((r1.rect.width/2)-(balae.rect.width/2))   
                balae.rect.y=r1.rect.y   
                balae.vel_y=-7       
                balasE.add(balae)   
                r1.temp=random.randrange(10)

        if (r2.rect.top>m2.rect.bottom) and (r2.rect.bottom<m3.rect.top):       
            if r2.temp<=0:   
                balae=Bala()    
                balae.rect.x=r2.rect.x+((r1.rect.width/2)-(balae.rect.width/2))   
                balae.rect.y=r2.rect.y   
                balae.vel_x=-7
                balae.image=pygame.image.load("imagenes/misil2.png")       
                balasE.add(balae)   
                r2.temp=random.randrange(10)

        if r3.rect.right<m6.rect.left:
            if r3.temp<=0:   
                balae=Bala()    
                balae.rect.x=r3.rect.x+((r1.rect.width/2)-(balae.rect.width/2))   
                balae.rect.y=r3.rect.y   
                balae.vel_y=-7       
                balasE.add(balae)   
                r3.temp=random.randrange(10)

        for b in balasE:    
            b_col=pygame.sprite.spritecollide(b,jugadores,False)
            b_col2=pygame.sprite.spritecollide(b,muros,False)    
            for e in b_col: 
                balasE.remove(b)
                j1.salud-=50
                sonido.play()
                if j1.salud<200 and j1.salud>100:
                    saludj1.color=AMARILLO
                if j1.salud<100:
                    saludj1.color=ROJO
                saludj1.actualizar(j1.salud)
            for a in b_col2:
                balasE.remove(b)                                                                                        
            if b.rect.y<-10 or b.rect.x<-10:  
                balasE.remove(b)

        if j1.salud==0:
            jugadores.remove(j1)
            saludJ.remove(saludj1)
            termino=False

        if (j1.rect.x>WIDTH-50) and (j1.rect.bottom<50):
            termino=False                             

        #Refresco de Pantalla
        pygame.draw.rect(pantalla,NEGRO,informacion) 
        muros.update()
        jugadores.update()
        rivales.update()
        balasE.update()
        saludJ.update() 
        muros.draw(pantalla)
        jugadores.draw(pantalla)
        rivales.draw(pantalla)
        balasE.draw(pantalla)
        saludJ.draw(pantalla)
        pygame.display.flip()
        pantalla.fill(NEGRO)
        pantalla.blit(fondo,(0,0))
        pantalla.blit(meta,(WIDTH-50,0))  
        reloj.tick(60)

    if j1.salud>0:
        print "Winner Jugador"  
    else:   
        print "Losser Jugador"  
    pygame.time.wait(200)    

if __name__ == "__main__":
    main()