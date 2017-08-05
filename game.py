"""Gère la partie propre au jeu."""

import cartography as carto
import entity
import case_entity

import surfaces as srf
import musics as msc
import events as evt
import pathfinder as ptfd
"""Imports."""


class Game:
	"""La classe qui lance le jeu à proprement parler."""

	def __init__(self, loop, map_name, load=None):
		"""Initialisation."""
		self.loop = loop

		self.game_msc = msc.Game()  # musique
		self.game_msc.play()

		self.entity = entity.GroupEntity()  # image personnage
		self.case_entity = case_entity.CaseEntityGroup()  # image labyrinthe

		self.map = carto.Map(map_name, self.entity, self.case_entity)  # la carte
		self.coords = self.map.coords  # les coordonnées de la carte

		self.load(load)  # si chargement, on charge les données.

		self.game_srf = srf.Game()  # images menus, boutons, etc.
		self.background = self.game_srf.background
		self.victory = self.game_srf.get_vict()
		self.sprite_grp = self.game_srf.get_sprites()
		self.button_list = self.game_srf.get_button_list()
		self.btm, self.btm_txt = self.game_srf.get_back_to_main()
		self.draw_sprite = [False, False]

		self.map_surface = self.game_srf.get_map_surface(self.map.size)  # surface
		self.camera_screen = self.game_srf.get_camera_screen(self.map_surface)  # cam

		self.pathfinder = ptfd.PathController(self.coords)  # le trouveur de chemins
		self.events = evt.Game(
			loop, map_name, self.camera_screen, self.pathfinder,
			self.entity.hero, self.sprite_grp, self.button_list,
			self.draw_sprite, self.btm_txt, self.coords, self.game_msc)  # évènements

		self.camera_screen.recenter_hero(self.entity.hero, start=True)

	def update(self):
		"""Update.

		On met à jour et dessine les différents
		groupes d'images (sprites), ainsi que la caméra.

		draw_sprite est une liste peu lisible qui permet
		d'afficher le menu de retour en arrière ou l'animation
		de victoire (en fonction des booléens contenus).
		"""
		srf.main_screen.blit(self.background, (0, 0))

		self.camera_screen.surface.fill((0, 0, 0))

		self.case_entity.group.update()
		self.entity.group.update()

		self.case_entity.group.draw(self.map_surface)
		self.pathfinder.display.draw(self.pathfinder.path, self.map_surface)
		self.entity.group.draw(self.map_surface)

		self.camera_screen.recenter_hero(self.entity.hero)
		self.camera_screen.update()
		srf.main_screen.blit(self.camera_screen.surface, (0, 0))

		self.sprite_grp.update()
		self.button_list.update()
		self.sprite_grp.draw(srf.main_screen)
		self.button_list.draw(srf.main_screen)

		if self.draw_sprite[0]:
			self.btm.update()
			self.btm_txt.update()
			self.btm.draw(srf.main_screen)
			self.btm_txt.draw(srf.main_screen)
		if self.draw_sprite[1]:
			self.victory.update()
			self.victory.draw(srf.main_screen)

	def event(self, event):
		"""Evènements."""
		self.events.test_events(event)

	def event_update(self):
		"""Appel les évènements simple indépendants aux controls."""
		self.events.update_events()

	def load(self, load):
		"""Chargement d'une map."""
		if load:
			x, y = load.hero_pos
			self.entity.create_hero(x, y)
