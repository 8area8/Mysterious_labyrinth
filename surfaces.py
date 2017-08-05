"""Toutes les instances de surfaces sont stockés ici."""

import os

import pygame
from pygame.locals import *
import pygame_extend as p_e

import constants
import data as dt
import camera as cmr
"""Imports."""

main_screen = pygame.display.set_mode(
	constants.MAIN_SCREEN_SIZE)


class TitleMenu:
	"""Classe qui prend les surfaces de l'écran titre."""

	def __init__(self):
		"""Init."""
		self.main_background = pygame.image.load('img/main_menu.jpg').convert()

		self.new_game = p_e.FontButton(
			'Nouvelle partie', x=211, y=259, name="new_game")
		self.load_game = p_e.FontButton(
			'Charger une partie', x=183, y=313,
			name="load_game", test=os.path.isfile('save'))
		self.exit = p_e.FontButton(
			'quitter le jeu', x=229, y=375, name="exit")

	def get_buttons(self):
		"""Retourne une liste des boutons."""
		font_grp = pygame.sprite.Group()
		font_grp.add(
			self.new_game,
			self.load_game,
			self.exit)
		return font_grp


class SelectLevel:
	"""Classe qui prend les surfaces du menu de selection de niveaux."""

	def __init__(self):
		"""Init."""
		self.book_files = dt.Data.list_map_files()
		self.index = 0

		self.main_background = pygame.image.load('img/select_level.jpg').convert()

		self.select_a_level = p_e.FontSprite(
			"Selectionnez un niveau:", x=153, y=47)
		self.back = p_e.SpriteButton(
			"img/back.png", 'img/back-2.png', x=26, y=33, name="back")
		self.page_x_on_y = p_e.DynamicsFonts(
			"page {}/{}", 153, 403, "book",
			self.index + 1, len(self.book_files), size=18)

	def get_sprites(self):
		"""Retourne une liste des textes."""
		sprites_grp = pygame.sprite.Group()
		sprites_grp.add(
			self.select_a_level,
			self.page_x_on_y)
		return sprites_grp

	def get_map_buttons(self):
		"""Retourne une liste des boutons."""
		buttons_grp = pygame.sprite.Group()

		x_list = 178
		y_list = 154

		for element in self.book_files[self.index]:
			text = "{}".format(element)
			buttons_grp.add(p_e.FontButton(
				text, size=18, x=x_list, y=y_list, name=element))
			y_list += 45
		buttons_grp.add(self.back)

		return buttons_grp


class Game:
	"""Classe qui gère les surfaces de la partie Game."""

	def __init__(self):
		"""Initalisation."""
		self.background = pygame.image.load('img/game_bg.jpg').convert()

		self.position = p_e.FontSprite("position:", x=24, y=421, size=15)
		self.coords = p_e.DynamicsFonts("{}, {}", 37, 445, "coords", 0, 10, size=20)

		self.pm = p_e.DynamicsFonts("{}", 280, 464, "pm", 0, size=18)
		self.pm.color = (249, 227, 157)
		self.pa = p_e.DynamicsFonts("{}", 364, 463, "pa", 0, size=18)
		self.pa.color = (249, 227, 157)

		self.cross = p_e.SpriteButton(
			"img/cross.png", 'img/cross-2.png', 588, 10, "cross")

		self.back_to_main = p_e.SimpleSprite("img/text_screen.png", 133, 144)
		self.yes = p_e.FontButton("oui", 226, 241, "yes", h_position=(6, 4))
		self.no = p_e.FontButton("non", 361, 241, "no", h_position=(6, 4))

		self.victory = p_e.AnimatedSprite(
			(0, 0), (640, 480), 'img/victory-anim', play=True)

	def get_map_surface(self, size):
		"""Retourne la surface de la map du jeu."""
		return pygame.Surface(size)

	def get_camera_screen(self, map_screen):
		"""Retourne la surface intelligente 'camera'."""
		return cmr.Camera(map_screen)

	def get_sprites(self):
		"""Retourne une liste des sprites."""
		sprites_grp = pygame.sprite.Group()
		sprites_grp.add(
			self.position,
			self.coords,
			self.pm,
			self.pa)
		return sprites_grp

	def get_button_list(self):
		"""Retourne les différents boutons."""
		button_list = pygame.sprite.Group()
		button_list.add(self.cross)
		return button_list

	def get_back_to_main(self):
		"""Retourne le menu de transition."""
		btm = pygame.sprite.Group()
		btm.add(
			self.back_to_main)
		btm_txt = pygame.sprite.Group()
		btm_txt.add(
			self.yes,
			self.no)
		return btm, btm_txt

	def get_vict(self):
		"""Retourne le sprite victoire."""
		vct = pygame.sprite.Group()
		vct.add(self.victory)
		return vct
