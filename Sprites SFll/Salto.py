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
muros=pygame.sprite.Group()
todos=pygame.sprite.Group()

#Clases y Funciones.
class Jugador(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.Surface([50,50])
		self.image.fill(BLANCO)
		self.rect=self.image.get_rect()
		self.vel_posX=0
		self.vel_posY=0
		self.gravity=0.4
		self.salto=False

	def gravedad(self):
		if self.vel_posY == 0:
			self.vel_posY=1
		else:
			self.vel_posY+=self.gravity

	def update(self):
		self.gravedad()
		self.rect.x+=self.vel_posX
		self.rect.y+=self.vel_posY

		if self.rect.y >= (HEIGHT-self.rect.height):
			self.vel_posY=0
			self.rect.y=HEIGHT-self.rect.height

class Muro(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.Surface([100,50])
		self.image.fill(VERDE)
		self.rect=self.image.get_rect()
		self.rect.x=200
		self.rect.y=100

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
	muro=Muro()
	muros.add(muro)
	todos.add(jugadores,muro)
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
			if evento.key == K_UP:
				jugador.salto=True
		if evento.type == KEYUP:
			jugador.vel_posX=0

		#logica
		ls_col=pygame.sprite.spritecollide(jugador,muros,False)
		for p in ls_col:
			if (jugador.rect.bottom >= p.rect.top) and (jugador.vel_posY > 0):
				jugador.rect.bottom = p.rect.top
				jugador.vel_posY=0
			if (jugador.rect.top < p.rect.bottom) and (jugador.vel_posY < 0):
				jugador.rect.top = p.rect.bottom
				jugador.vel_posY=0

		if jugador.salto:
			jugador.vel_posY=-10
			jugador.salto=False		
		#Actualizacion
		pantalla.fill(NEGRO)
		todos.update()
		todos.draw(pantalla)
		pygame.display.flip()
		reloj.tick(100)

if __name__ == "__main__":
	main()
