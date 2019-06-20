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
map01=pygame.sprite.Group()
map02=pygame.sprite.Group()
map03=pygame.sprite.Group()

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
				if (self.rect.bottom >= p.rect.top) and (self.vel_posY > 0):
					self.rect.bottom = p.rect.top
					self.vel_posY=0
						
				if (self.rect.top < p.rect.bottom) and (self.vel_posY < 0):
					self.rect.top = p.rect.bottom
					self.vel_posY=0

		if mundo02:			
			ls_col=pygame.sprite.spritecollide(self,map02,False)
			for p in ls_col:
				if (self.rect.bottom >= p.rect.top) and (self.vel_posY > 0):
					self.rect.bottom = p.rect.top
					self.vel_posY=0
						
				if (self.rect.top < p.rect.bottom) and (self.vel_posY < 0):
					self.rect.top = p.rect.bottom
					self.vel_posY=0

		if mundo03:			
			ls_col=pygame.sprite.spritecollide(self,map03,False)
			for p in ls_col:
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
		self.image=self.matrix[0][0][0][0]
		self.rect=self.image.get_rect()
		self.rect.inflate_ip(-22,0)
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
				if (self.rect.bottom >= p.rect.top) and (self.vel_posY > 0):
					self.rect.bottom = p.rect.top
					self.vel_posY=0
						
				if (self.rect.top < p.rect.bottom) and (self.vel_posY < 0):
					self.rect.top = p.rect.bottom
					self.vel_posY=0

		if mundo02:			
			ls_col=pygame.sprite.spritecollide(self,map02,False)
			for p in ls_col:
				if (self.rect.bottom >= p.rect.top) and (self.vel_posY > 0):
					self.rect.bottom = p.rect.top
					self.vel_posY=0
						
				if (self.rect.top < p.rect.bottom) and (self.vel_posY < 0):
					self.rect.top = p.rect.bottom
					self.vel_posY=0

		if mundo03:			
			ls_col=pygame.sprite.spritecollide(self,map03,False)
			for p in ls_col:
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
	pygame.display.set_caption("Mega Man XZ-Reborn")
	icon=pygame.image.load("images/icon.png")
	selector=pygame.image.load("images/selector.png")
	selector2=pygame.image.load("images/selector2.png")
	imageMenu=pygame.image.load("images/fondomenu.png")
	imageTurorial=pygame.image.load("images/fondotutorial.png")
	imageFondo1=pygame.image.load("maps/fondomapa01.png")
	imageFondo2=pygame.image.load("maps/fondomapa02.png")
	imageFondo3=pygame.image.load("maps/fondomapa03.png")
	imageVideo=pygame.image.load("images/video.png")
	imageSelector=pygame.image.load("images/selection.png")
	imageFondoPrevius=[imageMenu,imageTurorial,imageVideo,imageSelector]
	imageFondo=[0,imageFondo1,imageFondo2,imageFondo3]
	pygame.display.set_icon(icon)
	Map01(pantalla)
	Map02(pantalla)
	Map03(pantalla)
	#Jugador Mega Man X - X or Zero
	seleccion=0	
	posFondoX,posFondoY=0,0
	velx=-5
	final=False
	reloj=pygame.time.Clock()
	#Previos
	sound=pygame.mixer.Sound("sounds/intro.wav")
	movie=pygame.movie.Movie("videos/intro.mpg")
	movie_screen=pygame.Surface(movie.get_size())
	movie.set_display(movie_screen)
	movie.set_volume(0.99)
	megaman=RecorteX()
	zero=RecorteZero()
	x,y=155,[130,155,180]
	i,j=0,0
	m,z=13,1
	seguir1=False
	seguir2=False
	intro=False
	tutorial=False
	acabar=False
	while not seguir1:
		for evento in pygame.event.get():
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()
			if evento.type == KEYDOWN:
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
				movie.play()
				sound.play()
				pantalla.blit(imageFondoPrevius[2],(0,0))
				pantalla.blit(movie_screen,(90,10))
				if acabar:
					movie.stop()
					sound.stop()
					acabar=False
					seguir1=True
			else:	
				pantalla.blit(imageFondoPrevius[0],(0,0))
				pantalla.blit(selector,(x,y[i]))           
		pygame.display.flip()

	i=0
	while not seguir2:
		for evento in pygame.event.get():
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()
			if evento.type == KEYDOWN:
				if evento.key == K_SPACE:
					if i==0:
						seleccion=0
						seguir2=True
					else:
						seleccion=1
						seguir2=True
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
    #Ciclo del juego
	while True:
		for evento in pygame.event.get():
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()
			if evento.type == KEYDOWN:		
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
		if jugador.salto:
			jugador.vel_posY=-6
			jugador.salto=False

 		if jugador.rect.x < 0 and jugador.vel_posX<0.:
			jugador.rect.x=0

		if not mundo03:
			if not final:	
				if jugador.rect.x >= WIDTH-100 and jugador.vel_posX>0.:
					jugador.rect.x=WIDTH-100
					posFondoX+=velx
					#Mapa1
					if mundo01:
						if posFondoX<-2680:	
							velx=0
							final=True
						for m in map01:
							m.posx_fondo=posFondoX
					#Mapa2
					if mundo02:	
						if posFondoX<-1880:
							velx=0
							final=True
						for m in map02:
							m.posx_fondo=posFondoX	
			else:	
				if jugador.rect.x>WIDTH-40:
						jugador.rect.x=WIDTH-40

		if jugador.rect.x==WIDTH-50:
			if mundo01:
				map01.empty()
				jugador.rect.x=50
				if isinstance(jugador,X):
					jugador.rect.y=206
				else:
					jugador.rect.y=186	
				posFondoX=0
				final=False
				velx=-5
				mundo01=False
				mundo02=True
				mundo03=False

		if jugador.rect.x==WIDTH-40:		
			if mundo02:
				map02.empty()
				jugador.rect.x=115
				if isinstance(jugador,X):
					jugador.rect.y=229
				else:
					jugador.rect.y=209	
				jugador.rect.y=50
				posFondoX=0
				final=False
				velx=-5
				mundo01=False
				mundo02=False
				mundo03=True	

		if mundo01:
			fondo=imageFondo[1]
		if mundo02:
			fondo=imageFondo[2]
		if mundo03:
			fondo=imageFondo[3]

		#Actualizacion	
		pantalla.blit(fondo,[posFondoX,posFondoY])
		jugadores.draw(pantalla)
		jugadores.update()
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
		pygame.display.flip()
		reloj.tick(20)

if __name__ == "__main__":
	main()