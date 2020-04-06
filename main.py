#coding: utf-8
import time
import pygame
from pygame.locals import *

def refresh(dictionnaire):
	dictionnaire["fenetre"].blit(dictionnaire["player"],(dictionnaire["player_cord"]))
	pygame.display.flip()

def avance(dictionnaire, cord):
	player_cord = dictionnaire["player_cord"]
	player_cord[0] += cord[0]
	player_cord[1] += cord[1]
	dictionnaire["player_cord"] = player_cord
	refresh(dictionnaire)

def main():
	pygame.init()
	fenetre = pygame.display.set_mode((900,428))
	pygame.display.set_caption("Fla-py Bird !")
	#--
	#10/02/2020
	fond = pygame.image.load("images/background.jpg").convert()
	player = pygame.image.load("images/playerbird.png").convert_alpha()
	player_cord = [0,214]
	fenetre.blit(fond,(0,0))
	fenetre.blit(player,(player_cord))
	pygame.display.flip()
	dictionnaire = {"game":1,"game_statut":False,"player":player,"player_cord":player_cord,"fenetre":fenetre}
	#--
	#24/02/2020
	while dictionnaire["game"]:
		if dictionnaire["game_statut"] == True:
			dictionnaire["fenetre"].blit(fond,(0,0))
			time.sleep(.1)
			avance(dictionnaire, [20,0])
		for event in pygame.event.get():
			if event.type == QUIT:
				dictionnaire["game"] = 0
			elif event.type == KEYDOWN:
				if event.key == K_SPACE:
					if dictionnaire["game_statut"] == False:
						dictionnaire["game_statut"] = True
						avance(dictionnaire, [20,0])
					else:
						avance(dictionnaire, [0,20])
	#--
main()
