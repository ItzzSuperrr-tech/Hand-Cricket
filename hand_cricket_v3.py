import random
import time
import sys
import pygame
from pygame.locals import *

#Game Variables
FPS=40

SCREENWIDTH= 1080
SCREENHEIGHT=720

SCREEN=pygame.display.set_mode((SCREENHEIGHT,SCREENWIDTH))

game_sprites={}
game_sounds={}
#player variable

#background and hand sign variables
backgruond='gallery/sprites/img23.jpg'

Title='gallery/sprites/title.png'
Title='gallery/sprites/bg-2.png'
titleload=pygame.image.load(Title)
Titleupdate=pygame.transform.scale(titleload, (SCREENHEIGHT,SCREENWIDTH))

hand_sign0='gallery/sprites/hand_sign_0.png'
hand_sign1='gallery/sprites/hand_sign_1.png'
hand_sign2='gallery/sprites/hand_sign_2.png'
hand_sign3='gallery/sprites/hand_sign_3.png'
hand_sign4='gallery/sprites/hand_sign_4.png'
hand_sign5='gallery/sprites/hand_sign_5.png'
hand_sign6='gallery/sprites/hand_sign_6.png'

battingscorebyplayer=0
bowlingscorebycomputer=0

player_throws_batting=0
computer_random_batting=0

player_throws_bowling=1
computer_random_bowling=1

#WELCOME SCREEN FUNCTION

def WelcomeScreen():
#player
    playerx=int(SCREENWIDTH/5)
    playery=int(SCREENHEIGHT-game_sprites['player'].get_height())
    player_flat_hand_x=int(playerx+100)
    player_flat_hand_y=int((playerx+100)-game_sprites['player_flat_hand'].get_height())
#computer
    computerx=int(SCREENWIDTH/10)
    computery=int(SCREENHEIGHT-game_sprites['player'].get_height())
    computer_flat_hand_x=int(computerx+100)
    computer_flat_hand_y=int((playerx+100)-game_sprites['player_flat_hand'].get_height())

    #Welcome Screen Title
    Titlex=int((SCREENWIDTH-game_sprites['Title'].getwidth())/2)
    Titley=int(SCREENHEIGHT*0.13)
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT or (event.type==KEYDOWN or event.key==K_ESCAPE):
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN and event.key==(K_SPACE):
                return
            else:
                SCREEN.blit(game_sprites['background'],(0,0))

                SCREEN.blit(game_sprites['Title'],(Titlex,Titley))
                pygame.display.update()
                FPSCLOCK.tick(FPS)

def player_batting_inning_1(x):
    player_throws_batting=int(input("Enter a number from 0-6: "))
    computer_random_batting=random.randrange(0-6)
    
if __name__=='__main__':
    pygame.init() #Initializes all pygame modules
    FPSCLOCK=pygame.time.Clock() #Control FPS for the game
    pygame.display.set_caption("Hand Cricket by Mahit Shah")
    game_sprites['hand_signs']=(
        pygame.image.load('gallery/sprites/hand_sign_1.png').convert_alpha(),
        pygame.image.load('gallery/sprites/hand_sign_2.png').convert_alpha(),
        pygame.image.load('gallery/sprites/hand_sign_3.png').convert_alpha(),
        pygame.image.load('gallery/sprites/hand_sign_4.png').convert_alpha(),
        pygame.image.load('gallery/sprites/hand_sign_5.png').convert_alpha(),
        pygame.image.load('gallery/sprites/hand_sign_6.png').convert_alpha()
    )

    game_sprites['Title']=pygame.image.load(Title).convert_alpha()
    game_sounds['game over']=pygame.mixer.sound('gallery/audio/')
    game_sounds['hand_beat']=pygame.mixer.sound('gallery/audio/')

    game_sprites['background']=pygame.image.load(backgruond).convert()


    while True:
        WelcomeScreen() #Shows the screen until any button is pressed
        maingame() #Main game function