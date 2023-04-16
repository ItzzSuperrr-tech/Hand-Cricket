import pygame
import tkinter

#Display
width=1080
height=720
pygame.display.set_caption("Hand cricket")
gamewindow = pygame.display.set_mode((width, height))

background = pygame.image.load("Spark.jpg")
backgroundupdate=pygame.transform.scale(background, (width,height))
hand=pygame.image.load('hand_sign_2.png')
handupdate = pygame.transform.scale(hand, (500,500))   

def main():
    exit_game=False
    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            gamewindow.blit(backgroundupdate, (0,0))
            gamewindow.blit(handupdate, (0,0))

            pygame.display.update()
    
if __name__=="__main__":
    main()