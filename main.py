# coding: utf-8
import pygame
from pygame.locals import *

pygame.init()
fenetre = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Fla-py Bird !")
fond = pygame.image.load("images/background.jpg").convert()
pygame.display.flip()
continuer = 1
while continuer:
	for event in pygame.event.get():
		if event.type == QUIT:
			continuer = 0
	
	fenetre.blit(fond, (0,0))	
	pygame.display.flip()
