import numpy as np

def sigmoid(x):
    return 1 / (1 + np.e ** -x)

class NueralNet:
    def __init__(self, topology):

        # topology[i] is an integer corresponding to the number of nodes
        # in layer i of the network
        self.topology = topology
        self.numInputNodes = topology[0]
        self.numOutputNodes = topology[-1]
        self.numHiddenLayers = len(topology)-2
        self.totalLayers = len(topology)
        #each element is a matrix of weights
        self.weights = []

    def randomizeWeights(self):
        # if there are n layers, there are n-1 sets of weights
        for i in range(0, self.totalLayers - 1):
            self.weights.append(np.random.rand(self.topology[i + 1], self.topology[i]) ) #rows in num of nodes in next layer, columns in num rows in previous4

        print("W0:", self.weights[0])

    #does not implement bias atm. Param is column vector of input activations
    def feedForward(self, inputActivations):
        activations = list()
        activations.append( inputActivations )
        for i in range(1, self.totalLayers): #start at first hidden layer
            activations.append (sigmoid(np.dot(self.weights[i - 1], activations[i - 1])) )

############# TESTING #########

top = [4, 3, 2] #layer 0 (input) has 4 nodes, layers 1 (a hidden) has 3 nodes
network = NueralNet(top)
network.randomizeWeights()

input = np.array([1, 0, 1, 1])
input = input.transpose()

network.feedForward(input)
