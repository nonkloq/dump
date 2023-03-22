from random import random,shuffle
import numpy as np 
import matplotlib.pyplot as plt


def diagonal_conflicts(i,state):
    conflict = 0
    # lower half 
    x = i
    k = l = state[x] 
    while 0<i:
        k-=1
        l+=1 
        if k>=0 and state[i-1] == k: conflict+=1
        if l<8 and state[i-1] == l: conflict+=1
        i-=1

    # upper half
    k = l = state[x]
    i = x
    while i<7:
        k-=1
        l+=1 
        if k>=0 and state[i+1] == k: conflict+=1
        if l<8 and state[i+1] == l: conflict+=1
        i+=1
    return conflict

def score(state):
    conflicts = 0
    h = {}
    # column conflicts (row conflicts are impossible in this state representation)
    for x in state:
        if x in h: h[x] +=1
        else: h[x] = 0

    for i in range(len(state)):
        conflicts += h[state[i]] + diagonal_conflicts(i,state)
    return conflicts


def min_neighbour(state):
    min_state = None 
    min_conflicts = float('inf')
    for i in range(8):
        for k in state[i]+1,state[i]-1:
            if k<0 or k>=8: continue
            temp,state[i] = state[i],k
            conflicts = score(state)
            if conflicts < min_conflicts or (conflicts == min_conflicts and random() >= .5): 
                min_state = list(state)
                min_conflicts = conflicts                
            state[i] = temp
    return min_state, min_conflicts
                


def hill_climbing(curr_state):
    curr_score = score(curr_state)
    while True:
        nxt_state,nxt_score = min_neighbour(curr_state) # best next neighbour
        
        if nxt_score == 0: # minima
            curr_state = nxt_state
            break

        if nxt_score >= curr_score: # plateu or local minima    
            shuffle(curr_state) # random restart    
            curr_score = score(curr_state)
        else: 
            curr_score = nxt_score
            curr_state = nxt_state
    return curr_state

def view_board(state):
    board = np.zeros([8,8], dtype=int)
    for i in range(len(state)):
        board[i][state[i]] = 1
    plt.figure()
    plt.imshow(board)
    plt.show()

initial_state = [1,1,1,1,1,1,1,1]
view_board(hill_climbing(initial_state))