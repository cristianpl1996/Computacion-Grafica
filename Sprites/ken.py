#Modulos
import pygame, sys
from pygame.locals import *

#Constantes.
SIZE=WIDTH,HEIGHT=400,225
BLANCO=(255,255,255)
NEGRO=(0,0,0)
ROJO=(255,0,0)
VERDE=(0,255,0)
AZUL=(0,0,255)
AMARILLO=(246,255,51)
vel_posX,vel_posY=0,0
posX,posY=0,0
jugadores=pygame.sprite.Group()
hadoukens=pygame.sprite.Group()

#Clases y Funciones.
class Jugador(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.pkTheme=pygame.mixer.Sound("imagenes/pkTheme.wav")
		self.imageSprite=pygame.image.load("imagenes/ken.png")
		imageWidth=self.imageSprite.get_rect()[2]
		imageHeight=self.imageSprite.get_rect()[3]
		cantidadX=7
		cantidadY=10
		corteX=imageWidth/cantidadX
		corteY=imageHeight/cantidadY
		self.matriz=Recorte(self.imageSprite,corteX,corteY,cantidadX,cantidadY)
		self.image=self.matriz[1][0]
		self.rect=self.image.get_rect()
		self.rect.x=0
		self.rect.y=HEIGHT-100
		self.action=0
		self.direction=0
		self.i=0
		self.rightApretada=0
		self.leftApretada=0
		self.espacioApretada=0
		self.downApretada=0
		self.upApretada=0
		self.zApretada=0
		self.xApretada=0
		self.cApretada=0

	def update(self):
		global vel_posX,posX	
		keyState=pygame.key.get_pressed()

		if keyState[K_SPACE]:
			self.zApretada=False
			self.xApretada=False
			self.cApretada=False
			self.downApretada=False
			self.rightApretada=False
			self.leftApretada=False
			self.espacioApretada=True
			vel_posX=0
			if self.espacioApretada:
				self.action=4
				self.i=0
		elif keyState[K_RIGHT]:
			self.zApretada=False
			self.xApretada=False
			self.cApretada=False
			self.downApretada=False
			self.rightApretada=False
			self.leftApretada=False
			self.rightApretada=True	
			if self.rightApretada:
				self.action=1
				self.direction=1
				if self.rect.x==WIDTH-70:
					vel_posX=-10
					if posX<=-WIDTH:
						vel_posX=0
		elif keyState[K_LEFT]:
			self.zApretada=False
			self.xApretada=False
			self.cApretada=False
			self.upApretada=False
			self.downApretada=False
			self.espacioApretada=False
			self.rightApretada=False	
			self.leftApretada=True	
			if self.leftApretada:
				self.action=1
				self.direction=2
				if self.rect.x==0:
					vel_posX=10
					if posX>=0:
						vel_posX=0
		elif keyState[K_DOWN]:
			self.zApretada=False
			self.xApretada=False
			self.cApretada=False
			self.upApretada=False
			self.espacioApretada=False
			self.rightApretada=False
			self.leftApretada=False
			self.downApretada=True
			vel_posX=0
			if self.downApretada:
				self.action=2
				self.i=0
		elif keyState[K_UP]:
			self.zApretada=False
			self.xApretada=False
			self.cApretada=False
			self.downApretada=False
			self.espacioApretada=False
			self.rightApretada=False
			self.leftApretada=False
			self.upApretada=True
			vel_posX=0
			if self.upApretada:
				self.action=3
				self.i=0
		elif keyState[K_z]:
			self.xApretada=False
			self.cApretada=False
			self.downApretada=False
			self.espacioApretada=False
			self.rightApretada=False
			self.leftApretada=False
			self.upApretada=False
			self.zApretada=True
			vel_posX=0
			if self.zApretada:
				self.action=5
				self.i=0
		elif keyState[K_x]:
			self.zApretada=False
			self.cApretada=False
			self.downApretada=False
			self.espacioApretada=False
			self.rightApretada=False
			self.leftApretada=False
			self.upApretada=False
			self.xApretada=True
			vel_posX=0
			if self.xApretada:
				self.action=6
				self.i=0
		elif keyState[K_c]:
			self.zApretada=False
			self.xApretada=False
			self.downApretada=False
			self.espacioApretada=False
			self.rightApretada=False
			self.leftApretada=False
			self.upApretada=False
			self.cApretada=True
			vel_posX=0
			if self.cApretada:
				self.action=7
				self.i=0		
		else:
			vel_posX=0
			self.zApretada=False
			self.xApretada=False
			self.cApretada=False
			self.upApretada=False
			self.downApretada=False
			self.espacioApretada=False
			self.rightApretada=False
			self.leftApretada=False								

		if self.action==0:
			self.image=self.matriz[1][self.i]
			self.i+=1
			if self.i>3:
				self.i=0
				self.action=0

		if self.action==1:
			self.image=self.matriz[3][self.i]
			self.i+=1
			if self.direction==1:
				self.rect.x+=10
			if self.direction==2:
				self.rect.x-=10 
			if self.rect.right>WIDTH:
				self.rect.x=WIDTH-70
			if self.rect.left<0:
				self.rect.x=0	        	
			if self.i>4:
				self.i=0
				self.action=0

		if self.action==2:
			self.image=self.matriz[9][self.i]
			self.action=0

		if self.action==3:
			self.image=self.matriz[8][self.i]
			self.i+=1
			if not self.upApretada:
				self.rect.y=HEIGHT-120		
			if self.i>6:
				self.i=0
				self.rect.y=HEIGHT-100	
				self.action=0

		if self.action==4:
			self.image=self.matriz[0][self.i]
			self.i+=1
			if self.i>3:
				self.i=0
				hadouken=Hadouken(self.matriz,self.rect.x)
				hadouken.hadouken.play()
				hadouken.rect.x=self.rect.x+50
				hadouken.rect.y=self.rect.y
				hadoukens.add(hadouken)
				self.action=0

		if self.action==5:
			self.image=self.matriz[2][self.i]
			self.i+=1
			if self.i>2:
				self.pkTheme.play()
				self.i=0
				self.action=0

		if self.action==6:
			self.image=self.matriz[6][self.i]
			self.i+=1
			if self.i>4:
				self.pkTheme.play()
				self.i=0
				self.action=0

		if self.action==7:
			self.image=self.matriz[7][self.i]
			self.i+=1
			if self.i>4:
				self.pkTheme.play()
				self.i=0
				self.action=0

class Hadouken(pygame.sprite.Sprite):
	def __init__(self,matriz,x):
		pygame.sprite.Sprite.__init__(self)
		self.hadouken=pygame.mixer.Sound("imagenes/hadouken.wav")
		self.matriz=matriz
		self.x=x
		self.image=self.matriz[4][0]
		self.rect=self.image.get_rect()
		self.i=0
		self.limite=True

	def update(self):
		self.rect.x+=10
		if self.limite:
			self.image=self.matriz[4][self.i]
			self.i+=1
			if self.i>1:
				self.i=0	
		if self.rect.x>self.x+(WIDTH/2):
			self.limite=False
			self.image=self.matriz[5][self.i]
			self.i+=1
			if self.i>3:
				self.i=0
				hadoukens.remove(self)				
		
def Recorte(imageSprite,corteX,corteY,cantidadX,cantidadY):
	matriz=[]
	for y in range(cantidadY):
		matriz.append([])
		for x in range(cantidadX):
			cuadro=imageSprite.subsurface((x*corteX),(y*corteY),corteX,corteY)
			matriz[y].append(cuadro)
	return matriz

def main():
	#Inicializacion
	global vel_posX,posX
	pygame.init()
	pantalla=pygame.display.set_mode((SIZE))
	pygame.display.set_caption("Pygame")
	reloj=pygame.time.Clock()
	kenTheme=pygame.mixer.Sound("imagenes/kenTheme.wav")
	mainTheme=pygame.mixer.Sound("imagenes/mainTheme.wav")
	teclaTheme=pygame.mixer.Sound("imagenes/teclaTheme.wav")
	fondo=pygame.image.load("imagenes/fondo.png")
	fondoMenu=pygame.image.load("imagenes/fondoMenu.png")
	letra=pygame.image.load("imagenes/letraMenu.png")
	letra2=pygame.image.load("imagenes/letraMenu2.png")
	letras=[letra,letra2]
	jugador=Jugador()
	jugadores.add(jugador)
	#Previos
	mainTheme.play()
	i=0
	seguir=False
	while not seguir:
		for evento in pygame.event.get():
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()
			if evento.type == KEYDOWN:
				teclaTheme.play()
				mainTheme.stop()
				pygame.time.wait(2000)
				seguir=True	

		pantalla.blit(fondoMenu,(0,0))
		pantalla.blit(letras[i],(125,165))
		segundos=pygame.time.get_ticks()/1000
		if(segundos%2)==0:
			i=1
		else:
			i=0            
		pygame.display.flip() 
    #Ciclo del juego    
	kenTheme.play()
	while True:
		for evento in pygame.event.get():
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()						
		posX+=vel_posX			
		pantalla.fill(NEGRO)
		pantalla.blit(fondo,[posX,posY])
		jugadores.update()
		hadoukens.update()
		jugadores.draw(pantalla)
		hadoukens.draw(pantalla)
		pygame.display.flip()
		reloj.tick(10)
		
if __name__ == "__main__":
    main()