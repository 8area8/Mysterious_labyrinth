"""On définit la caméra du jeu.

Elle se déplacera sur la carte du jeu et pourra
suivre les déplacement du joueur.
"""

import pygame

import constants as cst
"""Imports."""


class Camera:
	"""La classe caméra."""

	def __init__(self, map_to_blit):
		"""Initialisation de la caméra."""
		self.x = 0
		self.y = 0

		self.map = map_to_blit
		self.size = map_to_blit.get_size()

		self.surface = pygame.Surface(cst.CAMERA_SIZE)
		self.rect = self.surface.get_rect()

	def recenter_hero(self, hero, start=None):
		"""Recentre la caméra sur le héros."""
		if hero.in_moove or start:
			self.x = hero.apparent.x - (cst.IMG_SIZE * 4)
			self.y = hero.apparent.y - (cst.IMG_SIZE * 3)

	def stop_overflow(self, to_x, to_y):
		"""S'assure que la caméra ne sorte pas de la carte."""
		if to_x < 0:
			to_x = 0
		elif to_x > self.size[0] - (10 * cst.IMG_SIZE):
			if self.size[0] >= 10 * cst.IMG_SIZE:
				to_x = self.size[0] - (10 * cst.IMG_SIZE)

		if to_y < 0:
			to_y = 0
		elif to_y > self.size[1] - (7 * cst.IMG_SIZE):
			to_y = self.size[1] - (7 * cst.IMG_SIZE)

		return to_x, to_y

	def update(self):
		"""Met à jour la caméra.

		1 - appel de la méthode qui empêche de sortir de la map.
		2 - blit de la map. C'est en réalité la map qui bouge
			et non la caméra. On inverse donc les valeurs de
			x et de y.
		"""
		self.x, self.y = self.stop_overflow(self.x, self.y)

		self.surface.blit(self.map, (-(self.x), -(self.y)))
