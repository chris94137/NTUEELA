import sys
import numpy as np
import pandas as pd

def load(fname):
    f = open(fname, 'r').readlines()
    n = len(f)
    ret = {}
    for l in f:
        l = l.split('\n')[0].split(',')
        i = int(l[0])
        ret[i] = {}
        for j in range(n):
            if str(j) in l[1:]:
                ret[i][j] = 1
            else:
                ret[i][j] = 0
    ret = pd.DataFrame(ret).values
    return ret

def get_tran(g):
    # TODO
    count = []
    for i in g:
    	count.append(0)
    for i in g:
    	for j in range(len(i)):
    		if i[j] == 1:
    			count[j] += 1
    t = np.zeros((len(count), len(count)))
    for i in range(len(g)):
    	for j in range(len(g)):
    		if g[i][j] == 1:
    			t[i][j] = 1.0 / float(count[j])
    return t 


def cal_rank(t, d = 0.85, max_iterations = 1000, alpha = 0.001):
    # TODO
    iter = 0
    n = len(t)
    r = np.zeros((n, 1))
    print(t)
    for i in r:
    	i[0] = 1.0 / n
    x = (1-d) * r;
    while iter <= max_iterations:
    	r_2 = d * t.dot(r) + x
    	if dist(r_2, r) <= alpha:
    		break
    	else:
    		r = r_2
    	iter += 1
    return r


def save(t, r):
    # TODO
    f1 = open('1.txt', 'w')
    f2 = open('2.txt', 'w')
    for i in t:
    	for j in i:
    		f1.write(str(j))
    		f1.write(' ')
    	f1.write('\n')
    for i in r:
    	f2.write(str(i[0]))
    	f2.write('\n')

def dist(a, b):
    return np.sum(np.abs(a-b))

def main():
    graph = load(sys.argv[1]) # graph : dataframe
    transition_matrix = get_tran(graph)
    rank = cal_rank(transition_matrix)
    save(transition_matrix, rank)

if __name__ == '__main__':
    main()

