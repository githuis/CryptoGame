import pygame
from pygame.locals import *
from lib import engine


class Player(pygame.sprite.Sprite):
	'''player sprite'''

	def __init__(self, imagepath, width, height, x, y, surface, ID):
		pygame.sprite.Sprite.__init__(self)

		self.imagepath = imagepath
		self.image = pygame.image.load(imagepath)

		self.direction = 'right'
		self.speed = 75

		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

		self.ID = ID

		self.inventory = pygame.sprite.Group()

	def move(self, key, sprites):
		'''checks collisions with other objects, then sets new coords for sprite'''

		if key == K_d:
			self.direction = 'right'
		elif key == K_s:
			self.direction = 'down'
		elif key == K_a:
			self.direction = 'left'
		elif key == K_w:
			self.direction = 'up'

		old_x = self.rect.x
		old_y = self.rect.y

		if self.direction == 'right':
			self.change_picture('to_right')
			self.rect.x += self.speed
		elif self.direction == 'down':
			self.rect.y += self.speed
		elif self.direction == 'left':
			self.change_picture('to_left')
			self.rect.x -= self.speed
		elif self.direction == 'up':
			self.rect.y -= self.speed
		if self.rect.x == -75 or self.rect.x == 900 or self.rect.y == -75 or self.rect.y == 675:
			self.rect.x = old_x
			self.rect.y = old_y
		for s in sprites:
			if engine.check_collision(self, s):
				self.rect.x = old_x
				self.rect.y = old_y
				break

	'''def draw(self):
		DISPLAYSURF.blit(self.image, self.rect)'''

	def add_to_inventory(self, sprites):
		for sprite in sprites:
			self.inventory.add(sprite)

	def change_picture(self, newpic):
		if newpic == 'to_right':
			self.image = pygame.image.load(self.imagepath)
		elif newpic == 'to_left':
			self.image = pygame.image.load(self.imagepath2)