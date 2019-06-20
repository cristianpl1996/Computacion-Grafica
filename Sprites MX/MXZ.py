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
GRIS=(128,128,128)
vel_posX,vel_posY=0,0
posX,posY=0,0
jugadores=pygame.sprite.Group()
busters=pygame.sprite.Group()

#Clases y Funciones.
class X(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		#Mega Man X - X
		self.imageSprite0_r=pygame.image.load("images/x_r.png")
		self.imageSprite0_l=pygame.image.load("images/x_l.png")
		imageWidth0=self.imageSprite0_r.get_rect()[2]
		imageHeight0=self.imageSprite0_r.get_rect()[3]
		quantityX0=11
		quantityY0=19
		cutX0=imageWidth0/quantityX0
		cutY0=imageHeight0/quantityY0
		self.matrix0_r=Cutout(self.imageSprite0_r,cutX0,cutY0,quantityX0,quantityY0)
		self.matrix0_l=Cutout(self.imageSprite0_l,cutX0,cutY0,quantityX0,quantityY0)
		#Mega Man X - X1.
		self.imageSprite1_r=pygame.image.load("images/x1_r.png")
		self.imageSprite1_l=pygame.image.load("images/x1_l.png")
		self.matrix1_r=Cutout(self.imageSprite1_r,cutX0,cutY0,quantityX0,quantityY0)
		self.matrix1_l=Cutout(self.imageSprite1_l,cutX0,cutY0,quantityX0,quantityY0)
		#Mega Man X - X Saber
		self.imageSprite2_r=pygame.image.load("images/xs_r.png")
		self.imageSprite2_l=pygame.image.load("images/xs_l.png")
		imageWidth2=self.imageSprite2_r.get_rect()[2]
		imageHeight2=self.imageSprite2_r.get_rect()[3]
		quantityX2=11
		quantityY2=2
		cutX2=imageWidth2/quantityX2
		cutY2=imageHeight2/quantityY2
		self.matrix2_r=Cutout(self.imageSprite2_r,cutX2,cutY2,quantityX2,quantityY2)
		self.matrix2_l=Cutout(self.imageSprite2_l,cutX2,cutY2,quantityX2,quantityY2)
		#Main Matrix
		self.matrix_r=[self.matrix0_r,self.matrix1_r,self.matrix2_r]
		self.matrix_l=[self.matrix0_l,self.matrix1_l,self.matrix2_l]
		self.matrix=[self.matrix_r,self.matrix_l]
		#Characteristics
		self.soundBuster=pygame.mixer.Sound("sounds/buster.wav")
		self.image=self.matrix[0][0][0][0]
		self.rect=self.image.get_rect()
		self.rect.x=70
		self.rect.y=HEIGHT-100
		self.action=0
		self.i=0
		self.j=0
		self.direction=0
		self.vel_posX=0
		#Variables Buster
		self.buster=0
		self.charge=0
		self.organize=True
		self.loadBuster=LoadBuster()

	def update(self):
		#Logica
		if not self.organize:
			if self.direction==0:
				self.rect.top+=10
			else:
				self.rect.top+=10
				self.rect.left+=23
			self.organize=True

		self.j+=1
		if self.j>1:
			self.j=0

		if self.buster>2:
			self.loadBuster.rect.x=self.rect.x
			self.loadBuster.rect.y=self.rect.y
			busters.add(self.loadBuster)
		else:
			busters.remove(self.loadBuster)

		self.buster+=self.charge
		self.rect.x+=self.vel_posX
		#Actions
		if self.action==0:
			if self.buster>5:
				self.image=self.matrix[self.direction][self.j][1][self.i]
			else:
				self.image=self.matrix[self.direction][0][1][self.i]
			self.i+=1
			if self.i>2:
				self.i=0

		if self.action==1:
			self.image=self.matrix[self.direction][0][2][self.i]
			self.i+=1
			if self.i>1:
				buster=Buster()
				buster.direction=self.direction
				if self.buster>5 and self.buster<15:
					buster.action=1
					if self.direction==0:
						buster.rect.x=self.rect.x-10
						buster.rect.y=self.rect.y+5
						buster.vel_posX=20
					else:
						buster.rect.x=self.rect.x+10
						buster.rect.y=self.rect.y+5
						buster.vel_posX=-20
				elif self.buster>15:
					buster.action=2
					if self.direction==0:
						buster.rect.x=self.rect.x-10
						buster.rect.y=self.rect.y+5
						buster.vel_posX=20
					else:
						buster.rect.x=self.rect.x+10
						buster.rect.y=self.rect.y+5
						buster.vel_posX=-20
				else:
					self.soundBuster.play()
					buster.action=0
					if self.direction==0:
						buster.rect.x=self.rect.x-15
						buster.rect.y=self.rect.y+5
						buster.vel_posX=20
					else:
						buster.rect.x=self.rect.x+15
						buster.rect.y=self.rect.y+5
						buster.vel_posX=-20
				busters.add(buster)
				self.buster=0
				self.i=0
				self.action=0
				self.loadBuster.i=0
				self.loadBuster.action=0

		if self.action==2:
			if self.organize:
				if self.direction==0:
					self.rect.top-=10
				else:
					self.rect.top-=10
					self.rect.left-=23
				self.organize=False
			self.image=self.matrix[self.direction][2][0][self.i]
			self.i+=1
			if self.i>10:
				self.i=0
				self.action=0
				self.buster=0

		if self.action==3:
			if self.buster>5:
				self.image=self.matrix[self.direction][self.j][3][self.i]
			else:
				self.image=self.matrix[self.direction][0][3][self.i]
			self.i+=1
			if self.i>10:
				self.i=0

		if self.action==4:
			if self.buster>5:
				self.image=self.matrix[self.direction][self.j][5][self.i]
			else:
				self.image=self.matrix[self.direction][0][5][self.i]
			self.i+=1
			if self.i>6:
				self.i=0
				self.action=0		

class Zero(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		#Mega Man X - Zero
		self.imageSprite0_r=pygame.image.load("images/zero_r.png")
		self.imageSprite0_l=pygame.image.load("images/zero_l.png")
		imageWidth0=self.imageSprite0_r.get_rect()[2]
		imageHeight0=self.imageSprite0_r.get_rect()[3]
		quantityX0=11
		quantityY0=15
		cutX0=imageWidth0/quantityX0
		cutY0=imageHeight0/quantityY0
		self.matrix0_r=Cutout(self.imageSprite0_r,cutX0,cutY0,quantityX0,quantityY0)
		self.matrix0_l=Cutout(self.imageSprite0_l,cutX0,cutY0,quantityX0,quantityY0)
		#Mega Man X - Zero1.
		self.imageSprite1_r=pygame.image.load("images/zero1_r.png")
		self.imageSprite1_l=pygame.image.load("images/zero1_l.png")
		self.matrix1_r=Cutout(self.imageSprite1_r,cutX0,cutY0,quantityX0,quantityY0)
		self.matrix1_l=Cutout(self.imageSprite1_l,cutX0,cutY0,quantityX0,quantityY0)
		#Mega Man X - Zero Saber
		self.imageSprite2_r=pygame.image.load("images/zeros_r.png")
		self.imageSprite2_l=pygame.image.load("images/zeros_l.png")
		imageWidth2=self.imageSprite2_r.get_rect()[2]
		imageHeight2=self.imageSprite2_r.get_rect()[3]
		quantityX2=13
		quantityY2=4
		cutX2=imageWidth2/quantityX2
		cutY2=imageHeight2/quantityY2
		self.matrix2_r=Cutout(self.imageSprite2_r,cutX2,cutY2,quantityX2,quantityY2)
		self.matrix2_l=Cutout(self.imageSprite2_l,cutX2,cutY2,quantityX2,quantityY2)
		#Main Matrix
		self.matrix_r=[self.matrix0_r,self.matrix1_r,self.matrix2_r]
		self.matrix_l=[self.matrix0_l,self.matrix1_l,self.matrix2_l]
		self.matrix=[self.matrix_r,self.matrix_l]
		#Characteristics
		self.soundBuster=pygame.mixer.Sound("sounds/buster.wav")
		self.image=self.matrix[0][0][0][0]
		self.rect=self.image.get_rect()
		self.rect.x=70
		self.rect.y=HEIGHT-200
		self.action=0
		self.i=0
		self.j=0
		self.direction=0
		self.vel_posX=0
		#Variables Buster
		self.buster=0
		self.charge=0
		self.organize=True
		self.loadBuster=LoadBuster()

	def update(self):
		#Logica
		if not self.organize:
			if self.direction==0:
				self.rect.top+=10
				self.rect.left+=10
			else:
				self.rect.top+=10
				self.rect.left+=23
			self.organize=True

		self.j+=1
		if self.j>1:
			self.j=0

		if self.buster>2:
			if self.direction==0:
				self.loadBuster.rect.x=self.rect.x
				self.loadBuster.rect.y=self.rect.y+15
			else:
				self.loadBuster.rect.x=self.rect.x+15
				self.loadBuster.rect.y=self.rect.y+15
			busters.add(self.loadBuster)
		else:
			busters.remove(self.loadBuster)

		self.buster+=self.charge
		self.rect.x+=self.vel_posX
		#Actions
		if self.action==0:
			if self.buster>5:
				self.image=self.matrix[self.direction][self.j][1][self.i]
			else:
				self.image=self.matrix[self.direction][0][1][self.i]
			self.i+=1
			if self.i>1:
				self.i=0

		if self.action==1:
			self.image=self.matrix[self.direction][0][2][0]
			buster=Buster()
			buster.direction=self.direction
			if self.buster>5 and self.buster<15:
				buster.action=5
				if self.direction==0:
					buster.rect.x=self.rect.x+15
					buster.rect.y=self.rect.y+20
					buster.vel_posX=20
				else:
					buster.rect.x=self.rect.x+5
					buster.rect.y=self.rect.y+20
					buster.vel_posX=-20
			elif self.buster>15:
				buster.action=4
				if self.direction==0:
					buster.rect.x=self.rect.x+30
					buster.rect.y=self.rect.y+20
					buster.vel_posX=20
				else:
					buster.rect.x=self.rect.x-10
					buster.rect.y=self.rect.y+20
					buster.vel_posX=-20
			else:
				self.soundBuster.play()
				buster.action=0
				if self.direction==0:
					buster.rect.x=self.rect.x+2
					buster.rect.y=self.rect.y+20
					buster.vel_posX=20
				else:
					buster.rect.x=self.rect.x+45
					buster.rect.y=self.rect.y+20
					buster.vel_posX=-20
			busters.add(buster)
			self.buster=0
			self.i=0
			self.action=0
			self.loadBuster.i=0
			self.loadBuster.action=0

		if self.action==2:
			if self.organize:
				if self.direction==0:
					self.rect.top-=10
					self.rect.left-=10
				else:
					self.rect.top-=10
					self.rect.left-=23
				self.organize=False
			self.image=self.matrix[self.direction][2][0][self.i]
			self.i+=1
			if self.i>12:
				self.i=0
				self.action=0
				self.buster=0

		if self.action==3:
			if self.buster>5:
				self.image=self.matrix[self.direction][self.j][3][self.i]
			else:
				self.image=self.matrix[self.direction][0][3][self.i]
			self.i+=1
			if self.i>10:
				self.i=1

		if self.action==4:
			if self.buster>5:
				self.image=self.matrix[self.direction][self.j][4][self.i]
			else:
				self.image=self.matrix[self.direction][0][4][self.i]
			self.i+=1
			if self.i>8:
				self.i=0
				self.action=0			

class Buster(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.imageSprite_r=pygame.image.load("images/buster_r.png")
		self.imageSprite_l=pygame.image.load("images/buster_l.png")
		imageWidth=self.imageSprite_r.get_rect()[2]
		imageHeight=self.imageSprite_r.get_rect()[3]
		quantityX=8
		quantityY=10
		cutX=imageWidth/quantityX
		cutY=imageHeight/quantityY
		self.matrix_r=Cutout(self.imageSprite_r,cutX,cutY,quantityX,quantityY)
		self.matrix_l=Cutout(self.imageSprite_l,cutX,cutY,quantityX,quantityY)
		self.matrix=[self.matrix_r,self.matrix_l]
		self.image=self.matrix[0][0][0]
		self.rect=self.image.get_rect()
		self.action=0
		self.i=0
		self.vel_posX=0
		self.direction=0

	def update(self):
		self.rect.x+=self.vel_posX
		if self.action==0:
			self.image=self.matrix[self.direction][0][0]
		if self.action==1:
			self.image=self.matrix[self.direction][2][self.i]
			self.i+=1
			if self.i>7:
				self.i=0
		if self.action==2:
			self.image=self.matrix[self.direction][5][self.i]
			self.i+=1
			if self.i>4:
				self.i=0
		if self.action==3:
			self.image=self.matrix[self.direction][3][self.i]
			self.i+=1
			if self.i>4:
				self.i=0
		if self.action==4:
			self.image=self.matrix[self.direction][6][self.i]
			self.i+=1
			if self.i>3:
				self.i=0
		if self.action==5:
			self.image=self.matrix[self.direction][8][self.i]
			self.i+=1
			if self.i>4:
				self.i=0

class LoadBuster(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.imageSprite=pygame.image.load("images/loadb.png")
		imageWidth=self.imageSprite.get_rect()[2]
		imageHeight=self.imageSprite.get_rect()[3]
		quantityX=17
		quantityY=4
		cutX=imageWidth/quantityX
		cutY=imageHeight/quantityY
		self.matrix=Cutout(self.imageSprite,cutX,cutY,quantityX,quantityY)
		self.image=self.matrix[0][0]
		self.rect=self.image.get_rect()
		self.rect.x=72
		self.rect.y=HEIGHT-100
		self.action=0
		self.i=0

	def update(self):
		if self.action==0:
			self.image=self.matrix[0][self.i]
			self.i+=1
			if self.i>15:
				self.i=0
				self.action=1
		if self.action==1:
			self.image=self.matrix[1][self.i]
			self.i+=1
			if self.i>15:
				self.i=0
				self.action=1
		if self.action==2:
			self.image=self.matrix[2][self.i]
			self.i+=1
			if self.i>16:
				self.i=0
				self.action=3
		if self.action==3:
			self.image=self.matrix[3][self.i]
			self.i+=1
			if self.i>16:
				self.i=0
				self.action=0

def Cutout(imageSprite,cutX,cutY,quantityX,quantityY):
	matrix=[]
	for y in range(quantityY):
		matrix.append([])
		for x in range(quantityX):
			picture=imageSprite.subsurface((x*cutX),(y*cutY),cutX,cutY)
			matrix[y].append(picture)
	return matrix

def main():
	#Inicializacion
	global vel_posX,posX
	pygame.init()
	pantalla=pygame.display.set_mode((SIZE))
	pygame.display.set_caption("Mega Man X")
	icon=pygame.image.load("images/icon.png")
	pygame.display.set_icon(icon)
	#Jugador Mega Man X - X or Zero
	#jugador=X()
	jugador=Zero()
	jugadores.add(jugador)
	#Reloj
	reloj=pygame.time.Clock()
    #Ciclo del juego
	while True:
		for evento in pygame.event.get():
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()
			if evento.type == KEYDOWN:
				if evento.key == K_LEFT:
					jugador.i=0
					jugador.direction=1
					jugador.action=3
					jugador.vel_posX=-5
				if evento.key == K_RIGHT:
					jugador.i=0
					jugador.direction=0
					jugador.action=3
					jugador.vel_posX=5
				if evento.key == K_UP:
					jugador.i=0
					jugador.action=4
				if evento.key == K_SPACE:
					jugador.i=0
					jugador.action=1
					jugador.charge=1
				if evento.key == K_z:
					jugador.i=0
					jugador.action=2
			if evento.type == KEYUP:
				if evento.key == K_SPACE:
					jugador.charge=0
					if jugador.buster>5:
						jugador.i=0
						jugador.action=1
				if evento.key == K_RIGHT or evento.key == K_LEFT:
					jugador.i=0
					jugador.action=0
					jugador.vel_posX=0	
					
		#Actualizacion
		pantalla.fill(NEGRO)
		jugadores.update()
		jugadores.draw(pantalla)
		busters.update()
		busters.draw(pantalla)
		pygame.display.flip()
		reloj.tick(20)

if __name__ == "__main__":
	main()
