#Modulos
import pygame, sys, random
from pygame.locals import *

#Constantes.
SIZE=WIDTH,HEIGHT=400,225
BLANCO=(255,255,255)
NEGRO=(0,0,0)
ROJO=(255,0,0)
VERDE=(0,255,0)
AZUL=(0,0,255)
AMARILLO=(246,255,51)
AGUAMARINA=(51,255,199)

jugadores=pygame.sprite.Group()
objetos=pygame.sprite.Group()
hadoukens=pygame.sprite.Group()
todos=pygame.sprite.Group()

#Clases y Funciones.
class Jugador(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.imagenSprite=pygame.image.load("imagenes/ken.png")
		imagenAncho=self.imagenSprite.get_rect()[2]
		imagenAlto=self.imagenSprite.get_rect()[3]
		cantidadX=7
		cantidadY=11
		corteX=imagenAncho/cantidadX
		corteY=imagenAlto/cantidadY
		self.matriz=Recorte(self.imagenSprite,corteX,corteY,cantidadX,cantidadY)
		self.action=1
		self.i=0
		self.direction=0
		self.lim=[3,3,2,4,1,3,4,4,6,0]
		self.image=self.matriz[self.action][self.i]
		self.rect=self.image.get_rect()
		self.rect.x=70
		self.rect.y=HEIGHT-100
		self.vel_posX=0
		self.vel_posY=0

	def update(self):
		self.image=self.matriz[self.action][self.i]
		self.i+=1
		if self.i>self.lim[self.action]:
			self.i=0
			if self.action==0:
				hadouken=Hadouken(self.matriz)
				hadouken.rect.left=self.rect.right-5
				hadouken.rect.top=self.rect.top-5
				hadoukens.add(hadouken)
				todos.add(hadoukens)
				self.action=1

			if self.action==2 or self.action==6 or self.action==7 or self.action==8:
				self.action=1

		self.rect.x+=self.vel_posX
		self.rect.y+=self.vel_posY

class Hadouken(pygame.sprite.Sprite):
	def __init__(self,matriz):
		pygame.sprite.Sprite.__init__(self)
		self.matriz=matriz
		self.image=self.matriz[4][0]
		self.rect=self.image.get_rect()
		self.i=0
		self.vel_posX=20
		self.limite=True

	def update(self):
		self.rect.x+=self.vel_posX
		if self.limite:
			self.image=self.matriz[4][self.i]
			self.i+=1
			if self.i>1:
				self.i=0

class Objeto(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.Surface([50,80])
		self.image.fill(BLANCO)
		self.rect=self.image.get_rect()
		self.rect.x=100
		self.rect.y=100
		self.des=0

	def update(self):
		if self.des > 0:
			self.des -= 1
		self.rect.x+=self.des


def Recorte(imagenSprite,corteX,corteY,cantidadX,cantidadY):
	matriz=[]
	for y in range(cantidadY):
		matriz.append([])
		for x in range(cantidadX):
			cuadro=imagenSprite.subsurface((x*corteX),(y*corteY),corteX,corteY)
			matriz[y].append(cuadro)
	return matriz

def main():
    #Inicializacion
    pygame.init()
    pantalla=pygame.display.set_mode((SIZE))
    pygame.display.set_caption("StreetFightherII")
    jugador=Jugador()
    jugadores.add(jugador)
    objeto=Objeto()
    objetos.add(objeto)
    todos.add(jugadores,objeto)
    reloj=pygame.time.Clock()
    #Ciclo del juego
    while True:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == KEYDOWN:
                if evento.key == K_LEFT:
                    jugador.vel_posX=-5
                if evento.key == K_RIGHT:
                    jugador.vel_posX=5
                if evento.key == K_DOWN:
                    jugador.vel_posY=5
                if evento.key == K_UP:
                    jugador.vel_posY=-5
                if evento.key == K_SPACE:
                    jugador.action=0
                    jugador.i=0
                if evento.key == K_z:
                    jugador.action=2
                    jugador.i=0
                if evento.key == K_x:
                    jugador.action=6
                    jugador.i=0
                if evento.key == K_c:
                    jugador.action=7
                    jugador.i=0
            if evento.type == KEYUP:
				jugador.vel_posX=0
				jugador.vel_posY=0

        #Logica
        ls_col=pygame.sprite.spritecollide(jugador,objetos,False)
        if jugador.action==2:
            for e in ls_col:
                pa= e.rect.bottom-10
                if jugador.rect.bottom >= pa:
                    e.des=10

        #Actualizacion
        pantalla.fill(NEGRO)
        todos.update()
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(10)

if __name__ == "__main__":
	main()
