import pygame
import os
import traceback
import time
from pygame.locals import *
pygame.init()
# Couleurs que nous utilisons dans ce programme
GRIS = (221, 221, 221)
NOIR = (0, 0, 0)
BLANC = (255, 255, 255)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)
BLEU = (0, 0, 255)
BLEUC = (112, 193, 237)
BLEUF = (18, 98, 141)
#music dans le jeu
pygame.mixer.music.load('Clarv-ArcadeMode.mp3')  #Charge la musique
pygame.mixer.music.play(-2) #the music will play and repeat indefinitely
def menu():
    fenetre.fill((255,255,255))
    play=pygame.image.load("play.jpg").convert_alpha()
    fenetre.blit(play,(420,150))
    pygame.display.flip()
    continuer=1
    for event in pygame.event.get():
         if event.type==QUIT: #un moyen de sortir de la boucle
            continuer=0
    while continuer==1:
        for event in pygame.event.get():
         if event.type==KEYDOWN:
            if event.key==K_RETURN:#lance le jeu (fct game)
                game()
            if event.key==K_o:#lance les options (fct option)
                option()
         if event.type==QUIT: #un moyen de sortir de la boucle
            continuer=0

def option():
    fenetre.fill((255,255,255))
    option=pygame.image.load("option.jpg")
    fenetre.blit(option,(420,200))
    pygame.display.flip()
    continuer=1
    while continuer==1:
        for event in pygame.event.get():
            if event.type==QUIT: #un moyen de sortir de la boucle
                continuer=0
            if event.type==KEYDOWN:
                if event.key==K_KP_PLUS:#augmente le son en appuyant sur la touche +
                    a=pygame.mixer.music.get_volume()
                    b=a+0.1
                    pygame.mixer.music.set_volume(b)
                if event.key==K_KP_MINUS:#augmente le son en appuyant sur la touche -
                    a=pygame.mixer.music.get_volume()
                    b=a-0.1
                    pygame.mixer.music.set_volume(b)
                if event.key==K_s:#met pause a la music
                    pygame.mixer.music.pause() #Met la musique en pause
                if event.key==K_p:#met pause a la music
                    pygame.mixer.music.unpause() #Reprend la musique là où elle a été coupée
                if event.key==K_ESCAPE:#quitte l'option retourne au menu
                    menu()

def game():
    fenetre.fill((255,255,255))
    pygame.display.flip()
    joueur1=1
    joueur2=1
    continuer=1
    for event in pygame.event.get():
            if event.type==QUIT:
                continuer=0



def obstacles():
    return obstacles
def victoire():
    fenetre.fill((255,255,255))
    if joueur1==0 and joueur2==1:
        Winjoueur1=pygame.image.load("Winjoueur1.jpg")
        fenetre.blit(Winjoueur1,(420,150))
        print("victoire Player 2")
    if joueur2==0 and joueur1==1:
        Winjoueur2=pygame.image.load("Winjoueur2.jpg")
        fenetre.blit(Winjoueur2,(420,150))
        print("victoire Player 1")
    else:
        egalite=pygame.image.load("egalite.jpg")
        fenetre.blit(egalite,(420,150))

try:
    os.environ['SDL_VIDEO_WINDOW_POS']="400,600"
    fenetre=pygame.display.set_mode((1280,600))
    pygame.display.set_caption("FriendsFunRun")#ce bloc donne un titre a la fenetre
    jeu_actif=True
    continuer=1
    fenetre.fill((255,255,255)) #on remplit la fenêtre de blanc
         #MENU bouton play
    play=pygame.image.load("play.jpg")
    fenetre.blit(play,(420,150))
    pygame.display.flip()
    continuer=1

    while continuer==1:
        for event in pygame.event.get():
         if event.type==KEYDOWN:
            if event.key==K_RETURN:#lance le jeu (fct game) et la détection de victoire
                game()
                #victoire()
            if event.key==K_o:#lance les options (fct option)
                option()
         if event.type==QUIT: #un moyen de sortir de la boucle
            continuer=0





except :
    traceback.print_exc() #ce bloc permet de récupérer des infos en cas d'erreur
finally:
    pygame.quit()
exit()
