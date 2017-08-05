"""Extension des classes popres à pygame."""

import pygame

import os
"""Imports."""


class SimpleSprite(pygame.sprite.Sprite):
	"""Un sprite qui incorpore la position à l'appel."""

	def __init__(self, file, x, y, name="sprite"):
		"""Initialisation."""
		super(SimpleSprite, self).__init__()

		self.image = pygame.image.load(file).convert_alpha()
		self.rect = self.image.get_rect()

		self.name = "sprite"

		self.x = x
		self.y = y

	def update(self):
		"""Update."""
		self.rect.x = self.x
		self.rect.y = self.y


class SpriteButton(SimpleSprite):
	"""Une image cliquable."""

	def __init__(self, file, file_h, x, y, name):
		"""Initialisation."""
		super(SpriteButton, self).__init__(file, x, y)

		self.file = file
		self.file_h = file_h

		self.name = name

		self.hover = False
		self.hover_memory = False

	def update(self):
		"""Update."""
		if self.hover and not self.hover_memory:
			self.hovering()
			self.hover_memory = True
		elif not self.hover and self.hover_memory:
			self.image = pygame.image.load(self.file).convert_alpha()
			self.hover_memory = False

		self.rect.x = self.x
		self.rect.y = self.y

	def hovering(self):
		"""Effet de zoom."""
		self.image = pygame.image.load(self.file_h).convert_alpha()


class FontSprite(pygame.sprite.Sprite):
	"""Une image textuel."""

	def __init__(self, text, x, y, name="font", size=24):
		"""Initialisation."""
		super(FontSprite, self).__init__()

		self.color = (212, 190, 190)
		self.text = text
		self.size = size

		self.name = name

		self.x = x
		self.y = y

		self.set_text()

	def set_text(self):
		"""Initialisation du texte."""
		self.font = pygame.font.Font('Fonts/Aclonica.ttf', self.size)
		self.image = self.font.render(str(self.text), 1, self.color).convert_alpha()
		self.rect = self.image.get_rect()

	def update(self):
		"""Update."""
		self.rect.x = self.x
		self.rect.y = self.y


class FontButton(FontSprite):
	"""Un bouton textuel."""

	def __init__(self, text, x, y, name, size=24, h_position=None, test=None):
		"""Initialisation."""
		super(FontButton, self).__init__(text, x, y, size=size)

		self.name = name

		self.hover = False
		self.hover_memory = False
		self.h_position = h_position

		self.test = test
		if self.test is False:
			self.grey_text()

		self.rect.x = self.x
		self.rect.y = self.y

	def update(self):
		"""Update."""
		if self.test is False:
			return
		if self.hover and not self.hover_memory:
			self.hovering()
			self.hover_memory = True
		elif not self.hover and self.hover_memory:
			self.set_text()
			if self.h_position:
				self.x += self.h_position[0]
				self.y += self.h_position[1]
			else:
				self.x += 13
				self.y += 4
			self.hover_memory = False

		self.rect.x = self.x
		self.rect.y = self.y

	def hovering(self):
		"""Effet de zoom."""
		self.font = pygame.font.Font('Fonts/Aclonica.ttf', self.size + 4)
		self.image = self.font.render(str(self.text), 1, self.color).convert_alpha()
		if self.h_position:
			self.x -= self.h_position[0]
			self.y -= self.h_position[1]
		else:
			self.x -= 13
			self.y -= 4

	def grey_text(self):
		"""Le texte est grisé."""
		self.x += 25
		self.font = pygame.font.Font('Fonts/Aclonica.ttf', self.size - 3)
		self.image = self.font.render(
			str(self.text), 1, (160, 160, 150)).convert_alpha()
		self.rect = self.image.get_rect()


class DynamicsFonts(FontSprite):
	"""Une image textuel."""

	def __init__(self, text, x, y, name, a_arg, b_arg=None, size=24):
		"""Initialisation."""
		super(DynamicsFonts, self).__init__(text, x, y, size=size)

		self.name = name

		self.two_args = False
		self.a_arg = a_arg
		self.b_arg = b_arg

		if self.b_arg:
			self.two_args = True

		self.image = self.font.render(
			str(self.get_dynamic_text()), 1, self.color).convert_alpha()

	def update(self):
		"""Update."""
		self.image = self.font.render(
			str(self.get_dynamic_text()), 1, self.color).convert_alpha()
		self.rect.x = self.x
		self.rect.y = self.y

	def get_dynamic_text(self):
		"""Retourne un texte dynamique."""
		if self.a_arg is None:
			self.a_arg = 0

		if self.two_args:
			if self.b_arg is None:
				self.b_arg = 0
			return self.text.format(self.a_arg, self.b_arg)

		return self.text.format(self.a_arg)


class AnimatedSprite(pygame.sprite.Sprite):
	"""Un sprite animé. repris sur le net, + quelques modifs."""

	def __init__(self, position, size, path, play=False, frame=3):
		"""Animated sprite."""
		super(AnimatedSprite, self).__init__()

		self.play = play

		self.position = position

		self.rect = pygame.Rect(position, size)
		self.images = self.load_images(path)
		self.index = 0
		self.image = self.images[self.index]

		self.velocity = pygame.math.Vector2(0, 0)

		self.animation_frames = frame
		self.current_frame = 0

	def update_frame_dependent(self):
		"""Update the image of Sprite every 6 frame."""
		if self.index == len(self.images) - 1:
			return
		self.current_frame += 1
		if self.current_frame >= self.animation_frames:
			self.current_frame = 0
			self.index += 1
			self.image = self.images[self.index]

		self.rect.move_ip(*self.velocity)

	def update(self):
		"""Update."""
		if self.play:
			self.update_frame_dependent()

		pos = self.position[0] * 60, self.position[1] * 60
		self.rect.x, self.rect.y = pos

	def load_images(self, path):
		"""Charge une liste d'image."""
		images = []
		for file_name in os.listdir(path):
			image = pygame.image.load(path + os.sep + file_name).convert_alpha()
			images.append(image)
		return images
