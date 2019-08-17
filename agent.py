import net
import time
import numpy as np

try:
  import curses

except Exception as e:
  print("Looks like you're not on linux. pip install windows-curses and try again")
  exit()


class Agent:
  # eventually there will be AI agents
  def getNextMove(self, state):
    pass

class KeyboardAgent(Agent):
  # that's you! arrow keys for movement, q to quit
  def __init__(self, stdscr, outfile = None, debugfile = None):
    self.stdscr = stdscr
    self.outfile = outfile
    self.debugfile = debugfile

  def getNextMove(self, state):
    char = self.stdscr.getch()
    next_move = state.direction
    if char == 113: next_move = 'QUIT'
    elif char == 454 or char == curses.KEY_RIGHT: next_move = 'RIGHT'
    elif char == 452 or char == curses.KEY_LEFT:  next_move = 'LEFT'
    elif char == 450 or char == curses.KEY_UP:    next_move = 'UP'
    elif char == 456 or char == curses.KEY_DOWN:  next_move = 'DOWN'
    return next_move

class NEAgent(Agent):
  # neuroevolution agent - has a NeuralNet to make decisions from
  def __init__(self, network, stdscr = None, outfile = None, debugfile = None):
    self.stdscr = stdscr
    self.outfile = outfile
    self.debugfile = debugfile
    self.network = network
    self.directions = ['RIGHT', 'LEFT', 'UP', 'DOWN']

  def getNextMove(self, state):
    inputs = np.array([state.snake_bools, state.food_bools]).flatten()
    outputs = self.network.feedForward(inputs)
    index = outputs.argmax()
    next_move = self.directions[index]
    if self.stdscr:
      curses.napms(50)
      self.stdscr.refresh()

    return next_move


