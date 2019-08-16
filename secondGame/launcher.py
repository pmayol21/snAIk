import testsnake
import threading
import sys
sys.path.insert(1,"/mnt/c/Users/Mayolp/AIFACT/snAIk")
import net
import genetic_methods
import numpy as np

#tids = []
#for i in range(1,5):
#    tids.append(threading.Thread(target=testsnake.Run, args=()))
#    tids[i-1].start()

#for i in tids:
#    i.join()
best_score = 0
snakes = []
for i in range(1,5):
    network = net.NeuralNet([5,5,4])
    network.randomizeWeights()
    #print(network.weights)
    snakes.append(network)

while(best_score < 10):
    snake_counter = 0
    while(len(snakes) > 10):
        print("deleting snakes " + str(len(snakes)))
        if(np.random.random() > .50):
            snakes.pop(snake_counter)
            snake_counter -= 1
        snake_counter = (snake_counter + 1)%len(snakes)
    scores = []
    for i in range(0,len(snakes)):
        snake, score = testsnake.Run(snakes[i])

        scores.append(score)
        if(score > best_score):
            best_score = score
    
    genetic_methods.LiveorDie(snakes, scores)
    genetic_methods.SexySnake(snakes)
    print("Made new Snakes")