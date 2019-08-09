import numpy as np

def sigmoid(x):
    return 1 / (1 + np.e ** -x)

class NeuralNet:
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
        self.mutationRate = 1

    def copy(self, copynet):
        # topology[i] is an integer corresponding to the number of nodes
        # in layer i of the network
        self.topology = copynet.topology
        self.numInputNodes = copynet.topology[0]
        self.numOutputNodes = copynet.topology[-1]
        self.numHiddenLayers = copynet.len(topology)-2
        self.totalLayers = copynet.len(topology)
        #each element is a matrix of weights
        self.weights = []

    def randomizeWeights(self):
        # if there are n layers, there are n-1 sets of weights
        for i in range(0, self.totalLayers - 1):
            self.weights.append(np.random.rand(self.topology[i + 1], self.topology[i]) ) #rows in num of nodes in next layer, columns in num rows in previous4

        # print("W0:", self.weights[0])

    #does not implement bias atm. Param is column vector of input activations
    def feedForward(self, inputActivations):
        activations = list()
        activations.append( inputActivations )
        for i in range(1, self.totalLayers): #start at first hidden layer
            activations.append (sigmoid(np.dot(self.weights[i - 1], activations[i - 1])) )

    #put all weights into a single array ([layer1 layer2 layer3])
    def flattenWeights(self):
        flattenWeights = []
        for i in self.weights:
            for j in i:
                if np.array_equal(np.array(flattenWeights), np.array([])):
                    flattenWeights = np.ravel(j)
                else:
                    flattenWeights = np.concatenate((flattenWeights,np.ravel(j)))
        return flattenWeights

    def mutate(self):
        tempWeights = flattenWeights(self)

        for i in tempWeights:
            tempRand = np.random.random(0,1)
            if(tempRand<mutationRate):

        
    def unflattenWeights(self, flattenedWeights):
        total_weights = 1
        for i in topology:
            total_weights *= i
        if(len(flattenedWeights) != total_weights):
            print("wrong dimensions in flattenedWeights, exitting")
            exit()