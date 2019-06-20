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
vel_posX,vel_posY=0,0
posX,posY=0,0
jugadores=pygame.sprite.Group()
enemigos=pygame.sprite.Group()
hadoukens=pygame.sprite.Group()
salud=pygame.sprite.Group()
energia=pygame.sprite.Group()
    
#Clases y Funciones.
class Jugador(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.kenScreamTheme=pygame.mixer.Sound("imagenes/kenScreamTheme.wav")
		self.imageSprite=pygame.image.load("imagenes/ken.png")
		imageWidth=self.imageSprite.get_rect()[2]
		imageHeight=self.imageSprite.get_rect()[3]
		cantidadX=7
		cantidadY=11
		corteX=imageWidth/cantidadX
		corteY=imageHeight/cantidadY
		print corteX,corteY
		self.matriz=Recorte(self.imageSprite,corteX,corteY,cantidadX,cantidadY)
		self.image=self.matriz[1][0]
		self.rect=self.image.get_rect()
		self.rect.x=70
		self.rect.y=HEIGHT-100
		self.action=0
		self.direction=0
		self.i=0
		self.vel_posX=0


	def limitesEnemigo(self):
		ls_col=pygame.sprite.spritecollide(self,enemigos,False)
		for e in ls_col:
			if self.rect.right>e.rect.left+25:
				self.rect.right=e.rect.left+25	

	def update(self):
		global vel_posX,posX
		self.limitesEnemigo()	
		#Actions
		if self.action==0:
			self.image=self.matriz[1][self.i]
			self.i+=1
			if self.i>3:
				self.i=0
				
		if self.action==1:
			self.image=self.matriz[3][self.i]
			self.i+=1	
			if self.i>4:
				self.i=0
			if self.direction==1:
				self.vel_posX=-10
				if self.rect.x==70:
					self.vel_posX=0
					vel_posX=10
					if posX>=0:
						vel_posX=0
						if self.rect.left<=70:
							self.vel_posX=-10	
			if self.direction==2:
				self.vel_posX=10
				if self.rect.x==WIDTH-140:
					self.vel_posX=0
					vel_posX=-10
					if posX<=-WIDTH:
						vel_posX=0
						if self.rect.right>=WIDTH-70:
							self.vel_posX=10
			if self.rect.right>=WIDTH:
				self.rect.x=WIDTH-70
			if self.rect.x<=0:
				self.rect.x=0				

		if self.action==2:
			self.image=self.matriz[9][self.i]

		if self.action==3:
			self.image=self.matriz[8][self.i]
			self.i+=1
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
				self.action=0
				hadouken=Hadouken(self.matriz,self.rect.x)
				hadouken.hadouken.play()
				hadouken.rect.left=self.rect.right-10
				hadouken.rect.y=self.rect.y
				hadoukens.add(hadouken)
	
		if self.action==5:
			self.image=self.matriz[2][self.i]
			self.i+=1
			if self.i>2:
				self.i=0
				self.action=0

		if self.action==6:
			self.image=self.matriz[6][self.i]
			self.i+=1
			if self.i>4:
				self.i=0
				self.action=0

		if self.action==7:
			self.image=self.matriz[7][self.i]
			self.i+=1
			if self.i>4:
				self.i=0
				self.action=0

		self.rect.x+=self.vel_posX

class Enemigo(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.pkTheme=pygame.mixer.Sound("imagenes/pkTheme.wav")
		self.colisionPunchTheme=pygame.mixer.Sound("imagenes/colisionPunchTheme.wav")
		self.colisionKickTheme=pygame.mixer.Sound("imagenes/colisionKickTheme.wav")
		self.colisionKick2Theme=pygame.mixer.Sound("imagenes/colisionKick2Theme.wav")
		self.kenScreamTheme=pygame.mixer.Sound("imagenes/kenScreamTheme.wav")
		self.imageSprite=pygame.image.load("imagenes/ken2.png")
		imageWidth=self.imageSprite.get_rect()[2]
		imageHeight=self.imageSprite.get_rect()[3]
		cantidadX=7
		cantidadY=11
		corteX=imageWidth/cantidadX
		corteY=imageHeight/cantidadY
		self.matriz=Recorte(self.imageSprite,corteX,corteY,cantidadX,cantidadY)
		self.image=self.matriz[1][0]
		self.rect=self.image.get_rect()
		self.rect.x=300
		self.rect.y=HEIGHT-100
		self.action=0
		self.i=0
		self.vel_posX=0
		self.radius=100

	def update(self):	
		#Actions		
		if self.action==0:
			self.image=self.matriz[1][self.i]
			self.i+=1
			if self.i>3:
				self.i=0
				self.action=0

		if self.action==1:
			self.image=self.matriz[3][self.i]
			self.i+=1	        	
			if self.i>4:
				self.i=0
				self.action=0

		if self.action==4:
			self.image=self.matriz[0][self.i]
			self.i+=1
			if self.i>3:
				self.i=0
				self.action=0
				hadouken=Hadouken(self.matriz,self.rect.x)
				hadouken.hadouken.play()
				hadouken.vel_posX=-10
				hadouken.rect.right=self.rect.left+10
				hadouken.rect.y=self.rect.y
				hadoukens.add(hadouken)

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

		self.rect.x+=self.vel_posX

class Hadouken(pygame.sprite.Sprite):
	def __init__(self,matriz,x):
		pygame.sprite.Sprite.__init__(self)
		self.hadouken=pygame.mixer.Sound("imagenes/hadoukenTheme.wav")
		self.colisionHadoukenTheme=pygame.mixer.Sound("imagenes/colisionHadoukenTheme.wav")
		self.matriz=matriz
		self.x=x
		self.image=self.matriz[4][0]
		self.rect=self.image.get_rect()
		self.i=0
		self.vel_posX=10
		self.limite=True

	def update(self):
		self.rect.x+=self.vel_posX
		if self.limite:
			self.image=self.matriz[4][self.i]
			self.i+=1
			if self.i>1:
				self.i=0	
		if self.rect.x>self.x+(WIDTH/2) or self.rect.x<self.x-(WIDTH/2):
			self.limite=False
			self.image=self.matriz[5][self.i]
			self.i+=1
			if self.i>3:
				self.i=0
				hadoukens.remove(self)

		ls_col=pygame.sprite.spritecollide(self,enemigos,False)
		for e in ls_col:
			if self.rect.right>e.rect.left+70:
				self.colisionHadoukenTheme.play()
				hadoukens.remove(self)

		ls_col2=pygame.sprite.spritecollide(self,jugadores,False)
		for j in ls_col2:
			if self.rect.left<j.rect.right-70:
				self.colisionHadoukenTheme.play()
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
	pygame.display.set_caption("StreetFightherII")
	#Banda Sonora
	mainTheme=pygame.mixer.Sound("imagenes/mainTheme.wav")
	teclaTheme=pygame.mixer.Sound("imagenes/teclaTheme.wav")
	kenTheme=pygame.mixer.Sound("imagenes/kenTheme.wav")
	pkTheme=pygame.mixer.Sound("imagenes/pkTheme.wav")
	#Imagenes
	fondoMenu=pygame.image.load("imagenes/fondoMenu.png")
	letraMenu=pygame.image.load("imagenes/letraMenu.png")
	letraMenu2=pygame.image.load("imagenes/letraMenu2.png")
	letrasMenu=[letraMenu,letraMenu2]
	fondoJuego=pygame.image.load("imagenes/fondoJuego.png")
	#Jugador
	jugador=Jugador()
	jugadores.add(jugador)
	#Enemigo
	enemigo=Enemigo()
	enemigos.add(enemigo)
	#Contador
	i=0
	#Teclas
	leftApretada=0
	rightApretada=0
	upApretada=0
	downApretada=0
	espacioApretada=0
	zApretada=0
	xApretada=0
	cApretada=0
	#Reloj
	reloj=pygame.time.Clock()
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
		pantalla.blit(letrasMenu[i],(125,165))
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
			if evento.type == KEYDOWN:
				if evento.key == K_LEFT:
					jugador.action=1
					jugador.direction=1
					jugador.i=0			
				if evento.key == K_RIGHT:
					jugador.action=1
					jugador.direction=2
					jugador.i=0	
				if evento.key == K_DOWN:
					jugador.action=2
					jugador.i=0							
				if evento.key == K_UP:
					jugador.action=3
					jugador.i=0	
				if evento.key == K_SPACE:
					jugador.action=4
					jugador.i=0	
				if evento.key == K_z:
					jugador.action=5
					jugador.i=0
					pkTheme.play()	
				if evento.key == K_x:
					jugador.action=6
					jugador.i=0
					pkTheme.play()	
				if evento.key == K_c:
					jugador.action=7
					jugador.i=0
					pkTheme.play()
			if evento.type == KEYUP:
				if (evento.key == K_LEFT) or (evento.key == K_RIGHT):
					jugador.action=0
					jugador.vel_posX=0
					vel_posX=0
				if evento.key == K_DOWN:
					jugador.action=0

		#Logica
		if pygame.sprite.collide_circle(enemigo,jugador):
			if enemigo.rect.left+25>jugador.rect.right:
				enemigo.vel_posX=-5
				enemigo.action=1
			else:
				enemigo.vel_posX=0
				enemigo.action=0
		#Actualizacion								
		posX+=vel_posX			
		pantalla.fill(NEGRO) 	
		pantalla.blit(fondoJuego,[posX,posY])
		jugadores.update()
		enemigos.update()
		hadoukens.update()
		jugadores.draw(pantalla)
		enemigos.draw(pantalla)
		hadoukens.draw(pantalla) 
		pygame.display.flip()
		reloj.tick(10)
			
if __name__ == "__main__":
	main()