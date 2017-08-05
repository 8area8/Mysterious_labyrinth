"""Regroupe les entités du jeu."""

import pygame
import pygame_xtd_entity as p_x_ntt
import constants as cst


class GroupEntity:
	"""La classe qui stock les personnages."""

	def __init__(self):
		"""Initialisation."""
		self.hero = None

		self.group = pygame.sprite.Group()

	def create_hero(self, x, y):
		"""Crée un héro."""
		self.group.empty()
		self.hero = Hero(x, y)
		self.group.add(self.hero.apparent)


class Hero:
	"""Classe qui définit le personnage jouable."""

	def __init__(self, x, y):
		"""Initialisation."""
		self.name = "Egama"

		self.apparent = p_x_ntt.Entity(
			'img/Edama.png', x * cst.IMG_SIZE, y * cst.IMG_SIZE, self)

		self._x = x
		self._y = y

		self._position = (x, y)

		self.moves_point = 5
		self.current_mp = self.moves_point

		self.in_moove = False  # les prochaines variables sont propres au mouvement
		self.moove_frames = []
		self.moove_end = []
		self.moove_i = 0
		self.moove_i_max = 0
		self.abs_x, self.abs_y = 0, 0

	def _get_x(self):
		"""Propriété de self._x."""
		self._x = self.apparent.x // cst.IMG_SIZE
		return self._x
	x = property(_get_x)

	def _get_y(self):
		"""Propriété de self.-y."""
		self._y = self.apparent.y // cst.IMG_SIZE
		return self._y
	y = property(_get_y)

	def _get_position(self):
		"""Propriété de self._position."""
		self._position = (self.x, self.y)
		return self._position
	position = property(_get_position)

	def start_moove(self, case_list):
		"""Actionne le mouvement.

		1: on initialise les variables
		2: pourchaque case, on teste les positions:
			si c'est à gauche,à droite, en haut ou en bas,
			le personnage se déplacera en conséquence.
		3: x et y prennent la valeur de la position testé,
			et on recommence pour les autres autres cases.
			On possède 2 listes, une qui donne les informations
			de mouvement (vitesse et direction), et l'autre qui
			teste si on est bien arrivé sur chaque case.
		"""
		self.in_moove = True
		self.moove_frames = []
		self.moove_end = []
		self.moove_i = 0
		self.moove_i_max = len(case_list)
		x, y = self.x, self.y

		for case in case_list:
			if case.position == (x, y + 1):
				self.moove_frames.append((0, cst.SPEED_MOOVE))
				self.moove_end.append((x, y + 1))

			if case.position == (x, y - 1):
				self.moove_frames.append((0, -(cst.SPEED_MOOVE)))
				self.moove_end.append((x, y - 1))

			if case.position == (x + 1, y):
				self.moove_frames.append((cst.SPEED_MOOVE, 0))
				self.moove_end.append((x + 1, y))

			if case.position == (x - 1, y):
				self.moove_frames.append((-(cst.SPEED_MOOVE), 0))
				self.moove_end.append((x - 1, y))
			x, y = case.position

	def moove(self):
		"""Déplace le personnage.

		0: on définit la position prétendu du personnage.
			utile pour différents testes d'évènements.
		1: on déplace le personnage
		2: on teste si sa position correspond à la case visée
		3: si oui, on incrémente l'index de mouvement, on teste
			s'il reste des cases à parcourir et si oui, on les
			parcours.
		"""
		self.abs_x, self.abs_y = self.moove_end[self.moove_i]

		self.apparent.x += self.moove_frames[self.moove_i][0]
		self.apparent.y += self.moove_frames[self.moove_i][1]

		x, y = self.moove_end[self.moove_i]
		x, y = (x * cst.IMG_SIZE, y * cst.IMG_SIZE)
		if (self.apparent.x, self.apparent.y) == (x, y):
			self.moove_i += 1
			if self.moove_i == self.moove_i_max:
				self.in_moove = False
