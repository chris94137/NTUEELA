import pandas as pd
import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt

attrs = ['AMB', 'CH4', 'CO', 'NMHC', 'NO', 'NO2',
        'NOx', 'O3', 'PM10', 'PM2.5', 'RAINFALL', 'RH',
        'SO2', 'THC', 'WD_HR', 'WIND_DIR', 'WIND_SPEED', 'WS_HR']
DAYS = np.array([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])

def read_TrainData(filename, N):
    #N: how many hours to be as inputs
    raw_data = pd.read_csv(filename).as_matrix()
    # 12 months, 20 days per month, 18 features per day. shape: (4320 , 24)
    data = raw_data[:, 3:] #first 3 columns are not data
    data = data.astype('float')
    X, Y = [], []
    for i in range(0, data.shape[0], 18*20):# shape[0] -> rows of the file
        # i: start of each month
        days = np.vsplit(data[i:i+18*20], 20) # shape: 20 * (18, 24) # split into 20 arrays (seperate by rows), (18, 24) = (features, data)
        concat = np.concatenate(days, axis=1) # shape: (18 feat, 480(day*hr))
        # take every N hours as x and N+1 hour as y
        for j in range(0, concat.shape[1]-N):
            features = concat[:, j:j+N].flatten() #the data of previous N hours
            features = np.append(features, [1]) # add w0
            X.append(features)
            Y.append([concat[9, j+N]]) #9th feature is PM2.5
    X = np.array(X) # previos N hours data
    Y = np.array(Y) # PM2.5
    return X, Y

#from 1/23 0am, 1am ..23pm... 2/23, 0am, .... ~ 12/31 23p.m, total 2424 hours
#will give you a matrix 2424 * (18*N features you need)
def read_TestData(filename, N):
	#only handle N <= 48(2 days)
    assert N <= 48
    raw_data = pd.read_csv(filename).as_matrix()
    data = raw_data[:, 3:]
    data = data.astype('float')
    surplus = DAYS - 20 #remaining days in each month after 20th
    test_X = []
    test_Y = [] #ground truth
    for i in range(12): # 12 month
        # i: start of each month
        start = sum(surplus[:i])*18
        end = sum(surplus[:i+1])*18
        days = np.vsplit(data[start:end], surplus[i])
        concat = np.concatenate(days, axis=1) # shape: (18 feat, (day*hr))
        for j in range(48, concat.shape[1]): #every month starts from 23th
            features = concat[:, j-N:j].flatten()
            features = np.append(features, [1]) # add w0
            test_X.append(features)
            test_Y.append([concat[9, j]])
    test_X = np.array(test_X)
    test_Y = np.array(test_Y)
    return test_X, test_Y


class Linear_Regression(object):
    def __init__(self):
        pass
    def train(self, train_X, train_Y):
        #TODO
        #W = ?
        W = np.dot(np.dot(inv(np.dot(train_X.transpose(), train_X)), train_X.transpose()), train_Y)
        min_set = []
        # for i in range(10):
        # 	# print(W)
        # 	min = 0
        # 	# print("W : \n", W)
        # 	for j in range(W.shape[0]):
        # 		if abs(W[j][0]) < abs(W[min][0]):
        # 			min = j
        # 	train_X = np.delete(train_X, min, axis = 1)
        # 	W = np.dot(np.dot(inv(np.dot(train_X.transpose(), train_X)), train_X.transpose()), train_Y)
        # 	min_set.append(min)
        # 	# print("min : ", min_set)
        self.W = W #save W for later prediction
        return min_set
    def predict(self, test_X, min_set):
        #TODO
        #predict_Y = ...?
        for i in min_set:
        	test_X = np.delete(test_X, i, axis = 1)
        predict_Y = np.dot(test_X, self.W)
        # print("W: ", self.W.shape)
        return predict_Y
def MSE(predict_Y, real_Y):
    #TODO :mean square error
    # loss = ?
    loss = np.power(real_Y - predict_Y, 2)
    sum = 0
    for i in loss:
    	sum += i
    loss = sum / real_Y.shape[0]
    return loss
def plotting(train_set_loss, test_set_loss, path = './loss.png'):
	assert len(train_set_loss) == len(test_set_loss)
	length = len(train_set_loss)
	plt.figure(figsize = (12, 8))
	plt.xticks(range(1, len(train_set_loss) + 1))
	plt.plot(range(1, length + 1), train_set_loss, 'b', label = 'train loss')
	plt.plot(range(1, length + 1), test_set_loss, 'r', label = 'test loss')
	plt.legend()
	plt.xlabel('N')
	plt.ylabel('MSE loss')
	plt.savefig(path)


if __name__ == '__main__' :
    N = 48
    train_X, train_Y = read_TrainData('train.csv', N=N)
    model = Linear_Regression()
    minset = model.train(train_X, train_Y)
    # print(train_X.shape)
    test_X, test_Y = read_TestData('test.csv', N=N)
    predict_Y = model.predict(test_X, minset)
    test_loss = MSE(predict_Y, test_Y)
    print(test_loss)
    train_set_loss = []
    test_set_loss = []
    for i in range(1, 49):
    	# print("n: ", i)
    	train_X, train_Y = read_TrainData('train.csv', N=i)
    	model = Linear_Regression()
    	minset = model.train(train_X, train_Y)
    	test_X, test_Y = read_TestData('test.csv', N=i)
    	predict_Y = model.predict(test_X, minset)
    	trained_Y = model.predict(train_X, minset)
    	train_loss = MSE(trained_Y, train_Y)
    	test_loss = MSE(predict_Y, test_Y)
    	train_set_loss.append(train_loss)
    	test_set_loss.append(test_loss)
    plotting(train_set_loss, test_set_loss)