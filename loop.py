"""La boucle prinicpale du jeu.

Tout se passe au sein de cette boucle.
"""

import pygame
from pygame.locals import *

import menus


class Loop:
	"""La classe constituant la boucle."""

	def __init__(self):
		"""Initialisation des variables et appel de la boucle.

		1 - x et y prennent la position de la souris pour les events.
		2 - clock prend le temps du jeu(fixe les FPS).
		3 - onclick test si on clic sur la souris ou non.
		4 - running permet de tester la boucle du jeu.

		5 - active_screen renvoit l'interface actuelle.
			Certainement la variable la plus importante, elle pourra
			contenir les différents menus comme le jeu en soi.

			On l'appelera pour les évènements et les mises à jours propre
			à l'interface contenue.

		6 - start appel la boucle du jeu.
		"""
		self.x, self.y = 0, 0

		self.clock = pygame.time.Clock()

		self.onclick = False
		self.running = True

		self.active_screen = menus.TitleMenu(self)

		self.start()

	def start(self):
		"""déclenche la boucle."""
		while self.running:
			self.x, self.y = pygame.mouse.get_pos()

			for event in pygame.event.get():  # boucle d'évènements.

				if event.type == QUIT:  # si on clique sur la croix
					self.running = False

				self.active_screen.event(event)  # appel des évènements.
			self.active_screen.event_update()  # appel des évènements bis.

			self.active_screen.update()  # mises à jours des éléments.
			pygame.display.flip()  # rafraichissement de l'écran.

			self.clock.tick(30)  # le jeu tourne à 30 FPS.
