#coding: utf-8
import time
import pygame
from pygame.locals import *

pygame.init()
fenetre = pygame.display.set_mode((900,428))
pygame.display.set_caption("Fla-py Bird !")
fond = pygame.image.load("images/background.jpg").convert()
player = pygame.image.load("images/playerbird.png").convert_alpha()
player_cord = [0,214]
fenetre.blit(fond,(0,0))
fenetre.blit(player,(player_cord))
pygame.display.flip()
game = 1
game_statut = False
while game:
	if game_statut == True:
		fenetre.blit(fond,(0,0))
		time.sleep(.1)
		y = player_cord[1]+6
		player_cord = [x,y]
	if player_cord[1] < 1:
		y = 1
		player_cord = [x,y]
		fenetre.blit(player,(player_cord))
	else:
		fenetre.blit(player,(player_cord))
		if player_cord[1] > 389:
			game= 0
	for event in pygame.event.get():
		if event.type == QUIT:
			game = 0
		if event.type == KEYDOWN:
			game_statut = True
			if event.key == K_SPACE:
				if player_cord < 250:
					x = player_cord[0]+20
				else:
					x = 250
					y = player_cord[1]-50
					player_cord = [x,y]
	pygame.display.flip()
