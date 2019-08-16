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
        self.mutationRate = .01

    def copy(self, copynet):
        # topology[i] is an integer corresponding to the number of nodes
        # in layer i of the network
        self.topology = copynet.topology
        self.numInputNodes = copynet.topology[0]
        self.numOutputNodes = copynet.topology[-1]
        self.numHiddenLayers = len(copynet.topology)-2
        self.totalLayers = copynet.len(topology)
        #each element is a matrix of weights
        self.weights = copynet.weights

    def randomizeWeights(self):
        # if there are n layers, there are n-1 sets of weights
        self.weights = []
        for i in range(0, self.totalLayers - 1):
            self.weights.append(np.random.rand(self.topology[i + 1], self.topology[i]) ) #rows in num of nodes in next layer, columns in num rows in previous4

    #does not implement bias atm. Param is column vector of input activations
    def feedForward(self, inputActivations):
        activations = list()
        activations.append( inputActivations )
        for i in range(1, self.totalLayers): #start at first hidden layer
            activations.append (sigmoid(np.dot(self.weights[i - 1], activations[i - 1])) )

        output = activations[-1]
        return output

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
        tempWeights = self.flattenWeights()

        #print(self.mutationRate)
        for i in range( len(tempWeights) ):
            tempRand = (np.random.randint(0,100))/100
            #print(tempRand)
            if(tempRand<self.mutationRate):
                #print(i)
                tempWeights[i] = (np.random.randint(0,100000000))/100000000
                #print(i)

        self.unflattenWeights(tempWeights)


    def unflattenWeights(self, flattenedWeights):
        self.weights = list()
        total_weights = 0
        weights_per_layer = []
        for i in range(1,len(self.topology)):
            total_weights += self.topology[i] * self.topology[i-1]
            weights_per_layer.append(self.topology[i] * self.topology[i-1])
        if(len(flattenedWeights) != total_weights):
            print("wrong dimensions in flattenedWeights, exitting")
            exit()

        flatten_index = 0
        for i in range(0,len(self.topology)-1):
            nodes = []

            weights_per_node = (int)(weights_per_layer[i]/self.topology[i+1])
            for j in range(0, self.topology[i+1]):
                weight_count = 0
                nodes.append(np.zeros(weights_per_node))
                while weight_count < weights_per_node:
                    nodes[j][weight_count] = flattenedWeights[flatten_index]
                    weight_count += 1
                    flatten_index += 1

            self.weights.append(np.array(nodes))
            # print(self.weights,end = "\n\n")

    def makeMove(self, input):
        output = feedForward(input)
        move = output[0]
        return move
                    
