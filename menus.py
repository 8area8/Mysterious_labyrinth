"""Possèdes les classes de menus du jeu."""

import os

import surfaces as srf
import musics as msc
import events as evt
"""Imports."""


class TitleMenu:
	"""Le menu principale du jeu."""

	def __init__(self, loop):
		"""Initialisation."""
		self.title_srf = srf.TitleMenu()
		self.title_msc = msc.TitleMenu()
		self.title_msc.play()

		self.background = self.title_srf.main_background
		self.button_list = self.title_srf.get_buttons()

		self.events = evt.TitleMenu(loop, self.button_list)

	def update(self):
		"""Update."""
		srf.main_screen.blit(self.background, (0, 0))

		self.button_list.update()
		self.button_list.draw(srf.main_screen)

	def event(self, event):
		"""Appel des évènements."""
		self.events.test_events(event)

	def event_update(self):
		"""Appel les évènements simple indépendants aux controls."""
		pass


class SelectLevel:
	"""Le menu de selection de niveau du jeu."""

	def __init__(self, loop):
		"""Initialisation."""
		self.select_srf = srf.SelectLevel()
		self.select_msc = msc.SelectLevel()
		self.select_msc.play()

		self.background = self.select_srf.main_background
		self.sprite_list = self.select_srf.get_sprites()
		self.button_list = self.select_srf.get_map_buttons()

		self.events = evt.SelectLevel(loop, self.button_list)

	def update(self):
		"""Update."""
		srf.main_screen.blit(self.background, (0, 0))

		self.sprite_list.update()
		self.button_list.update()

		self.sprite_list.draw(srf.main_screen)
		self.button_list.draw(srf.main_screen)

	def event(self, event):
		"""Appel des évènements."""
		self.events.test_events(event)

	def event_update(self):
		"""Appel les évènements simple indépendants aux controls."""
		pass
