import pygame

from pygame.locals import *

def getPos(move):
    x = recta.centerx -8*l + (move%3)*8*l
    y = recta.centery -8*l + (move//3)*8*l
    return x,y



sizeOfWin = (720, 480)
l = 10

pygame.init()
pygame.display.set_caption("Tic Tac Toe")
canvas = pygame.display.set_mode(sizeOfWin)
img = pygame.transform.scale(pygame.image.load("background.jpg"), sizeOfWin)
recta = pygame.Rect(0,0,26*l,26*l)
recta.centerx, recta.centery = sizeOfWin[0]//2, sizeOfWin[1]//2
lineArrS = [[recta.centerx-12*l,recta.centery-4*l], [recta.centerx-12*l,recta.centery+4*l], [recta.centerx-4*l,recta.centery-12*l], [recta.centerx+4*l,recta.centery-12*l]]
lineArrE = [[recta.centerx+12*l,recta.centery-4*l], [recta.centerx+12*l,recta.centery+4*l], [recta.centerx-4*l,recta.centery+12*l], [recta.centerx+4*l,recta.centery+12*l]]

canvas.blit(img, (0, 0))
pygame.draw.rect(canvas, "white", recta)
for i in range(len(lineArrS)):
    pygame.draw.line(canvas, "black", lineArrS[i], lineArrE[i], width=5)

gameOn = True
while gameOn:
    # for loop through the event queue
    
    for event in pygame.event.get():
         
        # Check for KEYDOWN event
        if event.type == KEYDOWN:
             
            # If the Backspace key has been pressed set
            # running to false to exit the main loop
            if event.key == K_BACKSPACE:
                gameOn = False
                 
        # Check for QUIT event
        elif event.type == QUIT:
            gameOn = False
    
    # Update the display using flip
    pygame.display.flip()