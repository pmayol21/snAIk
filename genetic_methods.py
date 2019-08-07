import net
import numpy as np

#add most of the genetic methods here

# takes a certain number of the weights of network 1 and concats them with weights in network 2
def CrossOver(parent1, parent2):

    # get all of the weights in the first network and second network in 1D numpy arrays
    flattenWeights1 = parent1.flattenWeights()
    flattenWeights2 = parent2.flattenWeights()

    # get the index to split on
    split_index = np.random.randint(0,len(flattenWeights1))
    print(str(split_index) + "\n")

    # return the concatenation of the first 0-split index of the first netowrk with 
    # the split index - rest of weights in second network
    return np.concatenate((flattenWeights1[0:split_index], flattenWeights2[split_index:len(flattenWeights2)]))