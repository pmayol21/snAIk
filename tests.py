import genetic_methods
import net
import numpy as np
import sys
sys.path.insert(1,"/mnt/c/Users/Mayolp/AIFACT/snAIk/secondGame")
import testsnake


# def printWeights(weights):
#     layer_counter = 1
#     for i in range(0, len(weights)):
#         print("Layer " + str(layer_counter) + ":")
#         node_counter = 1
#         for j in range(0, len(weights[i])):
#             print("\tNode " + str(node_counter) + ": ", end = "")
#             for k in range(0, len(weights[i][j])):
#                 print(weights[i][j][k], end = " ")
#             node_counter += 1
#             print()
#         layer_counter += 1
# --------------------------TESTING FEED FORWARD-------------------------------
print("--------------------------TESTING FEED FORWARD-------------------------------")
top = [4,3, 4] #layer 0 (input) has 4 nodes, layers 1 (a hidden) has 3 nodes
network = net.NeuralNet(top)
network.randomizeWeights()
# print(network.weights)


input = np.array(np.random.rand(1,4))
# input = [1,1 ,1]
# print(input)
input = input.transpose()
print(network.feedForward(input))
# print(network.weights)
network.randomizeWeights()
# print(network.weights)
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
print("-----------------------------------------------------------------------------",end = "\n\n")

# --------------------------TESTING SNAKE SELECTION-------------------------------
print("--------------------------TESTING KILLING-------------------------------")

snakes = []
scores = []
for i in range(0,10):
    scores.append(np.random.randint(0,100))
    snakes.append(i)

genetic_methods.LiveorDie(snakes, scores)
print(snakes)

print("-----------------------------------------------------------------------------",end = "\n\n")


# --------------------------TESTING SNAKE BREEDING-------------------------------
print("--------------------------TESTING MAKE BABIES-------------------------------")

breed_top = [65, 2, 8]
snakes = []
scores = []
for i in range(0, 10):
    scores.append(np.random.randint(0,100))
    snake = net.NeuralNet(breed_top)
    snake.randomizeWeights()
    snakes.append(snake)

genetic_methods.LiveorDie(snakes, scores)

print(len(snakes))
genetic_methods.SexySnake(snakes)
print(len(snakes))
print("-----------------------------------------------------------------------------",end = "\n\n")

# --------------------------TESTING GAME-------------------------------
print("--------------------------TESTING GAME CALL-------------------------------")
testsnake.Run()
print("-----------------------------------------------------------------------------",end = "\n\n")