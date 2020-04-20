#coding: utf-8
import time
import pygame
from pygame.locals import *

#Raffraichissement de la fenêtre
def refresh(dictionnaire):
	dictionnaire["fenetre"].blit(dictionnaire["player"],(dictionnaire["player_cord"]))
	dictionnaire["fenetre"].blit(dictionnaire["tuyaux_haut"][0],(dictionnaire["tuyaux_haut"][1]))
	dictionnaire["fenetre"].blit(dictionnaire["tuyaux_bas"][0],(dictionnaire["tuyaux_bas"][1]))
	pygame.display.flip()

#L'oiseau avance
def avanceTuyaux(dictionnaire):
	#dictionnaire["tuyaux_x"] = [tuyaux_x, tuyaux_cord_x]
	tuyaux_cord_haut = dictionnaire["tuyaux_haut"][1]
	tuyaux_cord_bas = dictionnaire["tuyaux_bas"][1]
	tuyaux_cord_haut[0] -= 5
	tuyaux_cord_bas[0] -= 5
	dictionnaire["tuyaux_haut"][1] = tuyaux_cord_haut
	dictionnaire["tuyaux_bas"][1] = tuyaux_cord_bas
	refresh(dictionnaire)

#Les tuyaux avancent
def avanceOiseau(dictionnaire, cord):
	player_cord = dictionnaire["player_cord"]
	player_cord[0] += cord[0]
	player_cord[1] += cord[1]
	dictionnaire["player_cord"] = player_cord
	refresh(dictionnaire)

#Téléportation directe de l'oiseau
def setOiseauCord(dictionnaire, cord):
	dictionnaire["player_cord"] = cord
	refresh(dictionnaire)

def main():
	pygame.init()
	fenetre = pygame.display.set_mode((900,428))
	pygame.display.set_caption("Fla-py Bird !")
	#--
	#10/02/2020
	fond = pygame.image.load("images/background.jpg").convert()
	player = pygame.image.load("images/playerbird.png").convert_alpha()
	tuyaux_haut = pygame.image.load("images/pipeNorth.png").convert_alpha()
	tuyaux_bas = pygame.image.load("images/pipeSouth.png").convert_alpha()
	#tuyaux_cord = [[coordonnées du tuyaux du haut],[coordonnées du tuyaux du bas]]
	tuyaux_cord = {"tuyaux_cord_haut":[425,-100],"tuyaux_cord_bas":[425,250]}
	player_cord = [0,214]
	fenetre.blit(fond,(0,0))
	fenetre.blit(player,(player_cord))
	fenetre.blit(tuyaux_haut, (tuyaux_cord["tuyaux_cord_haut"]))
	fenetre.blit(tuyaux_bas, (tuyaux_cord["tuyaux_cord_bas"]))
	pygame.display.flip()
	dictionnaire = {"game":1,"game_statut":False,"player":player,"player_cord":player_cord,"fenetre":fenetre,"tuyaux_haut":[tuyaux_haut,tuyaux_cord["tuyaux_cord_haut"]],"tuyaux_bas":[tuyaux_bas,tuyaux_cord["tuyaux_cord_bas"]]}
	#--
	#24/02/2020
	while dictionnaire["game"]:
		#Si le jeu est actif alors
		if dictionnaire["game_statut"] == True:
			dictionnaire["fenetre"].blit(fond,(0,0))
			time.sleep(.1)
			#Si l'oiseau n'est pas à la valeur maximale de la fenêtre
			if dictionnaire["player_cord"][1] > 0:
				avanceOiseau(dictionnaire, [0,5])
				avanceTuyaux(dictionnaire)
			#Sinon on le téléporte dans la fenêtre
			else:
				setOiseauCord(dictionnaire, [dictionnaire["player_cord"][0],1])
			#Si il n'est pas dans la fenêtre (en bas)
			if dictionnaire["player_cord"][1] > 388:
				#Le Jeu s'arrête
				dictionnaire["game"] = 0
		#Récupération de toute les entrées d'événements liés à pygame
		for event in pygame.event.get():
			#Si l'évent est de quitter alors on quitte
			if event.type == QUIT:
				#Le Jeu s'arrête
				dictionnaire["game"] = 0
			#Sinon si c'est la TOUCHE ESPACE
			elif event.type == KEYDOWN:
				if event.key == K_SPACE:
					#Si le jeu n'est pas actif
					if dictionnaire["game_statut"] == False:
						#Début de la partie
						dictionnaire["game_statut"] = True
						avanceOiseau(dictionnaire, [100,0])
					#Sinon
					else:
						avanceOiseau(dictionnaire, [0,-20])
	#--
main()
