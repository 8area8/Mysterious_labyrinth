"""Le fichier 'data' centre les données externes du jeu."""

import glob
import pickle
import os
"""Imports."""


class Data():
	"""CLasse regroupant les données externes."""

	file = None

	core_lab = []

	def import_file(cls):
		"""Importe un fichier de labyrinthe dans la liste 'core_lab'.

		1 - ouvre le fichier
		2 - Ajoute chaque ligne du fichier, en enlevant le retour de ligne.
		3 - retourne la liste ainsi faite.
		"""
		cls.core_lab = []

		with open(Data.file) as f:
			for line in f:
				Data.core_lab.append(list(line))

				if '\n' in Data.core_lab[-1]:
					Data.core_lab[-1].remove('\n')
		return Data.core_lab
	import_file = classmethod(import_file)

	def list_map_files(cls):
		"""Affiche les fichiers du dossier core_maps.

		1 - appel le module glob pour lister les fichiers.
		2 - on enlève le chemin et l'extention des noms ainsi listés.
		3 - on crée deux listes:
			-une qui représente un livre
			-une qui représente les pages, qui contiennent les
			noms des fichiers précedemment listés.
			chaque page contiendra cinq noms.
		4 - on retourne le livre.
		"""
		file_list = glob.glob('core_maps/*.txt')

		for i, file in enumerate(file_list):
			file = file[10:-4]
			file_list[i] = file

		page = []
		book = []
		file_per_page = 0

		for file in file_list:
			page.append(file)
			file_per_page += 1

			if file_per_page == 5:
				book.append(page)
				file_per_page = 0
				page = []

		if page:
			book.append(page)

		return book
	list_map_files = classmethod(list_map_files)

	def save(cls, hero_pos, map_name):
		"""Sauvegarde."""
		datas = SaveData(hero_pos, map_name)

		with open('save', 'wb') as save_file:
			pckl = pickle.Pickler(save_file)
			pckl.dump(datas)
	save = classmethod(save)

	def load(cls):
		"""Chargement."""
		with open('save', 'rb') as load_file:
			pckl = pickle.Unpickler(load_file)
			return pckl.load()
	load = classmethod(load)

	def erase_save(cls):
		"""Ecrase la sauvegarde."""
		if os.path.isfile('save'):
			os.remove('save')
	erase_save = classmethod(erase_save)


class SaveData:
	"""Classe qui retiens les données à sauvegarder."""

	def __init__(self, hero_pos, map_name):
		"""Initialisation."""
		self.hero_pos = hero_pos
		self.map_name = map_name
