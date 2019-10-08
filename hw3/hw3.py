import sys
import numpy as np

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import math

def plot_wave(x, path = './wave.png'):
    plt.gcf().clear()
    plt.plot(x)
    plt.xlabel('n')
    plt.ylabel('xn')
    plt.savefig(path)

def plot_ak(a, path = './freq.png'):
    plt.gcf().clear()

    # Only plot the mag of a
    a = np.abs(a)
    plt.plot(a)
    plt.xlabel('k')
    plt.ylabel('ak')
    plt.savefig(path)

def CosineTrans(x, B):
    # TODO
    # implement cosine transform
    invB = np.linalg.inv(B)
    return np.dot(invB, x)

def InvCosineTrans(a, B):
    # TODO
    # implement inverse cosine transform
    return np.dot(B, a)

def gen_basis(N):
    # TODO
    basis = np.zeros([N, N])
    for k in range(N):
    	for n in range(N):
    		if k == 0:
    			basis[n, k] = 1 / math.sqrt(N)
    		else:
    			basis[n, k] = math.sqrt(2 / N) * math.cos((n + 0.5) * k * math.pi / N)
    return basis

if __name__ == '__main__':

    signal_path = sys.argv[1]
    signal = np.genfromtxt(signal_path, delimiter = '\n')
    plot_wave(signal)
    basis = gen_basis(len(signal))
    a = CosineTrans(signal, basis)
    plot_ak(a, './b06901063_freq.png')
    mask = a < 12
    mx = np.ma.array(a, mask = mask, fill_value = 0)
    for element in range(len(mask)):
    	if mask[element]:
    		a[element] = 0;
    plot_ak(a, './freq.png')
    count = 0
    a_for_1 = np.copy(a)
    a_for_3 = np.copy(a)
    for element in range(len(a)):
    	if a[element] != 0:
    		count += 1
    		if not (count == 1):
    			a_for_1[element] = 0
    		if not (count == 3):
    			a_for_3[element] = 0
    plot_ak(a_for_1, './a1.png')
    plot_ak(a_for_3, './a3.png')
    ans_for_1 = InvCosineTrans(a_for_1, basis)
    ans_for_3 = InvCosineTrans(a_for_3, basis)
    plot_wave(ans_for_1, './f1.png')
    plot_wave(ans_for_3, './f3.png')
    np.savetxt('./b06901063_f1.txt', ans_for_1)
    np.savetxt('./b06901063_f3.txt', ans_for_3)



