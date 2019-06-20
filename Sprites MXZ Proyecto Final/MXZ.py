#Modulos
import pygame, sys, random, json
from pygame.locals import *

with open ('maps/mapa01.json') as archivo:
    base1 = json.load(archivo)

with open ('maps/mapa02.json') as archivo:
    base2 = json.load(archivo)

with open ('maps/mapa03.json') as archivo:
    base3 = json.load(archivo)           

#Constantes.
SIZE=WIDTH,HEIGHT=512,320
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
saluds=pygame.sprite.Group()
map01=pygame.sprite.Group()
map02=pygame.sprite.Group()
map03=pygame.sprite.Group()
enemigos=pygame.sprite.Group()
balasE=pygame.sprite.Group()

mundo01=True
mundo02=False
mundo03=False

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
		self.soundBuster1=pygame.mixer.Sound("sounds/buster1.wav")
		self.soundBuster2=pygame.mixer.Sound("sounds/buster2.wav")
		self.soundSaber=pygame.mixer.Sound("sounds/saber.wav")
		self.image=self.matrix[0][0][0][0]
		self.rect=self.image.get_rect()
		self.rect.inflate_ip(-10,0)
		self.rect.x=50
		self.rect.y=190
		self.action=0
		self.i=0
		self.j=0
		self.k=0
		self.direction=0
		self.vel_posX=0
		self.vel_posY=0
		#Variables Buster
		self.buster=0
		self.charge=0
		self.organize=True
		self.loadBuster=LoadBuster()
		self.gravity=0.7
		self.salto=False
		self.floorcollide=True
		self.block=False
		self.salud=150		

	def gravedad(self):
		if self.vel_posY == 0:
			self.vel_posY=1
		else:
			self.vel_posY+=self.gravity	

	def update(self):
		global mundo01,mundo02,mundo03
		#Logica
		keyState=pygame.key.get_pressed()
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
		self.rect.y+=self.vel_posY
		self.gravedad()
		if mundo01:
			ls_col=pygame.sprite.spritecollide(self,map01,False)
			for p in ls_col:
				if self.rect.y >= (p.rect.top-self.rect.height):
					self.vel_posY=0
					self.rect.y=p.rect.top-self.rect.height
					self.floorcollide=True
					if self.k == 3:
						self.k=0
						if keyState[K_LEFT] or keyState[K_RIGHT]:
							self.action=3
						else:		
							self.action=0
		if mundo02:					
			ls_col=pygame.sprite.spritecollide(self,map02,False)
			for p in ls_col:
				if self.rect.y >= (p.rect.top-self.rect.height):
					self.vel_posY=0
					self.rect.y=p.rect.top-self.rect.height
					self.floorcollide=True
					if self.k == 3:
						self.k=0
						if keyState[K_LEFT] or keyState[K_RIGHT]:
							self.action=3
						else:		
							self.action=0
		if mundo03:					
			ls_col=pygame.sprite.spritecollide(self,map03,False)
			for p in ls_col:
				if self.rect.y >= (p.rect.top-self.rect.height):
					self.vel_posY=0
					self.rect.y=p.rect.top-self.rect.height
					self.floorcollide=True
					if self.k == 3:
						self.k=0
						if keyState[K_LEFT] or keyState[K_RIGHT]:
							self.action=3
						else:		
							self.action=0									
	
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
					self.soundBuster1.play()
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
					self.soundBuster2.play()
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
				if keyState[K_LEFT] or keyState[K_RIGHT]:
					self.action=3
				else:		
					self.action=0

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
				self.soundSaber.play()
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
				self.image=self.matrix[self.direction][self.j][5][self.k]
			else:
				self.image=self.matrix[self.direction][0][5][self.k]
			self.k+=1
			if self.k>2:
				self.k=3
					
		if keyState[K_LEFT] or keyState[K_RIGHT]:
			self.block=True
		else:		
			self.block=False

		if mundo01:	
			ls_col=pygame.sprite.spritecollide(self,map01,False)
			for p in ls_col:
				
				if (self.rect.right >= p.rect.left) and (self.vel_posX > 0):
					self.rect.right = p.rect.left
					self.vel_posX=0

				if (self.rect.left <= p.rect.right) and (self.vel_posX < 0):
					self.rect.left = p.rect.right
					self.vel_posX=0			

				if (self.rect.bottom >= p.rect.top) and (self.vel_posY > 0):
					self.rect.bottom = p.rect.top
					self.vel_posY=0
					
				if (self.rect.top < p.rect.bottom) and (self.vel_posY < 0):
					self.rect.top = p.rect.bottom
					self.vel_posY=0

		if mundo02:			
			ls_col=pygame.sprite.spritecollide(self,map02,False)
			for p in ls_col:

				if (self.rect.right >= p.rect.left) and (self.vel_posX > 0):
					self.rect.right = p.rect.left
					self.vel_posX=0
					
				if (self.rect.left <= p.rect.right) and (self.vel_posX < 0):
					self.rect.left = p.rect.right
					self.vel_posX=0	

				if (self.rect.bottom >= p.rect.top) and (self.vel_posY > 0):
					self.rect.bottom = p.rect.top
					self.vel_posY=0
						
				if (self.rect.top < p.rect.bottom) and (self.vel_posY < 0):
					self.rect.top = p.rect.bottom
					self.vel_posY=0

		if mundo03:			
			ls_col=pygame.sprite.spritecollide(self,map03,False)
			for p in ls_col:

				if (self.rect.right >= p.rect.left) and (self.vel_posX > 0):
					self.rect.right = p.rect.left
					self.vel_posX=0
					
				if (self.rect.left <= p.rect.right) and (self.vel_posX < 0):
					self.rect.left = p.rect.right
					self.vel_posX=0	

				if (self.rect.bottom >= p.rect.top) and (self.vel_posY > 0):
					self.rect.bottom = p.rect.top
					self.vel_posY=0
						
				if (self.rect.top < p.rect.bottom) and (self.vel_posY < 0):
					self.rect.top = p.rect.bottom
					self.vel_posY=0								

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
		self.soundBuster1=pygame.mixer.Sound("sounds/buster1.wav")
		self.soundBuster2=pygame.mixer.Sound("sounds/buster2.wav")
		self.soundSaber=pygame.mixer.Sound("sounds/saber.wav")
		self.image=self.matrix[0][0][0][0]
		self.rect=self.image.get_rect()
		self.rect.inflate_ip(-13,0)
		self.rect.x=50
		self.rect.y=170
		self.action=0
		self.i=0
		self.j=0
		self.k=0
		self.direction=0
		self.vel_posX=0
		self.vel_posY=0
		#Variables Buster
		self.buster=0
		self.charge=0
		self.organize=True
		self.loadBuster=LoadBuster()
		self.gravity=0.7
		self.salto=False
		self.floorcollide=True
		self.block=False
		self.salud=150	

	def gravedad(self):
		if self.vel_posY == 0:
			self.vel_posY=1
		else:
			self.vel_posY+=self.gravity	

	def update(self):
		global mundo01,mundo02,mundo03
		#Logica
		keyState=pygame.key.get_pressed()
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
		self.rect.y+=self.vel_posY
		self.gravedad()
		if mundo01:
			ls_col=pygame.sprite.spritecollide(self,map01,False)
			for p in ls_col:
				if self.rect.y >= (p.rect.top-self.rect.height):
					self.vel_posY=0
					self.rect.y=p.rect.top-self.rect.height
					self.floorcollide=True
					if self.k==5:
						self.k=0
						if keyState[K_LEFT] or keyState[K_RIGHT]:
							self.action=3
						else:		
							self.action=0

		if mundo02:					
			ls_col=pygame.sprite.spritecollide(self,map02,False)
			for p in ls_col:
				if self.rect.y >= (p.rect.top-self.rect.height):
					self.vel_posY=0
					self.rect.y=p.rect.top-self.rect.height
					self.floorcollide=True
					if self.k==5:
						self.k=0
						if keyState[K_LEFT] or keyState[K_RIGHT]:
							self.action=3
						else:		
							self.action=0

		if mundo03:					
			ls_col=pygame.sprite.spritecollide(self,map03,False)
			for p in ls_col:
				if self.rect.y >= (p.rect.top-self.rect.height):
					self.vel_posY=0
					self.rect.y=p.rect.top-self.rect.height
					self.floorcollide=True
					if self.k==5:
						self.k=0
						if keyState[K_LEFT] or keyState[K_RIGHT]:
							self.action=3
						else:		
							self.action=0									

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
				self.soundBuster1.play()
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
				self.soundBuster2.play()
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
			if keyState[K_LEFT] or keyState[K_RIGHT]:
				self.action=3
			else:		
				self.action=0
		
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
				self.soundSaber.play()
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
				self.image=self.matrix[self.direction][self.j][4][self.k]
			else:
				self.image=self.matrix[self.direction][0][4][self.k]
			self.k+=1
			if self.k>4:
				self.k=5
							
		if keyState[K_LEFT] or keyState[K_RIGHT]:
			self.block=True
		else:		
			self.block=False

		if mundo01:	
			ls_col=pygame.sprite.spritecollide(self,map01,False)
			for p in ls_col:

				if (self.rect.right >= p.rect.left) and (self.vel_posX > 0):
					self.rect.right = p.rect.left
					self.vel_posX=0
					
				if (self.rect.left <= p.rect.right) and (self.vel_posX < 0):
					self.rect.left = p.rect.right
					self.vel_posX=0	

				if (self.rect.bottom >= p.rect.top) and (self.vel_posY > 0):
					self.rect.bottom = p.rect.top
					self.vel_posY=0
						
				if (self.rect.top < p.rect.bottom) and (self.vel_posY < 0):
					self.rect.top = p.rect.bottom
					self.vel_posY=0

		if mundo02:			
			ls_col=pygame.sprite.spritecollide(self,map02,False)
			for p in ls_col:

				if (self.rect.right >= p.rect.left) and (self.vel_posX > 0):
					self.rect.right = p.rect.left
					self.vel_posX=0
					
				if (self.rect.left <= p.rect.right) and (self.vel_posX < 0):
					self.rect.left = p.rect.right
					self.vel_posX=0	

				if (self.rect.bottom >= p.rect.top) and (self.vel_posY > 0):
					self.rect.bottom = p.rect.top
					self.vel_posY=0
						
				if (self.rect.top < p.rect.bottom) and (self.vel_posY < 0):
					self.rect.top = p.rect.bottom
					self.vel_posY=0

		if mundo03:			
			ls_col=pygame.sprite.spritecollide(self,map03,False)
			for p in ls_col:

				if (self.rect.right >= p.rect.left) and (self.vel_posX > 0):
					self.rect.right = p.rect.left
					self.vel_posX=0
					
				if (self.rect.left <= p.rect.right) and (self.vel_posX < 0):
					self.rect.left = p.rect.right
					self.vel_posX=0	

				if (self.rect.bottom >= p.rect.top) and (self.vel_posY > 0):
					self.rect.bottom = p.rect.top
					self.vel_posY=0
						
				if (self.rect.top < p.rect.bottom) and (self.vel_posY < 0):
					self.rect.top = p.rect.bottom
					self.vel_posY=0																		

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

class Salud(pygame.sprite.Sprite):
    def __init__(self,alto=10,x=50,y=11):
        pygame.sprite.Sprite.__init__(self)
        self.alto=alto
        self.image=pygame.Surface([150,self.alto])
        self.color=VERDE
        self.image.fill(self.color)
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y

    def actualizar(self,salud,x=50,y=11):
        self.image=pygame.Surface([salud,self.alto])
        self.image.fill(self.color)
        self.rect.x=x
        self.rect.y=y
 
class Sigma(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		#Mega Man X - Sigma
		self.imageSprite0=pygame.image.load("images/sigma.png")
		imageWidth0=self.imageSprite0.get_rect()[2]
		imageHeight0=self.imageSprite0.get_rect()[3]
		quantityX0=10
		quantityY0=13
		cutX0=imageWidth0/quantityX0
		cutY0=imageHeight0/quantityY0
		self.matrix=Cutout(self.imageSprite0,cutX0,cutY0,quantityX0,quantityY0)
		self.image=self.matrix[0][0]
		self.rect=self.image.get_rect()
		self.rect.x=300
		self.rect.y=200
		self.action=0
		self.i=0
		self.vel_posX=0
		self.vel_posY=0
		self.radius=100   
		self.temp=random.randrange(50)

	def update(self):
		#Logica
		self.rect.x+=self.vel_posX
		self.rect.y+=self.vel_posY
		#Actions
		if self.action==0:
			self.image=self.matrix[0][0]
			self.i+=1
			if self.i>1:
				self.i=0

		if self.action==1:
			self.image=self.matrix[1][self.i]
			self.i+=1
			if self.i>3:
				self.i=0
				self.action=0

		if self.action==2:
			self.image=self.matrix[2][self.i]
			self.i+=1
			if self.i>3:
				self.i=0
				self.action=0

		if self.action==3:
			self.image=self.matrix[3][self.i]
			self.i+=1
			if self.i>6:
				self.i=0
				self.action=0

		if self.action==4:
			self.image=self.matrix[4][self.i]
			self.i+=1
			if self.i>4:
				self.i=0
				self.action=0

		if self.action==5:
			self.image=self.matrix[5][self.i]
			self.i+=1
			if self.i>4:
				self.i=0
				self.action=0

		if self.action==6:
			self.image=self.matrix[2][self.i]
			self.i+=1
			if self.i>3:
				self.i=0
				self.action=0

class Dopler(pygame.sprite.Sprite):
	def __init__(self,x,y,n):
		pygame.sprite.Sprite.__init__(self)
		#Mega Man X - XG411
		self.imageSprite0=pygame.image.load("images/dopler.png")
		imageWidth0=self.imageSprite0.get_rect()[2]
		imageHeight0=self.imageSprite0.get_rect()[3]
		quantityX0=8
		quantityY0=2
		cutX0=imageWidth0/quantityX0
		cutY0=imageHeight0/quantityY0
		self.matrix=Cutout(self.imageSprite0,cutX0,cutY0,quantityX0,quantityY0)
		self.image=self.matrix[0][0]
		self.rect=self.image.get_rect()
		self.rect.x=x
		self.rect.y=y
		self.action=0
		self.xini=x
		self.posx_fondo=0
		self.n=n
		self.radius=100   
		self.temp=random.randrange(50)

	def update(self):
		#Logica
		self.rect.x = self.posx_fondo + self.xini
		#Actions
		if self.action==0:
			self.image=self.matrix[0][0]
		if self.action==1:
			self.image=self.matrix[0][0]	

class ZR12(pygame.sprite.Sprite):
	def __init__(self,x,y,n):
		pygame.sprite.Sprite.__init__(self)
		#Mega Man X - ZR12
		self.imageSprite0=pygame.image.load("images/zr12.png")
		imageWidth0=self.imageSprite0.get_rect()[2]
		imageHeight0=self.imageSprite0.get_rect()[3]
		quantityX0=7
		quantityY0=6
		cutX0=imageWidth0/quantityX0
		cutY0=imageHeight0/quantityY0
		self.matrix=Cutout(self.imageSprite0,cutX0,cutY0,quantityX0,quantityY0)
		self.image=self.matrix[0][0]
		self.rect=self.image.get_rect()
		self.rect.x=x
		self.rect.y=y
		self.action=0
		self.i=0
		self.xini=x
		self.posx_fondo=0
		self.n=n
		self.radius=100   
		self.temp=50
		self.salud=150

	def update(self):
		#Logica
		self.rect.x = self.posx_fondo + self.xini
		self.temp-=1
		#Actions
		if self.action==0:
			self.image=self.matrix[0][0]

		if self.action==1:
			self.image=self.matrix[2][self.i]
			self.i+=1
			if self.i>5:
				self.i=0
				self.action=0

class XG411(pygame.sprite.Sprite):
	def __init__(self,x,y,n):
		pygame.sprite.Sprite.__init__(self)
		#Mega Man X - XG411
		self.imageSprite0=pygame.image.load("images/xg411.png")
		imageWidth0=self.imageSprite0.get_rect()[2]
		imageHeight0=self.imageSprite0.get_rect()[3]
		quantityX0=4
		quantityY0=4
		cutX0=imageWidth0/quantityX0
		cutY0=imageHeight0/quantityY0
		self.matrix=Cutout(self.imageSprite0,cutX0,cutY0,quantityX0,quantityY0)
		self.image=self.matrix[0][0]
		self.rect=self.image.get_rect()
		self.rect.x=x
		self.rect.y=y
		self.action=0
		self.i=0
		self.xini=x
		self.posx_fondo=0
		self.n=n
		self.radius=100   
		self.temp=60
		self.salud=150

	def update(self):
		#Logica
		self.rect.x = self.posx_fondo + self.xini
		self.temp-=1
		#Actions
		if self.action==0:
			self.image=self.matrix[1][0]

		if self.action==1:
			self.image=self.matrix[0][self.i]
			self.i+=1
			if self.i>3:
				self.i=0
				self.action=0

class Spark13(pygame.sprite.Sprite):
	def __init__(self,x,y,n):
		pygame.sprite.Sprite.__init__(self)
		#Mega Man X - Spark13
		self.imageSprite0=pygame.image.load("images/spark13.png")
		imageWidth0=self.imageSprite0.get_rect()[2]
		imageHeight0=self.imageSprite0.get_rect()[3]
		quantityX0=4
		quantityY0=4
		cutX0=imageWidth0/quantityX0
		cutY0=imageHeight0/quantityY0
		self.matrix=Cutout(self.imageSprite0,cutX0,cutY0,quantityX0,quantityY0)
		self.image=self.matrix[0][0]
		self.rect=self.image.get_rect()
		self.rect.x=x
		self.rect.y=y
		self.action=0
		self.i=0
		self.xini=x
		self.posx_fondo=0
		self.n=n
		self.radius=100   
		self.temp=40
		self.salud=150

	def update(self):
		#Logica
		self.rect.x = self.posx_fondo + self.xini
		self.temp-=1
		#Actions
		if self.action==0:
			self.image=self.matrix[0][0]

		if self.action==1:
			self.image=self.matrix[1][self.i]
			self.i+=1
			if self.i>3:
				self.i=0
				self.action=0

class XG900(pygame.sprite.Sprite):
	def __init__(self,x,y,n):
		pygame.sprite.Sprite.__init__(self)
		#Mega Man X - Spark13
		self.imageSprite0=pygame.image.load("images/xg900.png")
		imageWidth0=self.imageSprite0.get_rect()[2]
		imageHeight0=self.imageSprite0.get_rect()[3]
		quantityX0=4
		quantityY0=5
		cutX0=imageWidth0/quantityX0
		cutY0=imageHeight0/quantityY0
		self.matrix=Cutout(self.imageSprite0,cutX0,cutY0,quantityX0,quantityY0)
		self.image=self.matrix[0][0]
		self.rect=self.image.get_rect()
		self.rect.x=x
		self.rect.y=y
		self.action=0
		self.i=0
		self.xini=x
		self.posx_fondo=0
		self.n=n
		self.radius=100   
		self.temp=50
		self.salud=200

	def update(self):
		#Logica
		self.rect.x = self.posx_fondo + self.xini
		self.temp-=1
		#Actions
		if self.action==0:
			self.image=self.matrix[2][0]

		if self.action==1:
			self.image=self.matrix[0][self.i]
			self.i+=1
			if self.i>3:
				self.i=0
				self.action=0

class BalasE(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load("images/bzr12.png")
		self.rect=self.image.get_rect()
		self.action=0
		self.i=0
		self.vel_posX=-5

	def update(self):
		self.rect.x+=self.vel_posX
		
class Mapa01(pygame.sprite.Sprite):
	def __init__(self,image,posXY,e):
		pygame.sprite.Sprite.__init__(self)
		self.image=image
		self.rect=self.image.get_rect()
		self.rect.x=posXY[0]
		self.rect.y=posXY[1]
		self.type=e
		self.xini=posXY[0]
		self.posx_fondo=0

	def update(self):
		self.rect.x = self.posx_fondo + self.xini					

class Mapa02(pygame.sprite.Sprite):
	def __init__(self,image,posXY,e):
		pygame.sprite.Sprite.__init__(self)
		self.image=image
		self.rect=self.image.get_rect()
		self.rect.x=posXY[0]
		self.rect.y=posXY[1]
		self.type=e
		self.xini=posXY[0]
		self.posx_fondo=0

	def update(self):
		self.rect.x = self.posx_fondo + self.xini

class Mapa03(pygame.sprite.Sprite):
	def __init__(self,image,posXY,e):
		pygame.sprite.Sprite.__init__(self)
		self.image=image
		self.rect=self.image.get_rect()
		self.rect.x=posXY[0]
		self.rect.y=posXY[1]
		self.type=e
		self.xini=posXY[0]
		self.posx_fondo=0

	def update(self):
		self.rect.x = self.posx_fondo + self.xini		

def Map01(pantalla):
	mapa = base1['layers'][0]['data']
	mapeo=[]
	for j in range(20):
		fila=[]
		for i in range(200):
			fila.append(mapa[i+(j*200)])
		mapeo.append(fila)

	imageSprite=pygame.image.load("maps/mapa01.png")
	imageWidth=imageSprite.get_rect()[2]
	imageHeight=imageSprite.get_rect()[3]
	cantidadX=25
	cantidadY=30
	corteX=imageWidth/cantidadX
	corteY=imageHeight/cantidadY
	m=Cutout(imageSprite,corteX,corteY,cantidadX,cantidadY)
	i=0
	for a in range (len(mapeo)):
		for e in mapeo[a]:
			c=e-1
			if (not(c < 0)):
				posXY=[(c/25),(c%25)]
				m01=Mapa01(m[int(posXY[0])][int(posXY[1])],[i*corteX,a*corteY],e)
				map01.add(m01)	
			i+=1
		i=0	

def enemigos1():
	e1=ZR12(194,163,1)
	e2=XG411(648,113,1)
	e3=ZR12(350,163,1)
	e4=ZR12(974,195,1)
	e5=XG411(1167,193,1)
	e6=XG411(1320,193,1)
	e7=ZR12(1644,163,1)
	e8=XG411(1860,113,1)
	e9=ZR12(2392,163,1)
	e10=ZR12(2664,163,1)
	e11=XG411(2788,161,1)
	e12=ZR12(2950,179,1)
	e13=XG411(3100,161,1)
	enemigos.add(e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13)

def Map02(pantalla):
	mapa = base2['layers'][0]['data']
	mapeo=[]
	for j in range(20):
		fila=[]
		for i in range(150):
			fila.append(mapa[i+(j*150)])
		mapeo.append(fila)

	imageSprite=pygame.image.load("maps/mapa02.png")
	imageWidth=imageSprite.get_rect()[2]
	imageHeight=imageSprite.get_rect()[3]
	cantidadX=12
	cantidadY=12
	corteX=imageWidth/cantidadX
	corteY=imageHeight/cantidadY
	m=Cutout(imageSprite,corteX,corteY,cantidadX,cantidadY)
	i=0
	for a in range (len(mapeo)):
		for e in mapeo[a]:
			c=e-1
			if (not(c < 0)):
				posXY=[(c/12),(c%12)]
				m02=Mapa02(m[int(posXY[0])][int(posXY[1])],[i*corteX,a*corteY],e)
				map02.add(m02)	
			i+=1
		i=0

def enemigos2():
	e1=Spark13(202,180,2)
	e2=XG411(332,177,2)
	e3=Spark13(665,164,2)
	e4=XG411(800,145,2)
	e5=Spark13(1070,180,2)
	e6=Spark13(1294,148,2)
	e7=Spark13(1870,148,2)
	e8=XG900(2090,230,2)
	e9=XG900(2230,230,2)
	e10=Dopler(2190,230,2)
	enemigos.add(e1,e2,e3,e4,e5,e6,e7,e8,e9,e10)

def Map03(pantalla):
	mapa = base3['layers'][0]['data']
	mapeo=[]
	for j in range(11):
		fila=[]
		for i in range(17):
			fila.append(mapa[i+(j*17)])
		mapeo.append(fila)

	imageSprite=pygame.image.load("maps/mapa03.png")
	imageWidth=imageSprite.get_rect()[2]
	imageHeight=imageSprite.get_rect()[3]
	cantidadX=7
	cantidadY=5
	corteX=imageWidth/cantidadX
	corteY=imageHeight/cantidadY
	m=Cutout(imageSprite,corteX,corteY,cantidadX,cantidadY)
	i=0
	for a in range (len(mapeo)):
		for e in mapeo[a]:
			c=e-1
			if (not(c < 0)):
				posXY=[(c/7),(c%7)]
				m03=Mapa03(m[int(posXY[0])][int(posXY[1])],[i*corteX,a*corteY],e)
				map03.add(m03)	
			i+=1
		i=0									

def Cutout(imageSprite,cutX,cutY,quantityX,quantityY):
	matrix=[]
	for y in range(quantityY):
		matrix.append([])
		for x in range(quantityX):
			picture=imageSprite.subsurface((x*cutX),(y*cutY),cutX,cutY)
			matrix[y].append(picture)
	return matrix

def RecorteX():
	imageSprite0_r=pygame.image.load("images/x_r.png")	
	imageWidth0=imageSprite0_r.get_rect()[2]
	imageHeight0=imageSprite0_r.get_rect()[3]
	quantityX0=11
	quantityY0=19
	cutX0=imageWidth0/quantityX0
	cutY0=imageHeight0/quantityY0
	matrix0_r=Cutout(imageSprite0_r,cutX0,cutY0,quantityX0,quantityY0)
	return matrix0_r

def RecorteZero():
	imageSprite0_r=pygame.image.load("images/zero_r.png")
	imageWidth0=imageSprite0_r.get_rect()[2]
	imageHeight0=imageSprite0_r.get_rect()[3]
	quantityX0=11
	quantityY0=15
	cutX0=imageWidth0/quantityX0
	cutY0=imageHeight0/quantityY0
	matrix0_r=Cutout(imageSprite0_r,cutX0,cutY0,quantityX0,quantityY0)
	return matrix0_r			

def main():
	global mundo01,mundo02,mundo03
	#Inicializacion
	pygame.init()
	pantalla=pygame.display.set_mode((SIZE))
	pygame.display.set_caption("Mega Man X-Reborn")
	icon=pygame.image.load("images/icon.png")
	pygame.display.set_icon(icon)
	selector=pygame.image.load("images/selector.png")
	selector2=pygame.image.load("images/selector2.png")
	imageMenu=pygame.image.load("images/fondomenu.png")
	imageTurorial=pygame.image.load("images/fondotutorial.png")
	imagePause=pygame.image.load("images/pause.png")
	imageFondo1=pygame.image.load("maps/fondomapa01.png")
	imageFondo2=pygame.image.load("maps/fondomapa02.png")
	imageFondo3=pygame.image.load("maps/fondomapa03.png")
	imageVideo=pygame.image.load("images/video.png")
	imageLoading=pygame.image.load("images/loading.png")
	imageSelector=pygame.image.load("images/selection.png")
	imageFondoPrevius=[imageMenu,imageTurorial,imageVideo,imageSelector]
	imageFondo=[imagePause,imageFondo1,imageFondo2,imageFondo3]
	telonNegro=pygame.Surface([512,32])
	telonNegro.fill(NEGRO)
	telonRojo=pygame.Surface([150,10])
	telonRojo.fill(ROJO)
	titlex=pygame.image.load("images/titlex.png")
	titlezero=pygame.image.load("images/titlezero.png")
	titlel1=pygame.image.load("images/titlel1.png")
	titlel2=pygame.image.load("images/titlel2.png")
	titlefl=pygame.image.load("images/titlefl.png")
	imageWin=pygame.image.load("images/mision.png")
	imageLoss=pygame.image.load("images/gameover.png")
	menu=pygame.mixer.Sound("sounds/menu.wav")
	menu.set_volume(0.4)
	menu2=pygame.mixer.Sound("sounds/menu2.wav")
	menu3=pygame.mixer.Sound("sounds/menu3.wav")
	mundo1=pygame.mixer.Sound("sounds/mundo1.wav")
	mundo1.set_volume(0.4)
	mundo2=pygame.mixer.Sound("sounds/mundo2.wav")
	mundo2.set_volume(0.4)
	mundo3=pygame.mixer.Sound("sounds/mundo3.wav")
	mundo3.set_volume(0.4)
	muerte=pygame.mixer.Sound("sounds/muerte.wav")
	muerte.set_volume(0.4)
	Map01(pantalla)
	Map02(pantalla)
	Map03(pantalla)
	enemigos1()
	#Jugador Mega Man X - X or Zero
	seleccion=0	
	posFondoX,posFondoY=0,0
	velx=-5
	final=False
	reloj=pygame.time.Clock()
	#Previos
	video=pygame.mixer.Sound("sounds/intro.wav")
	movie=pygame.movie.Movie("videos/intro.mpg")
	finalMovie=int(movie.get_length())
	movie_screen=pygame.Surface(movie.get_size())
	movie.set_display(movie_screen)
	video.set_volume(0.3)
	megaman=RecorteX()
	zero=RecorteZero()
	x,y=155,[130,155,180]
	i,j=0,0
	m,z=13,1
	seguir1=False
	seguir2=False
	seguir3=False
	intro=False
	tutorial=False
	acabar=False
	pause=False
	loading=False
	p=0
	segundos=0
	menu.play()
	while not seguir1:
		for evento in pygame.event.get():
			if evento.type == QUIT:
				movie.stop()
				video.stop()
				pygame.quit()
				sys.exit()
			if evento.type == KEYDOWN:
				menu2.play()
				if evento.key == K_SPACE:
					if i==0:
						intro=True
					elif i==1:
						tutorial=True
					else:
						pygame.quit()
						sys.exit()
				if evento.key == K_ESCAPE:
					tutorial=False
				if evento.key == K_TAB:
					acabar=True	
				if not tutorial:			
					if evento.key == K_DOWN:
						i+=1
						if i>2:
							i=0
					if evento.key == K_UP:
						i-=1
						if i<0:
							i=2	
			if evento.type == KEYUP:
				acabar=False
	
		if tutorial:
			pantalla.blit(imageFondoPrevius[1],(0,0))
			pantalla.blit(megaman[1][0],(250,135))
			pantalla.blit(zero[1][0],(350,115))
		else:
			if intro:
				menu.stop()
				movie.play()	
				video.play()
				segundos=pygame.time.get_ticks()/1000
				pantalla.blit(imageFondoPrevius[2],(0,0))
				pantalla.blit(movie_screen,(90,10))
				if acabar or (segundos>finalMovie):
					segundos=0
					movie.stop()
					video.stop()
					acabar=False
					seguir1=True
			else:	
				pantalla.blit(imageFondoPrevius[0],(0,0))
				pantalla.blit(selector,(x,y[i]))           
		pygame.display.flip()

	bandera=False
	segundos2=0
	i=0
	menu.play()
	while not seguir2:
		for evento in pygame.event.get():
			if evento.type == QUIT:
				menu.stop()
				pygame.quit()
				sys.exit()
			if evento.type == KEYDOWN:
				menu3.play()
				if evento.key == K_SPACE:
					if i==0:
						seleccion=0
					else:
						seleccion=1

					bandera=True
					menu.stop()	
				if evento.key == K_LEFT:
					m,z=13,1
					i-=1
					if i<0:
						i=0
				if evento.key == K_RIGHT:
					m,z=1,11
					i+=1
					if i>1:
						i=1
			
		if bandera:
			pantalla.blit(imageLoading,(0,0))
			segundos2+=1
			if segundos2> 300:
				segundos2=0
				bandera=False
				seguir2=True	
		else:
			pantalla.blit(imageFondoPrevius[3],(0,0))
			pantalla.blit(megaman[m][0],(155,175))
			pantalla.blit(zero[z][1],(280,155))
			if i==0: 
				pantalla.blit(selector2,(120,140))
			else:
				pantalla.blit(selector2,(250,140))          
		pygame.display.flip()				

	if (seleccion == 0):
		jugador=X()
	else:	
		jugador=Zero()

	jugadores.add(jugador)
	salud=Salud()
	saluds.add(salud)
	mundo1.play()
	segundos3=0
	gameover=False
	bloquears=True
	avanzar=False
	termino=False	
    #Ciclo del juego
	while not seguir3:
		for evento in pygame.event.get():
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()
			if evento.type == KEYDOWN:
				if evento.key == K_DELETE:
					if p==1:
						jugadores.empty()
						busters.empty()
						map01.empty()
						map02.empty()
						map03.empty()
						enemigos.empty()
						balasE.empty()
						mundo1.stop()
						mundo2.stop()
						mundo3.stop()
						mundo01=True
						mundo02=False
						mundo03=False
						seguir3=True
				if evento.key == K_ESCAPE:
					if p==0:
						pause=True
						mundo1.set_volume(0.1)
						mundo2.set_volume(0.1)
						mundo3.set_volume(0.1)
						p+=1
					else:
						pause=False
						mundo1.set_volume(0.4)
						mundo2.set_volume(0.4)
						mundo3.set_volume(0.4)
						p-=1		
				if evento.key == K_LEFT:
					if jugador.floorcollide:
						jugador.i=0
						jugador.action=3		
					jugador.direction=1	
					jugador.vel_posX=-5
				if evento.key == K_RIGHT:
					if jugador.floorcollide:
						jugador.i=0
						jugador.action=3
					jugador.direction=0	
					jugador.vel_posX=5
				if jugador.floorcollide:
					if evento.key == K_UP:
						jugador.i=0
						jugador.action=4
						jugador.salto=True
						jugador.floorcollide=False
				if evento.key == K_SPACE:
					if jugador.floorcollide:
						jugador.i=0
						jugador.action=1
						jugador.charge=1
				if not jugador.block:
					if jugador.floorcollide:	
						if evento.key == K_x:
							jugador.i=0
							jugador.action=2
			if evento.type == KEYUP:
				if evento.key == K_SPACE:
					jugador.charge=0
					if jugador.buster>5:
						jugador.i=0
						jugador.action=1
				if evento.key == K_RIGHT or evento.key == K_LEFT:
					if jugador.floorcollide:
						jugador.action=0
						jugador.i=0	
					jugador.vel_posX=0

		#Logica
		salud.actualizar(jugador.salud)
		for b in busters:    
			b_col=pygame.sprite.spritecollide(b,enemigos,True)
			b_col2=pygame.sprite.spritecollide(b,map01,False)
			b_col3=pygame.sprite.spritecollide(b,map02,False) 
			b_col4=pygame.sprite.spritecollide(b,map03,False)   
			for e in b_col: 
				busters.remove(b)
				if isinstance(e,Dopler):
					avanzar=True
				if isinstance(e,Sigma):
					termino=True	
			for e in b_col2: 
				busters.remove(b)
			for e in b_col3: 
				busters.remove(b)
			for e in b_col4: 
				busters.remove(b)		
			if (b.rect.x<0) or (b.rect.x>WIDTH):  
				busters.remove(b)

		for e in enemigos:
			if pygame.sprite.collide_circle(e,jugador):
				if e.temp<=0:
					e.action=1
					if isinstance(e,ZR12):
						balae=BalasE()
						balae.rect.x=e.rect.x
						balae.rect.y=e.rect.y+10
						balae.image=pygame.image.load("images/bzr12.png")
						balasE.add(balae)
						e.temp=50 
					if isinstance(e,XG411):
						balae=BalasE()
						balae.rect.x=e.rect.x
						balae.rect.y=e.rect.y+30
						balae.image=pygame.image.load("images/bxg411.png")
						balasE.add(balae)
						e.temp=60 
					if isinstance(e,Spark13):
						balae=BalasE()
						balae.rect.x=e.rect.x-5
						balae.rect.y=e.rect.y+10
						balae.image=pygame.image.load("images/bspark13.png")
						balasE.add(balae)
						e.temp=40  
					if isinstance(e,XG900):
						balae=BalasE()
						balae.rect.x=e.rect.x
						balae.rect.y=e.rect.y+30
						balae.image=pygame.image.load("images/bxg900.png")
						balasE.add(balae)
						e.temp=50
					if isinstance(e,Sigma):
						balae=BalasE()
						balae.rect.x=e.rect.x
						balae.rect.y=e.rect.y+30
						balae.image=pygame.image.load("images/b2sigma.png")
						balasE.add(balae)
						e.temp=random.randrange(50)	 		 						
				
		for b in balasE:    
			b_col=pygame.sprite.spritecollide(b,jugadores,False)
			b_col2=pygame.sprite.spritecollide(b,map01,False)
			b_col3=pygame.sprite.spritecollide(b,map02,False) 
			b_col4=pygame.sprite.spritecollide(b,map03,False)     
			for e in b_col: 
				balasE.remove(b)
				jugador.salud-=50
				salud.actualizar(jugador.salud)
			for e in b_col2: 
				balasE.remove(b)
			for e in b_col3: 
				balasE.remove(b)
			for e in b_col4: 
				balasE.remove(b)                                                                           
			if (b.rect.y< 0) or (b.rect.bottom>HEIGHT):  
				balasE.remove(b)			  		

		if jugador.salto:
			jugador.vel_posY=-6
			jugador.salto=False

 		if jugador.rect.x<0 and jugador.vel_posX<0.:
			jugador.rect.x=0

		if not mundo03:
			if not final:	
				if jugador.rect.x >= WIDTH-150 and jugador.vel_posX>0.:
					jugador.rect.x=WIDTH-150
					posFondoX+=velx
					#Mapa1
					if mundo01:
						if posFondoX<-2680:	
							velx=0
							final=True
						for m in map01:
							m.posx_fondo=posFondoX
						for e in enemigos:
							e.posx_fondo=posFondoX	
					#Mapa2
					if mundo02:	
						if posFondoX<-1880:
							velx=0
							final=True
						for m in map02:
							m.posx_fondo=posFondoX
						for e in enemigos:
							e.posx_fondo=posFondoX			
			else:	
				if jugador.rect.x>WIDTH-40:
						jugador.rect.x=WIDTH-40

		if jugador.rect.x==WIDTH-50:
			if mundo01:
				for e in enemigos:
					if e.n==1:
						enemigos.remove(e)
				map01.empty()
				balasE.empty()
				mundo1.stop()
				loading=True
				segundos3+=1
				if segundos3>300:
					mundo2.play()
					jugador.rect.x=50
					if isinstance(jugador,X):
						jugador.rect.y=206
					else:
						jugador.rect.y=186
					enemigos2()		
					posFondoX=0
					final=False
					velx=-5
					mundo01=False
					mundo02=True
					mundo03=False
					segundos3=0
					loading=False
					jugador.salud=150 	
		
		if avanzar:			
			if jugador.rect.x==WIDTH-40:		
				if mundo02:
					for e in enemigos:
						if e.n==2:
							enemigos.remove(e)
					map02.empty()
					balasE.empty()
					mundo2.stop()
					loading=True
					segundos3+=1
					if segundos3>300:
						mundo3.play()
						jugador.rect.x=115
						if isinstance(jugador,X):
							jugador.rect.y=229
						else:
							jugador.rect.y=209	
						posFondoX=0
						final=False
						velx=-5
						mundo01=False
						mundo02=False
						mundo03=True
						segundos3=0
						loading=False
						sigma=Sigma()
						enemigos.add(sigma)
						jugador.salud=150 

		if termino:
			if jugador.rect.x>WIDTH-200:		
				if mundo03:
					gameover=True
					jugadores.empty()
					busters.empty()
					map01.empty()
					map02.empty()
					map03.empty()
					enemigos.empty()
					balasE.empty()
					mundo1.stop()
					mundo2.stop()
					mundo3.stop()
					segundos3+=1
		

		if jugador.salud == 0:
			gameover=True
			jugadores.empty()
			busters.empty()
			map01.empty()
			map02.empty()
			map03.empty()
			enemigos.empty()
			balasE.empty()
			mundo1.stop()
			mundo2.stop()
			mundo3.stop()
			segundos3+=1

		if bloquears:
			if jugador.rect.y>HEIGHT:
				muerte.play()
				jugador.salud=0
				gameover=True
				jugadores.empty()
				busters.empty()
				map01.empty()
				map02.empty()
				map03.empty()
				enemigos.empty()
				balasE.empty()
				mundo1.stop()
				mundo2.stop()
				mundo3.stop()
				segundos3+=1
				bloquears=False		
								 	
		if mundo01:
			fondo=imageFondo[1]
		if mundo02:
			fondo=imageFondo[2]
		if mundo03:
			fondo=imageFondo[3]

		#Actualizacion
		if not gameover:
			if not loading:
				if not pause:
					pantalla.blit(fondo,[posFondoX,posFondoY])
					jugadores.draw(pantalla)
					jugadores.update()
					enemigos.draw(pantalla)
					enemigos.update()
					if mundo01:
						map01.draw(pantalla)
						map01.update()
					if mundo02:	
						map02.draw(pantalla)
						map02.update()
					if mundo03:	
						map03.draw(pantalla)
						map03.update()
					busters.update()
					busters.draw(pantalla)
					balasE.update()
					balasE.draw(pantalla)
					pantalla.blit(telonNegro,(0,0))
					pantalla.blit(telonRojo,(50,11))			
					saluds.update()
					saluds.draw(pantalla)
					if seleccion==0:
						pantalla.blit(titlex,(0,8))	
					else:
						pantalla.blit(titlezero,(0,8))
					if mundo01:
						pantalla.blit(titlel1,(400,8))
					if mundo02:
						pantalla.blit(titlel2,(400,8))
					if mundo03:
						pantalla.blit(titlefl,(400,8))					
					pygame.display.flip()
					reloj.tick(20)
				else:
					pantalla.blit(imageFondo[0],(0,0))
					pygame.display.flip()
			else:
				pantalla.blit(imageLoading,(0,0))
				pygame.display.flip()
		else:
			if jugador.salud>0:
				pantalla.blit(imageWin,(0,0))
			else:
				pantalla.blit(imageLoss,(0,0))		
			pygame.display.flip()
			if segundos3>500:
				segundos3=0
				mundo01=True
				mundo02=False
				mundo03=False
				seguir3=True
				gameover=False
				bloquears=True
				avanzar=False
				termino=False				

if __name__ == "__main__":
	while True:
		main()