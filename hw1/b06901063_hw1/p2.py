import sys
import numpy as np
from graph_gen import *

def has_cycle(sets):
    originSet = np.mat(sets)
    arraySet = np.mat(sets)
    for i in sets:
        arraySet = arraySet.dot(originSet)
        if arraySet.diagonal().tolist()[0] != [0 for i in range(len(sets))]:
            return True
        else:
            continue
    # TODO
    # return True if the graph has cycle; return False if not

    return False

def main():
    p2_list = list()
    if len(sys.argv) <= 1:
        p2_list = get_p2('r07')
    else:
        p2_list = get_p2(sys.argv[1])
    '''
    if has_cycle(p2_list[6]):
        print('Yes')
    else:
        print('No')
    '''
    for sets in p2_list:
        '''for i in range(len(sets)):
            for j in range(len(sets[i])):
                print("{:3s}".format("".join(str(sets[i][j]))), end = '')
            print('')'''
        '''
          HINT: You can `print(sets)` to show what the matrix looks like
            If we have a directed graph with 2->3 4->1 3->5 5->2 0->1
                   0  1  2  3  4  5
                0  0  1  0  0  0  0
                1  0  0  0  0  0  0
                2  0  0  0  1  0  0
                3  0  0  0  0  0  1
                4  0  1  0  0  0  0
                5  0  0  1  0  0  0
            The size of the matrix is (6,6)
        '''
        
        if has_cycle(sets):
            print('Yes')
        else:
            print('No')
        

if __name__ == '__main__':
    main()
