# snAIk

snAIk is a neuroevolution system designed to play Snake.

## Contributors:

Paul Mayol

Giovanni Morales

Josh Lebedinsky

Nathan Rausch

Richard Northrup

Will Zawilinski

[Our group presentation](https://docs.google.com/presentation/d/1xZgK9rnPcc02LQdOTg0_6cUooFeAgcZAJZcS8epcUdo/edit#slide=id.g35f391192_04)

## Instructions:

1. Download or clone this repo

2. If you are using Windows, install [windows-curses](https://pypi.org/project/windows-curses/):

```
pip install windows-curses
```

3. Run `sim.py` from the root folder `snAIk`:

```
python3 sim.py
```

## Neural Net
Neural net written from scratch using numerical computing functions in the package Numpy. The net is stored as a list of weight matrices. A function alows for matrix of input neuron activations to be passed in and fed forward, with a return matrix of a the 4 output activations, representing the networks choice to move the snake in 1 of 4 directions. Network can be created with any topology, allowing us to experiment.

## Genetic Algorithm
The length of each snake at the time of death determines how "fit" it was. The fittest snake in each generations gets to "breed" with the other snakes, meaning its neural net is combined 50/50 with another and slightly mutated randomly to produce a snake in the next generation.