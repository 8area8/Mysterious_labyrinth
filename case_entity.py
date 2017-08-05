"""Les élements du labytinth."""

import pygame
import pygame_extend as p_e

import constants as cst


class CaseEntityGroup:
	"""Classe qui stock les entités de labyrinthe."""

	def __init__(self):
		"""Initialisation."""
		self.group = pygame.sprite.Group()


class LabyrinthObject():
	"""CLasse mère aux objets du labyrinth."""

	def __init__(self, filename, x, y, door=False):
		"""On définit les propriétés de base."""
		self.solid = False
		self.x = x
		self.y = y

		if not door:
			self.apparent = p_e.SimpleSprite(
				filename, self.x * cst.IMG_SIZE, self.y * cst.IMG_SIZE)
		else:
			self.apparent = p_e.AnimatedSprite(
				(x, y), (60, 60), 'img/door-anim', frame=1)


class Wall(LabyrinthObject):
	"""Définition des murs du labyrinthe."""

	def __init__(self, filename, x, y):
		"""Initialisation de l'objet."""
		super(Wall, self).__init__(filename, x, y)
		self.solid = True

		self.name = "wall"


class Path(LabyrinthObject):
	"""Définition des chemins."""

	def __init__(self, filename, x, y, hero=False):
		"""Init."""
		super(Path, self).__init__(filename, x, y)

		self.name = "path"


class Entrance(LabyrinthObject):
	"""Définition de l'entrée du labyrinthe."""

	def __init__(self, filename, x, y):
		"""Init."""
		super(Entrance, self).__init__(filename, x, y)

		self.name = "exit"


class Door(LabyrinthObject):
	"""Définition des portes."""

	def __init__(self, filename, x, y):
		"""Init."""
		super(Door, self).__init__(filename, x, y, door=True)

		self.name = "door"
