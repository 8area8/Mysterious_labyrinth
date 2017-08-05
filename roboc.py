#! /usr/bin/env python3
# coding utf-8


"""Le fichier principal, initialise le jeu."""

import pygame

import loop
import constants
"""Imports."""

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()  # Initialisation

pygame.display.set_caption(constants.TITLE)  # On choisit un titre

loop.Loop()  # la classe la plus importante, elle fait tourner le jeu.
