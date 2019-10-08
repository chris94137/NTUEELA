import sys
import numpy as np
from graph_gen import *

def has_cycle(sets):
	# TODO
	# return True if the graph has cycle; return False if not
	while(len(sets) != 0):
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
			sets.append(newRow)
		sets.pop(0)

	return False

def main():
	p1_list = list()
	if len(sys.argv) <= 1:
		p1_list = get_p1('r07')
	else:
		p1_list = get_p1(sys.argv[1])
		
	for sets in p1_list:
		#print(sets)
		'''
		for i in range(len(sets)):
			for j in range(len(sets[i])):
				print("{:3s}".format("".join(str(sets[i][j]))), end = '')
			print('')
		'''
		'''
		  HINT: You can `print(sets)` to show what the matrix looks like
			If we have a directed graph with 2->3 4->1 3->5 5->2 0->1
				   0  1  2  3  4  5
				0  0  0 -1  1  0  0
				1  0  1  0  0 -1  0
				2  0  0  0 -1  0  1
				3  0  0  1  0  0 -1
				4 -1  1  0  0  0  0
			The size of the matrix is (5,6)
		'''
		if has_cycle(sets):
			print('Yes')
		else:
			print('No')

if __name__ == '__main__':
	main()

