import pygame
import math

from pygame.locals import *

def getPos(move):
    x = recta.centerx -8*l + (move%3)*8*l
    y = recta.centery -8*l + (move//3)*8*l
    return x,y

def dell(X, basket):                                 #Remove all items in basket from list X
    for i in basket:
        X.remove(i)
    return X

def humanmov(mov):                                  #Comprehend the human's Move
    global lose, lose2, lose3, win, win2, win3, neut
    human.append(mov)
    arr[mov] = -1                                   #Update the move in arr and human list
    basket = []
    for i in range(len(win)):                       #If a human plays a move which blocks a winning path, then remove all such paths from win and win2
        if mov in win[i]:
            basket.append(win[i])
    win = dell(win, basket)
    basket = []
    for i in range(len(win2)):
        if mov in win2[i]:
            basket.append(win2[i])
    win2 = dell(win2, basket)
    basket = []
    for i in range(len(neut)):                      #If path is in neut and human plays a move in it then shift it to lose while deleting from neut
        j = neut[i]
        if mov in neut[i]:
            j.remove(mov)
            lose.append(j)
            basket.append(neut[i])
    neut = dell(neut, basket)
    basket = []
    for i in range(len(lose)):                       #If path already has a move played by human and human plays another move then shift it to lose2
        j = lose[i]
        if mov in lose[i]:
            j.remove(mov)
            lose2.append(j)
            basket.append(lose[i])
    lose = dell(lose, basket)
    basket = []
    for i in range(len(lose2)):                     #If path already has 2 moves played by human and human plays another move then shift it to lose3
        j = lose2[i]                                #Lose 3 being non empty denotes AI has lost
        if mov in lose2[i]:
            j.remove(mov)
            lose3.append(j)
            basket.append(lose2[i])
    lose2 = dell(lose2, basket)
    basket = []

def compmov(mov):                                   #Comprehend the AI's Move
    global lose, lose2, lose3, win, win2, win3, neut
    comp.append(mov)                                #Update the move in arr and comp list
    arr[mov] = 1
    basket = []
    for i in range(len(lose)):                      #If the AI plays a move which blocks a winning path for human, then remove all such paths from lose and lose2
        if mov in lose[i]:
            basket.append(lose[i])
    lose = dell(lose, basket)
    basket = []
    
    for i in range(len(lose2)):                     
        if mov in lose2[i]:
            basket.append(lose2[i])
    lose2 = dell(lose2, basket)
    basket = []
    for i in range(len(neut)):                      #If path is in neut and AI plays a move in it then shift it to win while deleting from neut
        j = neut[i]
        if mov in neut[i]:
            j.remove(mov)
            win.append(j)
            basket.append(neut[i])
    neut = dell(neut, basket)
    basket = []
    for i in range(len(win)):                       #If path already has a move played by AI and AI plays another move then shift it to win2
        j = win[i]
        if mov in win[i]:       
            j.remove(mov)
            win2.append(j)
            basket.append(win[i])
    win = dell(win, basket)
    basket = []
    for i in range(len(win2)):                      #If path already has 2 moves played by AI and AI plays another move then shift it to win3
        j = win2[i]                                 #Win3 being non empty denotes AI has won
        if mov in win2[i]:
            j.remove(mov)
            win3.append(j)
            basket.append(win2[i])
    win2 = dell(win2, basket)
    basket = []

def match(human, comp):                             #Decides which move AI should play next
    if(len(win2)>0):                                #First if we can win in 1 move make it,
        return win2[0][0]
    if(len(lose2)>0):                               #Second if we will lose in the nesst move prevent human from making it
        return lose2[0][0]
    if(len(win)>0):                                 #Third if no danger of losing, make a move taking in a direction towards win
        return win[0][0]
    if(len(lose)>0):                                #Fourth if no such move possible then make one blocking the human's winning path
        return lose[0][0]
    if(len(neut)>0):                                #Lastly make a move increasing our chances by a bit
        return neut[0][0]
    return arr.index(0)                             #If no move exists then take first possible move from 0,1,2,...7,8
        
def display(text, loc = (-1,-1)):                       #Present game on screen. If over then don't show instructions for next move
    if loc == (-1,-1):
        loc = (recta.centerx, recta.centery+12*l+(sizeOfWin[1]-recta.centery-12*l)//2)
    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    text_surface = my_font.render(text, False, (0, 0, 0))
    canvas.blit(text_surface, loc)

def cross(mov):
    rect1 = 2

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

arr =  [0 for i in range(9)] 
# [0 1 2
#  3 4 5
#  6 7 8]
# We start with all possible moves which can secure a win if played by single player.
# And put them all in neut (neutral). Leave rest lists empty
neut = [[0,4,8], [2,4,6],            #diagonal win positions
        [0,1,2], [3,4,5], [6,7,8],   #horizontal win positions
        [0,3,6], [1,4,7], [2,5,8]]   #vertical win positions
        
win = []
win2 = []
win3 = []
lose = []          
lose2 = []
lose3 = []
human = []
comp = []

over = False
gameOn = True
while gameOn:
    # for loop through the event queue
    
    for event in pygame.event.get():
         
        # Check for KEYDOWN event
        if event.type == KEYDOWN:
            # If the Escape key has been pressed set
            # running to false to exit the main loop
            if event.key == K_ESCAPE:
                gameOn = False
        if event.type == MOUSEBUTTONDOWN and not over:
            pos = pygame.mouse.get_pos()
            pos = ((pos[0] - recta.centerx + 12*l)/24/l , (pos[1] - recta.centery + 12*l)/24/l)
            if(0<=pos[0]<=2 and 0<=pos[1]<=2):
                mov = 3*math.floor(pos[1])+math.floor(pos[0])
                humanmov(mov)
                if(len(lose3)>0):
                    display("You WIN")
                    over = True
                    break
                nextmove = match(human, comp)                           #Calculate AI's best move and comprehend it
                compmov(nextmove)
                if(len(win3)>0):
                    display("You LOSE")
                    over = True
                    break
                if(not 0 in arr):                                       #No result and out of moves, we draw
                    display("A Draw")
                    over = True
                    break
        # Check for QUIT event
        elif event.type == QUIT:
            gameOn = False
    
    # Update the display using flip
    pygame.display.flip()