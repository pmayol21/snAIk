# snAIk
Training a neural net to play a classical snake game through neural evolution.

## Contributors

Paul Mayol

Giovanni Morales

Josh Lebedinsky

Nathan Rausch

Richard Northrup

Will Zawilinski

## Slideshow link

https://docs.google.com/presentation/d/1xZgK9rnPcc02LQdOTg0_6cUooFeAgcZAJZcS8epcUdo/edit#slide=id.g35f391192_04

## How to run  

1)In the folder testsnake.py, change the directory on line 6 to be your local path to /snAIk
2)Change line 129 in the same file to be the path to secondGame/index2.png , which is the snake body
3)Change line 130 in the same file to be the path to secondGame/apple.png, which is the apple
4)Have pygame and numpy installed for python3
4)In /secondGame, run the command in terminal "python3 launcher.py"

## Nueral Net

Nueral net written from scratch using numerical computing functions in the package Numpy. The net is stored as a list of weight matrices. A function alows for matrix of input nueron activations to be passed in and fed forward, with a return matrix of a the 4 output activations, representing the networks choice to move the snake in 1 of 4 directions. Network can be created with any topology, allowing us to experiment. 

## Genetic Algorithm

The length of each snake at the time of death determines how "fit" it was. The fittest snake in each generations gets to "breed" with the other snakes, meaning its nueral net is combined 50/50 with another and slightly mutated randomly to produce a snake in the next generation. 
