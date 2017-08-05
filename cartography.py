"""Gère la création de la map."""

import pygame

import data as dt
import case_entity as c_entity
import constants as cst
"""Imports."""


class Map:
	"""Classe qui gère les coordonnées et éléments de la map."""

	def __init__(self, map_name, entity, case_entity):
		"""Initalisation."""
		dt.Data.file = "core_maps/{}.txt".format(map_name)

		self.size = (0, 0)
		self.coords = {}

		self.entity = entity
		self.case_entity = case_entity

		self.create_map()

	def create_map(self):
		"""Crée la carte en utilisant le module Data."""
		coordinates = dt.Data.import_file()

		for y, string in enumerate(coordinates):
			for x, letter in enumerate(string):
				self.create_case(letter, x, y)

		self.size = (
			len(coordinates[0]) * cst.IMG_SIZE, len(coordinates) * cst.IMG_SIZE)

	def create_case(self, letter, x, y):
		"""Crée une case du labytinthe."""
		if letter == "O":
			self.coords[x, y] = c_entity.Wall('img/wall.png', x, y)
		elif letter == " ":
			self.coords[x, y] = c_entity.Path('img/path.png', x, y)
		elif letter == "U":
			self.coords[x, y] = c_entity.Entrance('img/exit.png', x, y)
		elif letter == ".":
			self.coords[x, y] = c_entity.Door('img/door.png', x, y)
		elif letter == "X":
			self.coords[x, y] = c_entity.Path('img/path.png', x, y)
			self.entity.create_hero(x, y)

		self.case_entity.group.add(self.coords[x, y].apparent)
