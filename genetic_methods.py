import net
import numpy as np

#add most of the genetic methods here


def CrossOver(parent1, parent2):
    flattenWeights1 = parent1.flattenWeights()
    flattenWeights2 = parent2.flattenWeights()

    split_index = np.random.randint(0,len(flattenWeights1))
    print(str(split_index) + "\n")

    return np.concatenate((flattenWeights1[0:split_index], flattenWeights2[split_index:len(flattenWeights2)]))



# top = [4, 3, 2] #layer 0 (input) has 4 nodes, layers 1 (a hidden) has 3 nodes
# network1 = net.NeuralNet(top)
# network1.randomizeWeights()
# network2 = net.NeuralNet(top)
# network2.randomizeWeights()

# crossed_works = CrossOver(network1, network2)
# print(len(crossed_works))
# print(crossed_works)