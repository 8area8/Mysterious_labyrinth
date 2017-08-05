"""Gestion centralisé des évènements."""

import pygame
from pygame.locals import *

import constants as cst
import menus
import game
import data
"""Imports."""


class BaseEvents:
	"""Boîte à outils pour les évènements."""

	def __init__(self):
		"""Init."""
		self.leftclick = False
		self.mouse_pos = None

		self.actions = None

		self.clic = pygame.mixer.Sound('sound/clic.wav')

	def get_leftclick(self, event):
		"""Définit le clique gauche enfoncé de la souris."""
		if event.type == MOUSEBUTTONDOWN and event.button == 3:
			self.leftclick = True
		elif event.type == MOUSEBUTTONUP:
			self.leftclick = False

	def get_hovering(self, button_list=None):
		"""Teste un effet de survol sur l'image."""
		if button_list:
			btn_list = button_list
		else:
			btn_list = self.button_list
		for button in btn_list:
			if button.rect.collidepoint(self.mouse_pos):
				button.hover = True

			if button.hover:
				if not button.rect.collidepoint(self.mouse_pos):
					button.hover = False

	def get_clic(self):
		"""Clic!."""
		self.clic.play()
		self.clic.set_volume(0.3)


class TitleMenu(BaseEvents):
	"""Evènements du menu TitleMenu."""

	def __init__(self, loop, button_list):
		"""Init."""
		super(TitleMenu, self).__init__()
		self.loop = loop

		self.button_list = button_list

	def test_events(self, event):
		"""Liste des évènements possibles."""
		self.mouse_pos = pygame.mouse.get_pos()

		if event.type == MOUSEBUTTONDOWN and event.button == 1:
			self.get_clic()
			for button in self.button_list:
				if button.rect.collidepoint(self.mouse_pos):
					if button.name == "new_game":
						self.loop.active_screen = menus.SelectLevel(self.loop)
					elif button.name == "load_game":
						if button.test:
							load_file = data.Data.load()
							map_name = load_file.map_name
							self.loop.active_screen = game.Game(
								self.loop, map_name, load=load_file)
					elif button.name == "exit":
						self.loop.running = False

		self.get_hovering()


class SelectLevel(BaseEvents):
	"""Evènements du menu SelectLevel."""

	def __init__(self, loop, button_list):
		"""Init."""
		super(SelectLevel, self).__init__()
		self.loop = loop

		self.button_list = button_list

	def test_events(self, event):
		"""Liste des évènemets possibles."""
		self.mouse_pos = pygame.mouse.get_pos()

		if event.type == MOUSEBUTTONDOWN and event.button == 1:
			self.get_clic()
			for button in self.button_list:
				if button.name == "back":
					if button.rect.collidepoint(self.mouse_pos):
						self.loop.active_screen = menus.TitleMenu(self.loop)
				elif button.rect.collidepoint(self.mouse_pos):
					self.loop.active_screen = game.Game(self.loop, button.name)

		self.get_hovering()


class Game(BaseEvents):
	"""Evènements du jeu."""

	def __init__(
		self, loop, map_name, camera, pathfinder,
		actual_hero, sprite_grp, button_list,
		draw_sprite, btm_txt, coords, music):
		"""Initialisation.

		La classe contient une tonne de paramètres. Je préfère
		donner chaque paramètre un par un plutot que d'envoyer
		la classe 'Game' comme gros paramètre; ça permet une plus
		grande modularité et une meilleure maintenance.
		"""
		super(Game, self).__init__()
		self.loop = loop

		self.map_name = map_name

		self.music = music
		self.mus_door = pygame.mixer.Sound('sound/door.wav')
		self.mus_door.set_volume(0.3)

		self.camera = camera
		self.sprite_grp = sprite_grp
		self.button_list = button_list
		self.draw_sprite = draw_sprite
		self.one_victory = False
		self.btm_txt = btm_txt

		self.actual_hero = actual_hero
		self.test_pos = ()

		self.coords = coords
		self.pathfinder = pathfinder

	def test_events(self, event):
		"""Appel les évènements interactifs."""
		self.get_leftclick(event)
		if self.leftclick:
			self.moove_map(event)

		if event.type == MOUSEBUTTONDOWN and event.button == 1:
			self.get_clic()
			if not self.actual_hero.in_moove and self.pathfinder.path.case_list:
				self.moove_character(self.pathfinder.path.case_list)
			self.menu_back_to_main()
			if self.draw_sprite[1]:
				self.erase()
				self.loop.active_screen = menus.TitleMenu(self.loop)

	def update_events(self):
		"""Appel les évènements passifs."""
		self.mouse_pos = pygame.mouse.get_pos()
		x, y = self.mouse_pos
		x_case, y_case = self.get_case_coords(x, y)

		self.save()

		self.test_victory()
		self.test_door()

		self.display_datas(x_case, y_case)
		self.active_pathfinder(x_case, y_case)
		if self.draw_sprite[0]:
			self.get_hovering(button_list=self.btm_txt)
		else:
			self.get_hovering()

	def moove_map(self, event):
		"""On bouge la map grâce à la souris (clique droit enfoncé)."""
		if event.type == MOUSEMOTION:
			if self.camera.rect.collidepoint(self.mouse_pos):
				x_motion, y_motion = pygame.mouse.get_pos()

				self.camera.x -= x_motion - self.loop.x
				self.camera.y -= y_motion - self.loop.y

	def get_relatives_coords(self, x, y, abstract=True, index_x=0, index_y=0):
		"""Retourne les coordonnées de la case sous le curseur."""
		x_map, y_map = cst.CAMERA_SIZE

		if not self.camera.map.get_rect().collidepoint(self.mouse_pos):
			return None, None
		if x < 0 or y < 0:
			return None, None

		while x > cst.IMG_SIZE * (index_x + 1):
			index_x += 1
		x = cst.IMG_SIZE * index_x

		while y > cst.IMG_SIZE * (index_y + 1):
			index_y += 1
		y = cst.IMG_SIZE * index_y

		if abstract:
			x = x // 60
			y = y // 60
		return x, y

	def get_case_coords(self, x, y):
		"""Retourne la position relative à la map et non à l'écran."""
		x = x + self.camera.x
		y = y + self.camera.y
		if x and y:
			x, y = self.get_relatives_coords(x, y)
		return x, y

	def moove_character(self, case_list):
		"""Actionne le mouvement du personnage."""
		self.actual_hero.start_moove(case_list)

	def test_victory(self):
		"""Teste les conditions de victoire.

		Si c'est bon, on modifie la liste qui gère l'activation,
		et c'est la classe Game qui se chargera de mettre à jour
		l'animation de victoire.
		"""
		pos = self.actual_hero.position
		if self.coords[pos].name == "exit" and not self.draw_sprite[1]:
			self.draw_sprite[1] = True

		elif self.draw_sprite[1] and not self.one_victory:
			self.music.play_victory()
			self.one_victory = True

	def test_door(self):
		"""Teste le passage du héro sur une porte."""
		if self.test_pos == (self.actual_hero.abs_x, self.actual_hero.abs_y):
			return
		self.test_pos = self.actual_hero.abs_x, self.actual_hero.abs_y
		coord = self.coords[self.test_pos]
		print("{} {}".format(coord.x, coord.y))
		if coord.name == "door":
			if not coord.apparent.play:
				coord.apparent.play = True
				self.mus_door.play()

	def menu_back_to_main(self):
		"""Affiche un menu de retour à l'écran titre."""
		if not self.draw_sprite[0]:
			for button in self.button_list:
				if button.name == "cross" and button.rect.collidepoint(self.mouse_pos):
					self.draw_sprite[0] = True
		elif self.draw_sprite[0]:
			for button in self.btm_txt:
				if button.name == "yes" and button.rect.collidepoint(self.mouse_pos):
					self.loop.active_screen = menus.TitleMenu(self.loop)
				elif button.name == "no" and button.rect.collidepoint(self.mouse_pos):
					self.draw_sprite[0] = False

	def active_pathfinder(self, x_case, y_case):
		"""Active le pathfinder, qui se charge de trouver un chemin."""
		if not self.actual_hero.in_moove and not\
			self.draw_sprite[0] and not self.draw_sprite[1]:
			self.pathfinder.test_path(self.actual_hero, x_case, y_case)
		else:
			self.pathfinder.path.case_list = []

	def display_datas(self, x_case, y_case):
		"""Met à jour différentes petites données."""
		for sprite in self.sprite_grp:
			if sprite.name == "coords":
				sprite.a_arg, sprite.b_arg = x_case, y_case
			elif sprite.name == "pm":
				sprite.a_arg = self.actual_hero.current_mp

	def save(self):
		"""Sauvegarde la partie."""
		data.Data.save(self.actual_hero.position, self.map_name)

	def erase(self):
		"""Ecrase la sauvegarde."""
		data.Data.erase_save()
