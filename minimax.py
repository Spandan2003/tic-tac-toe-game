import numpy as np
import pygame
import math

from pygame.locals import *

def eval(state):
    result = [  state[0] + state[1] + state[2],
                state[3] + state[4] + state[5],
                state[6] + state[7] + state[8],
                state[0] + state[3] + state[6],
                state[1] + state[4] + state[7],
                state[2] + state[5] + state[8],
                state[0] + state[4] + state[8],
                state[2] + state[4] + state[6]]
    if 3 in result:
        return 1
    elif -3 in result:
        return -1
    else:
        return 0

def display(arr, over=False):                       #Present game on screen. If over then don't show instructions for next move
    displ = ['X' if item == -1 else 'O' if item==1 else '_' for item in arr]
    if not over:
        print("Please enter the coordinates of your move in the following pattern:")
        print("0  1  2 \n3  4  5 \n6  7  8")
    for i in range(3):
        for j in range(3):
            print(displ[3*i+j], end = "    ")
        print()

def bestMove(state):
    term = eval(state)
    print("best start")
    display(state)
    if term!=0 or not 0 in state:
        return term, -1
    move = []
    for pos_move in range(9):
        if(state[pos_move]==0):
            move.append(pos_move)
    result = -10
    best = 0
    temp_state = state
    for m in move:
        temp_state[m] = 1
        nextres, nextmove = bestMove(-temp_state)
        (result, best) = max((-nextres, m), (result, best), key= lambda l: l[0])
        temp_state[m] = 0
    temp_state[best] = 1
    print("res = "+str(result)+"      move = "+str(best))
    return result, best



st  = np.asarray([1 , -1 , 1,
                  0 , 0 , 0,
                  -1 , 0 , -1])
display(st)
res, m = bestMove(st)
st[m] = 1
print("move="+str(m))
display(st)