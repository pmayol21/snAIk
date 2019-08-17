from agent import Agent, NEAgent
from terminal_snake import Game, GameState
import genetic_methods
import datetime
import net
import terminal_snake
import numpy as np
import random

try:
  import curses

except Exception as e:
  print("Looks like you're not on linux. pip install windows-curses and try again")
  exit()

width = 8
height = 8
max_moves = 20
input_layer_size = width * height * 2
population = 200
seed_size = int(population * 0.9)
generations = 500
topology = [input_layer_size, 10, 4]

def nextGeneration(seeds):
  gen = []
  for i in range(population):
    seed = seeds[random.randint(0, len(seeds) - 1)]
    new_snake = net.NeuralNet(topology)
    new_snake.copy(seed)
    new_snake.mutate()
    gen.append(new_snake)

  return gen

def findWinners(snakes, scores):
  return [x for x, _ in sorted(zip(snakes, scores), key = lambda pair: pair[1])[-20:]]

def run(stdscr = None):
  game = Game()
    
  outfile = open('log.txt', 'w')
  debugfile = open('debug.txt', 'w')
  outfile.write(f'-------------------new log: {str(datetime.datetime.now())}\n\n')
  debugfile.write(f'-------------------new debug: {str(datetime.datetime.now())}\n\n')

  snakes = []
  for i in range(population):
    snake = net.NeuralNet(topology)
    snake.randomizeWeights()
    snakes.append(snake)

  for i in range(generations):
    scores = []
    outfile.write(f'start generation {i}')
    for snake in snakes:
      game.reset(8, 8)
      stdscr.clear()
      stdscr.addstr(0, 2 * width + 1, f'generation {i}')
      # stdscr.getch()
      agent = NEAgent(snake, stdscr, outfile, debugfile)
      # agent = NEAgent(snake, None, outfile, None)
      score, fullrun = game.play(agent, max_moves)
      scores.append(score)
      # print(f'{i}: {score}; ')
      if score > 2:
        # print(score)
        outfile.write(f'scored {score}! in gen {i}\n')
        outfile.write(fullrun)

    seeds = findWinners(snakes, scores)
    snakes = nextGeneration(seeds)
    # genetic_methods.LiveorDie(snakes, scores)
    # genetic_methods.SexySnake(snakes)


  outfile.close()
  debugfile.close()




# run()
curses.wrapper(run)
