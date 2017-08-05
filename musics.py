"""Fichier propre aux musiques du jeu."""

import pygame


class TitleMenu:
	"""Musiques de l'écran titre."""

	def play(self):
		"""Joue l'intro."""
		pygame.mixer.music.fadeout(400)
		pygame.mixer.fadeout(10)
		pygame.mixer.music.load('sound/intro.ogg')
		pygame.mixer.music.play(loops=-1)
		pygame.mixer.music.set_volume(1)


class SelectLevel:
	"""Musiques de la selection de niveaux."""

	def play(self):
		"""Joue la musique de ce menu."""
		pygame.mixer.music.fadeout(400)
		pygame.mixer.music.load('sound/Select_level.ogg')
		pygame.mixer.music.play(loops=-1)
		pygame.mixer.music.set_volume(0.4)


class Game:
	"""Musiques du jeu."""

	def __init__(self):
		"""Initialise les bruitages."""
		self.clap = pygame.mixer.Sound('sound/clap.wav')
		self.forest = pygame.mixer.Sound('sound/forest.ogg')

	def play(self):
		"""Joue la musique et les sons de forêt."""
		pygame.mixer.music.fadeout(400)
		pygame.mixer.music.load('sound/enchanted_forest.ogg')
		pygame.mixer.music.play(loops=-1)
		pygame.mixer.music.set_volume(1)
		self.forest.play(loops=-1)
		self.forest.set_volume(0.1)

	def play_victory(self):
		"""Joue la musique de victoire."""
		pygame.mixer.music.fadeout(400)
		pygame.mixer.music.load('sound/victory.wav')
		self.clap.play()
		self.clap.set_volume(0.8)
		pygame.mixer.music.play()
