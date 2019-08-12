import genetic_methods
import net
import numpy as np


# --------------------------TESTING FEED FORWARD-------------------------------
print("--------------------------TESTING FEED FORWARD-------------------------------")
top = [65, 100, 4] #layer 0 (input) has 4 nodes, layers 1 (a hidden) has 3 nodes
network = net.NeuralNet(top)
network.randomizeWeights()

input = np.array(np.random.rand(1,65))
print(input)
input = input.transpose()
print(network.feedForward(input))
print("-----------------------------------------------------------------------------",end = "\n\n")
# -----------------------------------------------------------------------------


# --------------------------TESTING CROSSOVER-------------------------------
print("--------------------------TESTING CROSSOVER-------------------------------")

top = [4, 3, 2] #layer 0 (input) has 4 nodes, layers 1 (a hidden) has 3 nodes
network1 = net.NeuralNet(top)
network1.randomizeWeights()
network2 = net.NeuralNet(top)
network2.randomizeWeights()

crossed_works = genetic_methods.CrossOver(network1, network2)
print(len(crossed_works))
print(crossed_works)
print("-----------------------------------------------------------------------------",end = "\n\n")
# -----------------------------------------------------------------------------

# --------------------------TESTING FITNESS-------------------------------
print("--------------------------TESTING FITNESS-------------------------------")

test_scores = np.random.rand(4) * 100

print(test_scores)

print(genetic_methods.EvalFit(test_scores))
print("-----------------------------------------------------------------------------",end = "\n\n")
# -----------------------------------------------------------------------------

# --------------------------TESTING MUTATE-------------------------------
print("--------------------------TESTING MUTATE-------------------------------")

print("Pre mutate:")
print(network1.weights)

network1.mutate()

print("Post mutate:")
print(network1.weights)

print("-----------------------------------------------------------------------------",end = "\n\n")
# -----------------------------------------------------------------------------


# --------------------------TESTING UNFLATTEN-------------------------------
print("--------------------------TESTING UNFLATTEN-------------------------------")
print(network1.weights)
flattened1 = network1.flattenWeights()
network2.unflattenWeights(flattened1)
print(network2.weights)

if(len(network2.weights) != len(network1.weights)):
    print("\n\nFAILURE: unequal top level sizes") 
    exit(0)

for i in range(0,len(network1.weights)):
    if(len(network1.weights[i]) != len(network2.weights[i])):
        print("\n\nFAILURE: unequal inside sizes")
        exit(0)
    for j in range(0, len(network1.weights[i])):
        for k in range(0, network1.weights[i][j].size):
            if(network1.weights[i][j][k] != network2.weights[i][j][k]):
                print("\n\nFAILURE: Unequal values")
                exit(0)
print("Success")
print("-----------------------------------------------------------------------------")
