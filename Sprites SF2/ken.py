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
		self.pkTheme=pygame.mixer.Sound("imagenes/pkTheme.wav")
		self.colisionPunchTheme=pygame.mixer.Sound("imagenes/colisionPunchTheme.wav")
		self.colisionKickTheme=pygame.mixer.Sound("imagenes/colisionKickTheme.wav")
		self.colisionKick2Theme=pygame.mixer.Sound("imagenes/colisionKick2Theme.wav")
		self.kenScreamTheme=pygame.mixer.Sound("imagenes/kenScreamTheme.wav")
		self.lossTheme=pygame.mixer.Sound("imagenes/lossTheme.wav")
		self.winTheme=pygame.mixer.Sound("imagenes/winTheme.wav")
		self.imageSprite=pygame.image.load("imagenes/ken.png")
		imageWidth=self.imageSprite.get_rect()[2]
		imageHeight=self.imageSprite.get_rect()[3]
		cantidadX=7
		cantidadY=11
		corteX=imageWidth/cantidadX
		corteY=imageHeight/cantidadY
		self.matriz=Recorte(self.imageSprite,corteX,corteY,cantidadX,cantidadY)
		self.image=self.matriz[1][0]
		self.rect=self.image.get_rect()
		self.rect.x=70
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
		self.colisionHadouken=False
		self.actionJugador=0
		self.salud=150
		self.energia=150
		self.bloqueHadouken=False
		self.banderaSalud=False
		self.Terminar=True
		self.acabo=False

	def limitesEnemigo(self):
		ls_col=pygame.sprite.spritecollide(self,enemigos,False)
		for e in ls_col:
			if self.rect.right>e.rect.left+35:
				self.rect.right=e.rect.left+35
				
	def update(self):
		global vel_posX,posX	
		keyState=pygame.key.get_pressed()
		self.limitesEnemigo()

		if not self.banderaSalud:
			if keyState[K_SPACE]:
				if not self.bloqueHadouken:
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
				else:
					if self.energia>50:
						self.bloqueHadouken=False
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
					if self.rect.x==WIDTH-140:
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
					if self.rect.x==70:
						vel_posX=10
						if posX>=0:
							vel_posX=0
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
					
			if self.action==1:
				self.image=self.matriz[3][self.i]
				self.i+=1
				if self.direction==1:
					self.rect.x+=10
				if self.direction==2:
					self.rect.x-=10 
				if self.rect.right>WIDTH-70:
					if posX!=-WIDTH:
						self.rect.x=WIDTH-140
					else:
						if self.rect.right>WIDTH:
							self.rect.x=WIDTH-70
				if self.rect.left<70:
					if posX!=0:
						self.rect.x=70
					else:
						if self.rect.x<0:
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
				if self.energia>50:
					self.image=self.matriz[0][self.i]
					self.i+=1
					if self.i>3:
						self.i=0
						hadouken=Hadouken(self.matriz,self.rect.x)
						hadouken.hadouken.play()
						hadouken.rect.left=self.rect.right-10
						hadouken.rect.y=self.rect.y
						hadoukens.add(hadouken)
						self.energia-=50
						self.action=0
				else:
					self.bloqueHadouken=True
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

			if self.action==8:
				self.image=self.matriz[9][self.i]
				self.i+=1
				if self.i>2:
					self.i=0
					if self.actionJugador==5:
						self.colisionPunchTheme.play()
					if self.actionJugador==6:
						self.colisionKickTheme.play()
					if self.actionJugador==7:
						self.colisionKick2Theme.play()
					self.salud-=30	
					self.action=0
			
			ls_col=pygame.sprite.spritecollide(self,enemigos,False)
			for e in ls_col:
				if self.action==4:
			 		e.i=1
					e.action=8
				elif self.action==5:
					e.actionJugador=5
			 		e.i=1
					e.action=8
				elif self.action==6:
					e.actionJugador=6
					e.i=1
					e.action=8 
				elif self.action==7:
					e.actionJugador=7
					e.i=1
					e.action=8

			if self.colisionHadouken:
				self.action=8
				self.i=1
				self.colisionHadouken=False

			if self.salud==0:
				self.kenScreamTheme.play()
				self.rect.x-=40
				self.banderaSalud=True	

		else:
			self.image=self.matriz[10][self.i]
			if not self.acabo:
				self.i+=1
				if self.i>3:
					self.i=3
					self.acabo=True
			else:
				self.Terminar=False		
					
class Enemigo(pygame.sprite.Sprite):
	def __init__(self,salude,energiae):
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
		self.rect.x=800
		self.rect.y=HEIGHT-100
		self.action=0
		self.direction=0
		self.i=0
		self.j=0
		self.k=0
		self.vel_posX=0
		self.posJugadorRight=0
		self.colisionHadouken=False
		self.actionJugador=0
		self.banderaSalud=False
		self.salud=50
		self.energia=50
		self.bloqueHadouken=False
		self.termino=False
		self.salude=salude
		self.energiae=energiae
		self.murio=False
		self.Terminar2=True

	def update(self):
		if not self.banderaSalud:
			if not self.termino:
				if self.rect.left+35>self.posJugadorRight:
					if not self.colisionHadouken:
						self.vel_posX=5
						self.action=1
					else:
						self.vel_posX=0
						self.i=1
						self.action=8
						self.rect.right+=20
						self.colisionHadouken=False
				else:
					self.vel_posX=0
					
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
					if not self.bloqueHadouken:
						self.image=self.matriz[0][self.i]
						self.i+=1
						if self.i>3:
							self.i=0
							hadouken=Hadouken(self.matriz,self.rect.x)
							hadouken.hadouken.play()
							hadouken.vel_posX=-10
							hadouken.rect.right=self.rect.left+10
							hadouken.rect.y=self.rect.y
							hadoukens.add(hadouken)
							self.energia-=25
							if self.energia==0:
								self.bloqueHadouken=True
							self.action=0	
					else:			
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

				if self.action==8:
					self.image=self.matriz[9][self.i]
					self.i+=1
					if self.i>2:
						self.i=0
						if self.actionJugador==5:						
							self.colisionPunchTheme.play()
						if self.actionJugador==6:						
							self.colisionKickTheme.play()
						if self.actionJugador==7:						
							self.colisionKick2Theme.play()
						self.salud-=10	
						self.rect.x+=40			
						self.action=0

				ls_col=pygame.sprite.spritecollide(self,jugadores,False)
				for e in ls_col:
					if self.rect.left+35<=self.posJugadorRight:
						self.j+=1
						if self.j==20:
							aleatorio=random.randrange(4,8)
							self.action=aleatorio
							self.j=0
							if self.action==4:
								e.actionJugador=4
							elif self.action==5:
								e.actionJugador=5
						 		e.i=1
								e.action=8
							elif self.action==6:
								e.actionJugador=6
								e.i=1
								e.action=8 
							elif self.action==7:
								e.actionJugador=7
								e.i=1
								e.action=8

				if self.salud==0:
					self.termino=True
					self.kenScreamTheme.play()

			else:
				self.image=self.matriz[10][self.i]
				self.i+=1
				self.k+=5
				if self.i>3:
					self.i=3
				if self.k>100:
					self.Terminar2=False
					self.murio=True
					enemigos.remove(self)
					salud.remove(self.salude)
					energia.remove(self.energiae)

		else:
			self.vel_posX=0	
		self.rect.x-=self.vel_posX			

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
				e.colisionHadouken=True
				self.colisionHadoukenTheme.play()
				hadoukens.remove(self)

		ls_col2=pygame.sprite.spritecollide(self,jugadores,False)
		for e in ls_col2:
			if self.rect.left<e.rect.right-70:
				e.colisionHadouken=True
				self.colisionHadoukenTheme.play()
				hadoukens.remove(self)

class Salud(pygame.sprite.Sprite):
    def __init__(self,alto=10,x=20,y=20):
        pygame.sprite.Sprite.__init__(self)
        self.alto=alto
        self.image=pygame.Surface([150,self.alto])
        self.color=AMARILLO
        self.image.fill(self.color)
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y

    def actualizar(self,salud,x=20,y=20):
        self.image=pygame.Surface([salud,self.alto])
        self.image.fill(self.color)
        self.rect.x=x
        self.rect.y=y

class Energia(pygame.sprite.Sprite):
    def __init__(self,alto=3,x=20,y=30):
        pygame.sprite.Sprite.__init__(self)
        self.alto=alto
        self.image=pygame.Surface([150,self.alto])
        self.color=AGUAMARINA
        self.image.fill(self.color)
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y

    def actualizar(self,energia=3,x=20,y=30):
        self.image=pygame.Surface([energia,self.alto])
        self.image.fill(self.color)
        self.rect.x=x
        self.rect.y=y        
												
									
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
	telonRojo=pygame.Surface([150,10])
	telonRojo.fill(ROJO)
	telonRojoE=pygame.Surface([50,3.3])
	telonRojoE.fill(ROJO)
	kenTheme=pygame.mixer.Sound("imagenes/kenTheme.wav")
	mainTheme=pygame.mixer.Sound("imagenes/mainTheme.wav")
	teclaTheme=pygame.mixer.Sound("imagenes/teclaTheme.wav")
	victoryTheme=pygame.mixer.Sound("imagenes/victoryTheme.wav")
	fondo=pygame.image.load("imagenes/fondoJuego.png")
	fondoMenu=pygame.image.load("imagenes/fondoMenu.png")
	letra=pygame.image.load("imagenes/letraMenu.png")
	letra2=pygame.image.load("imagenes/letraMenu2.png")
	lettersKen=pygame.image.load("imagenes/lettersKen.png")
	letras=[letra,letra2]
	jugador=Jugador()
	jugadores.add(jugador)
	saludj=Salud()
	salude=Salud(3.3)
	salud.add(saludj,salude)
	energiaj=Energia()
	energiae=Energia(2)
	energia.add(energiaj,energiae)
	enemigo=Enemigo(salude,energiae)
	enemigos.add(enemigo)
	Terminar=True
	Terminar2=True
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
	while (Terminar and Terminar2):
		for evento in pygame.event.get():
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()
		#Logica
		posJugadorRight=jugador.rect.right
		enemigo.posJugadorRight=posJugadorRight
		saludj.actualizar(jugador.salud)
		energiaj.actualizar(jugador.energia)
		salude.actualizar((enemigo.salud),(enemigo.rect.x+10),(enemigo.rect.y-10))
		energiae.actualizar((enemigo.energia),(enemigo.rect.x+10),(enemigo.rect.y-8))
		segundos=pygame.time.get_ticks()/1000
		if(segundos%2)==0:
			if jugador.energia!=150:
				jugador.energia+=1 

		enemigo.banderaSalud=jugador.banderaSalud		
		Terminar=jugador.Terminar
		Terminar2=enemigo.Terminar2	
		#Actualizacion								
		posX+=vel_posX			
		pantalla.fill(NEGRO) 	
		pantalla.blit(fondo,[posX,posY])
		pantalla.blit(telonRojo,(20,20))
		if not enemigo.murio:
			pantalla.blit(telonRojoE,((enemigo.rect.x+10),(enemigo.rect.y-10)))
		pantalla.blit(lettersKen,(20,35))
		jugadores.update()
		enemigos.update()
		hadoukens.update()
		salud.update()
		energia.update()
		jugadores.draw(pantalla)
		enemigos.draw(pantalla)
		hadoukens.draw(pantalla)
		salud.draw(pantalla)
		energia.draw(pantalla)  
		pygame.display.flip()
		reloj.tick(10)
		
	kenTheme.stop()
	pygame.time.wait(500)
	victoryTheme.play()
	pygame.time.wait(2000)
	if not jugador.Terminar:	
		jugador.lossTheme.play()
	else:
		jugador.winTheme.play()
	pygame.time.wait(2000)
	jugadores.remove(jugador)
	salud.remove(saludj)
	energia.remove(energiaj)
	enemigos.remove(enemigo)
	salud.remove(salude)
	energia.remove(energiae)
	posX=0	
		
if __name__ == "__main__":
    while True:
    	main()