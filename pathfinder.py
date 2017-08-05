"""Trouve les cases possibles en fonction des points de mouvement du joueur."""

import pygame

import constants as cst


class Case:
	"""Une case."""

	def __init__(self, position, parent=None):
		"""Initialisation.

		possède une position abstraite,
		éventuellement une case parente,
		et possiblement une apparence.
		"""
		self.position = position
		self.x, self.y = position

		self.parent = parent

		self.image = None
		self.rect = None
		self.pos = None

	def get_img(self):
		"""Initialise les images.

		Utile pour afficher le chemin.
		"""
		self.image = pygame.image.load('img/moove.png').convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.x, self.rect.y = self.x * cst.IMG_SIZE, self.y * cst.IMG_SIZE
		self.pos = (self.rect.x, self.rect.y)


class DisplayPath:
	"""Affiche le chemin.

	Classe très simple, qui permet d'afficher le chemin
	en créant les images de chaque case du chemin, et en
	les affichant. Elle est appelé depuis le fichier Game.
	"""

	def __init__(self):
		"""Initialisation."""
		self.case_list = []

	def draw(self, path, surface):
		"""Update."""
		if path and path.case_list:
			self.case_list = path.case_list

			for case in self.case_list:
				case.get_img()
				surface.blit(case.image, case.pos)


class PathController:
	"""Trouve un chemin selon le Pathfinder et les choix du joueur."""

	def __init__(self, game_map):
		"""Initialisation de l'instance."""
		self.path = Path()

		self.mouse_case = Case((-1, -1))

		self.max_mp = 0
		self.current_mp = 0

		self.map = game_map

		self.cases_pathfinder = []
		self.path_quality = []
		self.display = DisplayPath()

	def test_path(self, current_hero, x, y):
		"""Met à jour le PathController (méthode principale!).

		1: Teste si la souris pointe sur la map ou si elle pointe sur la
			même case que précedement.
		2: On teste le héro courant (intutile dans cette version du jeu).
		3: on initialise les variables pour préparer les vrais calculs.
		4: on teste si on a un chemin, et qu'on revient en arrière. Si c'est
			le cas, alors on enlève une case au chemin.
		5: on teste si on avance d'une case. Si oui, on ajoute une case au
			chemin.
		6: Sinon, c'est que la souris pointe ailleurs. On réinitialise le
			chemin et on appel la méthode qui va tester tous les chemins
			possibles et voir si la souris pointe sur une des cases d'un
			chemin. Si oui, on créera ce chemin.
		"""
		self.cases_pathfinder = []
		if x is None and y is None or (x, y) == self.mouse_case.position:
			return

		if not self.path.hero or self.path.hero.name != current_hero.name:
			self.path = Path(hero=current_hero)

		self.mouse_case = Case((x, y))
		self.max_mp = current_hero.moves_point
		self.current_mp = self.max_mp - self.path.distance()

		if self.path.case_list and len(self.path.case_list) > 1:
			if self.path.case_list[-2].position == self.mouse_case.position:
				self.path.case_list = self.path.case_list[:-1]
				return

		if self.current_mp > 0 and self.test_next_case():
			self.path.case_list.append(self.mouse_case)
			return

		self.path.case_list = []
		self.current_mp = current_hero.moves_point

		self.start_pathfinder(self.mouse_case)

	def test_next_case(self):
		"""Test l'ajout d'une case au path.

		1: on teste si on a un chemin en cours. Si oui, alors la case
			teste partira de ce chemin, sinon elle partira du héro.
		2: on teste les cases adjacentes à la case teste.
		3: si on a des cases possibles, on teste si la souris pointe sur
			une de ces cases. Si oui, on retourne Vrai.
		"""
		if self.path.case_list:
			test_case = self.path.case_list[-1]
			if len(self.path.case_list) > 1:
				parent = self.path.case_list[-2]
			else:
				parent = None
		else:
			test_case = Case(self.path.hero.position)
			parent = None

		possibles_cases = self.get_possibles_cases(test_case, parent=parent)

		if possibles_cases:
			for case in possibles_cases:
				if case.position == self.mouse_case.position:
					return True
		return False

	def get_possibles_cases(self, case, parent=None):
		"""Renvoit les mouvements possibles depuis une case.

		1: On crée 4 positions qui correspondent au nord, sud, est et ouest.
		2: pour chaque position, on teste si c'est pas un mur, la case du héro,
			ou la case parent à la case teste (si on retourne pas sur nos pas).
		3: si tout les testes sont bon, on ajoute la case dans une liste qu'on
			retourne à la fin.
		"""
		x, y = case.position

		possibles_mooves = []

		possibles_mooves.append((x + 1, y))
		possibles_mooves.append((x - 1, y))
		possibles_mooves.append((x, y + 1))
		possibles_mooves.append((x, y - 1))

		possibles_cases = []

		for position in possibles_mooves:
			if position in self.map and self.map[position].solid:
				continue
			if parent and parent.position == position:
				continue
			if position == self.path.hero.position:
				continue
			# les 7 prochaines lignes sont sales...
			if self.path.case_list:
				bool_test = False
				for case in self.path.case_list:
					if position == case.position:
						bool_test = True
				if bool_test:
					continue

			possibles_cases.append(Case(position, parent=case))

		return possibles_cases

	def start_pathfinder(self, destination):
		"""Calcul un chemin d'après une destination.

		1: on test si la souris pointe sur le héro.
		2: on teste les cases possibles qu'on ajoute à 'case-list'.
		3: si on a trouvé des cases, on va tester si une des cases correspond
			à celle du curseur, et si c'est le cas on remonte jusqu'au héro.
			'path_quality' est une variable de transition qui permet de
			trouver le chemin le plus court parmis les chemins possibles.
		"""
		self.cases_pathfinder = []
		if destination.position == self.path.hero.position:
			return

		self.get_possibles_paths(Case(self.path.hero.position), self.current_mp)

		if not self.cases_pathfinder:
			return

		self.path_quality = []
		for case in self.cases_pathfinder:
			if destination.position == case.position:
				self.get_destination_to_hero(case)
		if self.path_quality:
				self.path_quality = sorted(self.path_quality, key=lambda paths: len(paths))
				self.path.case_list = self.path_quality[0]

	def get_destination_to_hero(self, destination):
		"""Trace le chemin depuis la destination jusqu'au héro.

		1: On remonte de case en case jusqu'à trouver celle qui
			correspond à la position du héro (donc la case du héro).
			Pour chaque case trouvé, on l'ajoute dans une liste, que
			l'on inverse à la fin (car on part de la dernière à la première).
		"""
		case = destination
		path = []
		path.append(case)
		while case.parent.position != self.path.hero.position:
			case = case.parent
			path.append(case)
		path.reverse()
		self.path_quality.append(path)

	def get_possibles_paths(self, case_test, current_mp):
		"""Calcul récursif.

		1: On teste les cases adjacente à la case du héro.
		2: Pour chaque case trouvé, on l'ajoute dans une liste,
			on enlève un point de mouvement (pour tenir compte
			du mouvement max du héro), et on refait le même
			teste avec la case trouvé comme case teste.
		"""
		parent = None
		if case_test.parent:
			parent = case_test.parent
		possibles_cases = self.get_possibles_cases(case_test, parent)

		current_mp -= 1
		for case in possibles_cases:
			self.cases_pathfinder.append(case)
			if current_mp > 0 and possibles_cases:
				self.get_possibles_paths(case, current_mp)


class Path:
	"""La classe chemin."""

	def __init__(self, hero=None):
		"""Initialisation.

		Classe très basique, renferme l'objet hero
		et une liste qui contiend le chemin trouvé.
		"""
		self.hero = hero
		self.case_list = []

	def distance(self):
		"""Retourne la taille de case_list."""
		if self.case_list:
			return len(self.case_list)
		return 0
