"""Extension des classes pygame, pour les personnages."""

import pygame

import constants as cst
"""Imports."""


class Entity(pygame.sprite.Sprite):
	"""Classe d'affichagedes entités."""

	def __init__(self, file, x, y, parent):
		"""Initialisation."""
		super(Entity, self).__init__()

		self.image = pygame.image.load(file).convert_alpha()
		self.rect = self.image.get_rect()

		self.chara = parent

		self.x = x
		self.y = y

	def update(self):
		"""Update."""
		self.rect.x = self.x
		self.rect.y = self.y - 1 * cst.IMG_SIZE

		if self.chara.in_moove:
			self.chara.moove()
