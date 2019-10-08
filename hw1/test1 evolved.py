import sys
import numpy as np
from graph_gen import *

def has_cycle(sets):
    # TODO
    # return True if the graph has cycle; return False if not
    while(len(sets) != 0):
        #print
        for i in range(len(sets)):
            for j in range(len(sets[i])):
                print("{:3s}".format("".join(str(sets[i][j]))), end = '')
            print('')
        for j in range(3 * len(sets[0])):
            print('-', end = '')
        print('')
        #

        for s in sets:
            if 1 not in s:
                return True
        idx = sets[0].index(1)
        correctRow = []
        for i in range(len(sets)):
            if sets[i][idx] == -1:
                correctRow.append(i)
        if len(correctRow) == 0:
            sets.pop(0)
            continue
        for i in correctRow:
            newRow = []
            for j in range(len(sets[i])):
                newRow.append(sets[0][j] + sets[i][j])
            print(newRow)
            sets.append(newRow)
        for j in range(3 * len(sets[0])):
            print('-', end = '')
        print('')
        sets.pop(0)
    return False

def main():
    sets1=[]
    for n in range (5):
        sets1.append([0]*4)
    sets1[0][3]=1
    sets1[0][2]=-1
    sets1[1][0]=1
    sets1[1][1]=-1
    sets1[2][2]=1
    sets1[2][0]=-1
    sets1[3][3]=1
    sets1[3][1]=-1
    sets1[4][3]=1
    sets1[4][0]=-1
    if has_cycle(sets1):
        print('Yes')
    else:
        print('No')
    sets2=[]
    for n in range (4):
        sets2.append([0]*4)
    sets2[0][2]=1
    sets2[0][0]=-1
    sets2[1][0]=1
    sets2[1][1]=-1
    sets2[2][1]=1
    sets2[2][2]=-1
    sets2[3][1]=1
    sets2[3][3]=-1
    if has_cycle(sets2):
        print('Yes')
    else:
        print('No')
    sets3=[]
    for n in range (4):
        sets3.append([0]*4)
    sets3[0][2]=1
    sets3[0][0]=-1
    sets3[1][3]=1
    sets3[1][2]=-1
    sets3[2][1]=1
    sets3[2][3]=-1
    sets3[3][1]=1
    sets3[3][2]=-1
    if has_cycle(sets3):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
