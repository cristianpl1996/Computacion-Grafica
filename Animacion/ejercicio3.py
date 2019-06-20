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
        self.vidas=2

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
    def __init__(self): 
        pygame.sprite.Sprite.__init__(self) 
        self.image=pygame.image.load("imagenes/naveE3.png")
        self.rect=self.image.get_rect()
        self.vel_x=0
        self.vel_y=0
        self.m1=0
        self.m3=0
        self.m5=0
        self.n=0
        self.bandera=0
        self.radius=100   
        self.temp=random.randrange(50)

    def update(self):
        if self.bandera==1:
            if self.rect.bottom>self.m3.rect.bottom:
                self.vel_y=-1*self.vel_y
                self.image=pygame.image.load("imagenes/naveE1.png")
                self.n=1
            if self.rect.y<0:
                self.vel_y=-1*self.vel_y
                self.image=pygame.image.load("imagenes/naveE3.png")
                self.n=2
        if self.bandera==2:
            if self.rect.right>self.m5.rect.left:
                self.vel_x=-1*self.vel_x
                self.image=pygame.image.load("imagenes/naveE2.png")
                self.n=1
            if self.rect.left<self.m1.rect.right:
                self.vel_x=-1*self.vel_x
                self.image=pygame.image.load("imagenes/naveE4.png")
                self.n=2            
        if self.bandera==3:
            if self.rect.y>(HEIGHT-40-self.rect.height):
                self.vel_y=-1*self.vel_y
                self.image=pygame.image.load("imagenes/naveE1.png")
                self.n=1
            if self.rect.y<0:
                self.vel_y=-1*self.vel_y
                self.image=pygame.image.load("imagenes/naveE3.png")
                self.n=2
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

class Boton(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.boton1=pygame.image.load("imagenes/startR.png")
        self.boton2=pygame.image.load("imagenes/startV.png")
        self.imagenes=[self.boton1,self.boton2]
        self.n=0
        self.image=self.imagenes[self.n]
        self.rect=self.image.get_rect()

    def update(self):
        self.image=self.imagenes[self.n]        

class Cursor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        self.image=pygame.image.load("imagenes/cursor.png")  
        self.rect=self.image.get_rect()

    def update(self):
        self.rect.x,self.rect.y=pygame.mouse.get_pos()
        self.rect.x=self.rect.x-(self.rect.width/2)
        self.rect.y=self.rect.y-(self.rect.height/2)

def main():
    #Inicializacion
    pygame.init()
    pygame.mouse.set_visible(False)
    pantalla=pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("Pygame")
    reloj=pygame.time.Clock()
    fondo=pygame.image.load("imagenes/fondo.png")
    meta=pygame.image.load("imagenes/meta.png")
    Fondo=pygame.mixer.Sound("imagenes/fondo.wav")
    sonido=pygame.mixer.Sound("imagenes/sonido.wav")
    explosion=pygame.mixer.Sound("imagenes/explosion.wav")
    shop=pygame.mixer.Sound("imagenes/shop.wav")
    informacion=(0,HEIGHT-40,WIDTH,40)
    termino=True
    contadorBalas=0
    contadorVidas=0
    misil3=pygame.image.load("imagenes/misiles3.png")
    misil2=pygame.image.load("imagenes/misiles2.png")
    misil1=pygame.image.load("imagenes/misiles1.png")
    nada=pygame.image.load("imagenes/nada.png")
    misiles=[misil3,misil2,misil1,nada]
    vida2=pygame.image.load("imagenes/vida2.png")
    vida1=pygame.image.load("imagenes/vida1.png")
    vidas=[vida2,vida1,nada]
    #Muros
    muros=pygame.sprite.Group()
    m1=Muros(80,250)
    m1.rect.x=120
    m1.rect.y=150
    m1.image=pygame.image.load("imagenes/muros/m1.png")
    m2=Muros(220,80)
    m2.rect.x=200
    m2.rect.y=240
    m2.image=pygame.image.load("imagenes/muros/m2.png")
    m3=Muros(80,180)
    m3.rect.x=280
    m3.rect.y=0
    m3.image=pygame.image.load("imagenes/muros/m3.png")
    m4=Muros(170,80)
    m4.rect.x=460
    m4.rect.y=80
    m4.image=pygame.image.load("imagenes/muros/m4.png")
    m5=Muros(80,150)
    m5.rect.x=540
    m5.rect.y=200
    m5.image=pygame.image.load("imagenes//muros/m5.png")
    m6=Muros(320,70)
    m6.rect.x=320
    m6.rect.y=430
    m6.image=pygame.image.load("imagenes/muros/m6.png")
    m7=Muros(80,200)
    m7.rect.x=750
    m7.rect.y=0
    m7.image=pygame.image.load("imagenes/muros/m7.png")
    m8=Muros(80,250)
    m8.rect.x=750
    m8.rect.y=250
    m8.image=pygame.image.load("imagenes/muros/m8.png")
    muros.add(m1,m2,m3,m4,m5,m6,m7,m8)
    #Jugador
    jugadores=pygame.sprite.Group()
    j1=Jugador()
    j1.muros=muros
    jugadores.add(j1)
    #Rivales
    rivales=pygame.sprite.Group()
    r1=Rival()
    r1.rect.x=390
    r1.vel_y=3
    r1.bandera=1
    r1.m3=m3
    r2=Rival()
    r2.rect.x=220
    r2.rect.y=350
    r2.vel_x=4
    r2.bandera=2
    r2.radius=200
    r2.m1=m1
    r2.m5=m5
    r2.image=pygame.image.load("imagenes/naveE4.png")
    r3=Rival()
    r3.rect.x=670
    r3.rect.y=310
    r3.vel_y=5
    r3.bandera=3
    r3.radius=300
    rivales.add(r1,r2,r3)
    #Salud del jugador
    saludJ=pygame.sprite.Group()
    saludj1=Salud()
    saludJ.add(saludj1)
    #Balas 
    balas=pygame.sprite.Group()
    #Balas enemigas
    balasE=pygame.sprite.Group()
    #Boton
    botones=pygame.sprite.Group()
    b1=Boton()
    b1.rect.x=370
    b1.rect.y=150
    botones.add(b1)
    #Cursor
    cursor=pygame.sprite.Group()
    c1=Cursor()
    cursor.add(c1)
    #Previos
    shop.play()
    seguir=False
    while not seguir:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            if b1.n==1:
                if evento.type==MOUSEBUTTONDOWN:
                    shop.stop()
                    sonido.play()
                    pygame.time.wait(1000)
                    seguir=True
                    botones.remove(b1)
                    cursor.remove(c1)                   
                else:
                    b1.n=0        
        for b in botones:
            b_col=pygame.sprite.spritecollide(b,cursor,False)
            for e in b_col:                    
                b1.n=1

        pantalla.blit(fondo,(0,0))                 
        botones.update() 
        botones.draw(pantalla)
        cursor.update()
        cursor.draw(pantalla)
        pygame.display.flip()                          
    #Ciclo del juego
    Fondo.play()
    while termino:
        #Captura de eventos
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == KEYDOWN:
                if evento.key == K_LEFT:
                    j1.vel_x=-5
                    j1.vel_y=0
                    j1.n=3
                if evento.key == K_RIGHT:
                    j1.vel_x=5
                    j1.vel_y=0
                    j1.n=1
                if evento.key == K_UP:
                    j1.vel_y=-5
                    j1.vel_x=0
                    j1.n=0
                if evento.key == K_DOWN:
                    j1.vel_y=5
                    j1.vel_x=0
                    j1.n=2
                if contadorBalas<3:    
                    if evento.key ==K_SPACE:
                        bala=Bala()
                        if j1.n==0:                            
                            bala.image=pygame.image.load("imagenes/misil.png")
                            bala.rect.x=j1.rect.x+((j1.rect.width/2)-(bala.rect.width/2))   
                            bala.rect.y=j1.rect.y
                            bala.vel_x=0
                            bala.vel_y=-7
                        if j1.n==1:
                            bala.image=pygame.image.load("imagenes/misil4.png")
                            bala.rect.x=j1.rect.x+((j1.rect.width/2)-(bala.rect.width/2))
                            bala.rect.y=j1.rect.y+((j1.rect.height/2)-(bala.rect.width/2))   
                            bala.vel_x=7
                            bala.vel_y=0
                        if j1.n==2:
                            bala.image=pygame.image.load("imagenes/misil3.png")
                            bala.rect.x=j1.rect.x+((j1.rect.width/2)-(bala.rect.width/2))   
                            bala.rect.y=j1.rect.y
                            bala.vel_x=0
                            bala.vel_y=7
                        if j1.n==3:
                            bala.image=pygame.image.load("imagenes/misil2.png")
                            bala.rect.x=j1.rect.x+((j1.rect.width/2)-(bala.rect.width/2))
                            bala.rect.y=j1.rect.y+((j1.rect.height/2)-(bala.rect.width/2))
                            bala.vel_x=-7
                            bala.vel_y=0                
                        balas.add(bala)
                        contadorBalas+=1                         
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
        for b in balas:    
            b_col=pygame.sprite.spritecollide(b,rivales,True)
            b_col2=pygame.sprite.spritecollide(b,muros,False)    
            for e in b_col: 
                balas.remove(b)
            for a in b_col2: 
                balas.remove(b)
            if (b.rect.x<-10) or (b.rect.y<-10) or (b.rect.x>WIDTH) or (b.rect.y>HEIGHT-b.rect.height-40):  
                balas.remove(b)

        for r in rivales:
            if pygame.sprite.collide_circle(r,j1):
                if r.bandera==1:
                    if r.temp<=0:   
                        balae=Bala()
                        if r.n==1:    
                            balae.rect.x=r.rect.x+((r.rect.width/2)-(balae.rect.width/2))   
                            balae.rect.y=r.rect.y
                            balae.vel_y=-7   
                            balae.image=pygame.image.load("imagenes/misilE2.png") 
                        if r.n==2:
                            balae.rect.x=r.rect.x+((r.rect.width/2)-(balae.rect.width/2))   
                            balae.rect.y=r.rect.y   
                            balae.vel_y=7   
                            balae.image=pygame.image.load("imagenes/misilE.png")
                        balasE.add(balae)
                if r.bandera==2:
                    if r.temp<=0:  
                        balae=Bala()
                        if r.n==1:     
                            balae.rect.x=r.rect.x+((r.rect.width/2)-(balae.rect.width/2))   
                            balae.rect.y=r.rect.y+((r.rect.height/2)-(balae.rect.width/2))      
                            balae.vel_x=-7  
                            balae.image=pygame.image.load("imagenes/misilE4.png")
                        if r.n==2:
                            balae.rect.x=r.rect.x+((r.rect.width/2)-(balae.rect.width/2))   
                            balae.rect.y=r.rect.y+((r.rect.height/2)-(balae.rect.width/2))      
                            balae.vel_x=7   
                            balae.image=pygame.image.load("imagenes/misilE3.png")
                        balasE.add(balae)            
                if r.bandera==3:
                    if r.temp<=0:  
                        balae=Bala()
                        if r.n==1:     
                            balae.rect.x=r.rect.x+((r.rect.width/2)-(balae.rect.width/2))   
                            balae.rect.y=r.rect.y   
                            balae.vel_y=-7   
                            balae.image=pygame.image.load("imagenes/misilE2.png") 
                        if r.n==2:
                            balae.rect.x=r.rect.x+((r.rect.width/2)-(balae.rect.width/2))   
                            balae.rect.y=r.rect.y   
                            balae.vel_y=7   
                            balae.image=pygame.image.load("imagenes/misilE.png")                      
                        balasE.add(balae)   
                r.temp=random.randrange(50)

        for b in balasE:    
            b_col=pygame.sprite.spritecollide(b,jugadores,False)
            b_col2=pygame.sprite.spritecollide(b,muros,False)    
            for e in b_col: 
                balasE.remove(b)
                j1.salud-=50
                explosion.play()
                if j1.salud<200 and j1.salud>100:
                    saludj1.color=AMARILLO
                if j1.salud<100:
                    saludj1.color=ROJO
                saludj1.actualizar(j1.salud)
            for a in b_col2:
                balasE.remove(b)                                                                                        
            if b.rect.y<-10 or b.rect.bottom>HEIGHT-b.rect.height-10:  
                balasE.remove(b)

        if j1.salud<=0:
            contadorVidas+=1
            j1.vidas-=1
            contadorBalas=0
            j1.rect.x=0
            j1.rect.y=0
            j1.salud=300
            saludj1.color=VERDE
            saludj1.actualizar(j1.salud) 

        if j1.vidas==0:
            termino=False

        if (j1.rect.x>WIDTH-100) and (j1.rect.top<80):
            termino=False               
              
        #Refresco de Pantalla
        reloj.tick(50)
        pantalla.blit(fondo,(0,0))  
        pygame.draw.rect(pantalla,NEGRO,informacion) 
        pantalla.blit(meta,(WIDTH-100,80))
        pantalla.blit(vidas[contadorVidas],(350,HEIGHT-35))
        pantalla.blit(misiles[contadorBalas],(500,HEIGHT-35)) 
        muros.update()
        jugadores.update()
        rivales.update()
        balasE.update()
        balas.update()  
        saludJ.update() 
        muros.draw(pantalla)
        jugadores.draw(pantalla)
        rivales.draw(pantalla)
        balasE.draw(pantalla)
        balas.draw(pantalla) 
        saludJ.draw(pantalla)
        pygame.display.flip() 

    fuente=pygame.font.Font(None,76)
    if j1.vidas==0:
        texto=fuente.render("JUGADOR 1 LOSSER",True,BLANCO)   
    else:
        texto=fuente.render("JUGADOR 1 WINNER",True,BLANCO)     
       
    Fondo.stop()    
    pantalla.blit(fondo,(0,0))
    pantalla.blit(texto,(240,200))
    pygame.display.flip()
    pygame.time.wait(2000)    

if __name__ == "__main__":
    while True:
        main()
   