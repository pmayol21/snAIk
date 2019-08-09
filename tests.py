import genetic_methods
import net
import numpy as np


# --------------------------TESTING FEED FORWARD-------------------------------
print("TESTING FEED FORWARD")
top = [4, 3, 2] #layer 0 (input) has 4 nodes, layers 1 (a hidden) has 3 nodes
network = net.NeuralNet(top)
network.randomizeWeights()

input = np.array([1, 0, 1, 1])
input = input.transpose()
print(network.feedForward(input), end = "\n\n")
# -----------------------------------------------------------------------------


# --------------------------TESTING CROSSOVER-------------------------------
print("TESTING CROSSOVER")

top = [4, 3, 2] #layer 0 (input) has 4 nodes, layers 1 (a hidden) has 3 nodes
network1 = net.NeuralNet(top)
network1.randomizeWeights()
network2 = net.NeuralNet(top)
network2.randomizeWeights()

crossed_works = genetic_methods.CrossOver(network1, network2)
print(len(crossed_works))
print(crossed_works, end = "\n\n")
# -----------------------------------------------------------------------------

# --------------------------TESTING CROSSOVER-------------------------------
print("TESTING FITNESS FUNCTION")

test_scores = np.random.rand(4) * 100

print(test_scores)

print(genetic_methods.EvalFit(test_scores))