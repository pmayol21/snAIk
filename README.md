# snAIk

snAIk is a neuroevolution system designed to play Snake.

## Contributors

Paul Mayol

Giovanni Morales

Josh Lebedinsky

Nathan Rausch

Richard Northrup

Will Zawilinski

[Our group presentation](https://docs.google.com/presentation/d/1xZgK9rnPcc02LQdOTg0_6cUooFeAgcZAJZcS8epcUdo/edit#slide=id.g35f391192_04)

## Instructions:

### Terminal-based game

1. Download or clone this repo (https://github.com/pmayol21/snAIk)

2. If you are using Windows, install [windows-curses](https://pypi.org/project/windows-curses/):

```
pip install windows-curses
```

4. Run `terminal_snake.py` from the root folder `snAIk`:

```
python3 sim.py
```

Here you can test the visuals. Keep in mind this version of snake is not timed.

3. Run `sim.py` from the root folder `snAIk`:

```
python3 sim.py
```

Here you can see the simulation - it takes many generations to learn the game.

### GUI-based game

1. In the folder testsnake.py, change the directory on line 6 to be your local path to /snAIk
2. Change line 129 in the same file to be the path to secondGame/index2.png , which is the snake body
3. Change line 130 in the same file to be the path to secondGame/apple.png, which is the apple
4. Have pygame and numpy installed for python3
4. In /secondGame, run the command in terminal "python3 launcher.py"


## Neural Net
Neural net written from scratch using numerical computing functions in the package Numpy. The net is stored as a list of weight matrices. A function alows for matrix of input neuron activations to be passed in and fed forward, with a return matrix of a the 4 output activations, representing the networks choice to move the snake in 1 of 4 directions. Network can be created with any topology, allowing us to experiment.

## Genetic Algorithm
The length of each snake at the time of death determines how "fit" it was. The fittest snake in each generations gets to "breed" with the other snakes, meaning its neural net is combined 50/50 with another and slightly mutated randomly to produce a snake in the next generation.


## Our process/struggles
We initially attempted to create out own game from scratch. After this failed, we then found a python game online which we modified to suit our needs (found at https://pythonspot.com/snake-with-pygame/). However, after our discusion during and after the demo on Friday, rewrote an entire snake game again, in order to get different inputs with the hope of allowing our neural network to have access to more inputs. This provided better results, however our results are still not ideal.
We also experimented with the size of the neural network. We found that with a small network (1 internal layer with 4 nodes), the network was significantly limited in it's ability to learn. However, we also found that when we created significantly large networks, the outputs aproached 1, which is an undesireable result.
