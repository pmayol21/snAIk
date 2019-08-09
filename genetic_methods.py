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

    # return the concatenation of the first 0-split index of the first netowrk with 
    # the split index - rest of weights in second network
    return np.concatenate((flattenWeights1[0:split_index], flattenWeights2[split_index:len(flattenWeights2)]))


# takes in a numpy array of the final scores of all of the snake games that were played
# returns probability array  of how likely each snake was to survive 

# max probability to survive will be .90 (the highest scoring snake will have a 90% chance to pass on its genes)
def EvalFit(score_array):
    probability_arr = []

    max_prob = .98 #can change this value to make the probability of best scoring snake surviving higher
    max_score = 0

    for i in score_array:
        if(i > max_score):
             max_score = i
    
    for i in score_array:
        probability_arr.append((i - (1 - max_prob) * i)/max_score)

    return np.array(probability_arr)
