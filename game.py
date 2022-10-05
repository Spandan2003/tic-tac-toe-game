#import pygame
import numpy

def humanmov(mov):
    human.append(mov)
    arr[mov] = -1
    for i in range(len(win)):
        if mov in win[i]:
            win.remove(win[i])
            i-=1
    for i in win2:
        if mov in i:
            win2.remove(win[i])
    for i in range(len(neut)):
        j = neut[i]
        if mov in neut[i]:
            neut.remove(neut[i])
            j.remove(mov)
            lose.append(j)
            i-=1
    for i in range(len(lose)):
        j = lose[i]
        if mov in lose[i]:
            lose.remove(lose[i])
            j.remove(mov)
            lose2.append(j)
            i-=1
    for i in range(len(lose2)):
        j = lose2[i]
        if mov in lose2[i]:
            lose2.remove(lose2[i])
            j.remove(mov)
            lose3.append(j)

def compmov(mov):
    comp.append(mov)
    arr[mov] = 1
    for i in range(len(lose)):
        if mov in lose[i]:
            lose.remove(lose[i])
            i-=1
    for i in range(len(lose2)):
        if mov in i:
            lose2.remove(lose2[i])
    for i in range(len(neut)):
        j = neut[i]
        if mov in neut[i]:
            neut.remove(neut[i])
            j.remove(mov)
            win.append(j)
    for i in range(len(win)):
        j = win[i]
        if mov in win[i]:
            win.remove(win[i])
            j.remove(mov)
            win2.append(j)
    for i in range(len(win2)):
        j = win2[i]
        if mov in win2[i]:
            win2.remove(win2[i])
            j.remove(mov)
            win3.append(j)

def match(human, comp):
    if(len(win2)>0):
        return win2[0][0]
    if(len(lose2)>0):
        return lose2[0][0]
    if(len(win)>0):
        return win[0][0]
    if(len(lose)>0):
        return lose[0][0]
    return neut[0][0]
        
def display(arr):
    displ = ['><' if item == -1 else 'O' if item==1 else '_' for item in arr]
    for i in range(3):
        for j in range(3):
            print(displ[3*i+j], end = "    ")
        print()

arr =  [0 for i in range(9)] 
# [0 1 2
#  3 4 5
#  6 7 8]
neut = [[0,1,2], [3,4,5], [6,7,8],   #horizontal win positions
        [0,3,6], [1,4,7], [2,5,8],  #vertical win positions
        [0,4,8], [2,4,6]]           #diagonal win positions
win = []
win2 = []
win3 = []
lose = []          
lose2 = []
lose3 = []
human = []
comp = []
compmov(4)
while(True):
    display(arr)
    mov = int(input())
    humanmov(mov)
    if(len(lose3)>0):
        print("YOU WON")
        break
    nextmove = match(human, comp)
    compmov(nextmove)
    if(len(win3)>0):
        print("Better luck Next Time")
        break
    if(not 0 in arr):
        print("A draw")
        break
    
display(arr)
print("END")

