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

def LiveorDie(snakes, scores):
    chances = EvalFit(scores)
    snake_counter = 0
    print(chances)
    for i in range(0,len(chances)):
        chance = np.random.random()
        if(chance > chances[i]):
            print("Killed snake " + str(snakes[snake_counter]) + " with chance: " + str(chance) + " vs chance of survival: " + str(chances[i]))
            snakes.pop(snake_counter)
        else:
            snake_counter += 1

# implemented breeding by the best snake getting to do the doo with all other snakes and those will be the children
# added to the population
def SexySnake(snakes):
    if(len(snakes) == 1):
        child = net.NeuralNet(snakes[0].topology)
        child.copy(snakes[0])

        child.mutate()
        snakes.append(child)
        return
    

    for i in range(1, len(snakes)):
        child = net.NeuralNet(snakes[0].topology)
        child.unflattenWeights(CrossOver(snakes[0], snakes[i]))
        child.mutate()
        snakes.append(child)
    return