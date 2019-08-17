import random
import numpy as np
from agent import Agent, KeyboardAgent

try:
  import curses

except Exception as e:
  print("Looks like you're not on linux. pip install windows-curses and try again")
  exit()


class GameState:
  # (0,0) is top left corner
  def __init__(self, width, height):
    # random.seed(5)
    assert width > 0
    assert height > 0
    self.width = width
    self.height = height
    self.head = (height//2, width//2)
    self.food = (random.randint(0, self.height - 1), random.randint(0, self.width - 1))
    self.snake_list = [self.head]
    self.direction = 'RIGHT'
    self.snake_bools = np.array([[0 for i in range(width)] for j in range(height)])
    self.food_bools = np.array([[0 for i in range(width)] for j in range(height)])
    self.snake_bools[self.head[0]][self.head[1]] = True
    self.food_bools[self.food[0]][self.food[1]] = 1

  def __str__(self):
    return (f'score: {len(self.snake_list)}\n\n' +
      '\n'.join([''.join(
      ['oo' if self.head[0] == i and self.head[1] == j else
      '()' if self.snake_bools[i][j] else
      '::' if self.food_bools[i][j] else '__'
      for j in range(self.width)])
      for i in range(self.height)])) + '\n\n'

  def rep(self):
    return [''.join(
      ['oo' if self.head[0] == i and self.head[1] == j else
      '()' if self.snake_bools[i][j] else
      '::' if self.food_bools[i][j] else '__'
      for j in range(self.width)])
      for i in range(self.height)] + [f'score: {len(self.snake_list)}', '']

class Game:
  def __init__(self):
    self.state = None
    self.directions = {'RIGHT' : (0, 1),
                       'LEFT' : (0, -1),
                       'UP' : (-1, 0),
                       'DOWN' : (1, 0)}

  def reset(self, width, height):
    self.state = GameState(width, height)

  # return 0 for normal timestep, 1 if gameover, -1 for any error
  def timestep(self):
    state = self.state
    last_position = state.snake_list[0]
    delta_position = self.directions[state.direction]
    # not using x and y because of how the board is oriented,
    # that would confuse me too much
    m = last_position[0] + delta_position[0]
    n = last_position[1] + delta_position[1]
    next_position = (m, n)
    more_food = False
    tail = (state.snake_list[-1])
    if m < 0 or m >= state.height or n < 0 or n >= state.width:
      # collision with wall
      return 1

    if state.food_bools[m][n]:
      # found food
      state.food_bools[m][n] = 0
      more_food = True

    else:
      # didn't find food, end of tail disappears
      state.snake_bools[tail[0]][tail[1]] = 0
      state.snake_list.pop()

    if state.snake_bools[m][n]:
      # collision with self
      return 1

    state.snake_list.insert(0, (m, n))
    state.snake_bools[m][n] = 1
    state.head = (m, n)
    if more_food:
      # TODO: fix this to just pick one of the empty spaces
      while state.snake_bools[m][n]:
        m = random.randint(0, state.height - 1)
        n = random.randint(0, state.width - 1)

      state.food_bools[m][n] = 1
      state.food = (m, n)

  def play(self, agent, max_moves):

    fullrun = ""

    # agent.stdscr.addstr(25, 15, f'hmmmmmmmm')
    # agent.stdscr.getch()

    for move in range(max_moves):
      if (agent.stdscr):
        # agent.stdscr.getch()
        # agent.stdscr.addstr(0, 0, str(self.state))
        for i, line in enumerate(self.state.rep()):
          agent.stdscr.addstr(i, 0, line)
        agent.stdscr.addstr('q to quit\n')
        agent.stdscr.refresh()
        # agent.stdscr.getch()

      if (agent.debugfile):
        agent.debugfile.write(str(self.state))

      fullrun += str(self.state)

      self.state.direction = agent.getNextMove(self.state)
      if self.state.direction == 'QUIT': break
      result = self.timestep()
      if result == -1: return -1
      if result == 1: break

    if (agent.stdscr):
      agent.stdscr.addstr(f'game over, you scored {len(self.state.snake_list)} points!')

    if (agent.debugfile):
      agent.debugfile.write(f'game over, you scored {len(self.state.snake_list)} points!')

    return (len(self.state.snake_list), fullrun)

def main(stdscr):
  curses.curs_set(False)
  stdscr.clear()
  stdscr.addstr(0, 0, 'use the arrow keys or WASD to move around.\npress any key to begin!')
  char = stdscr.getch()
  while (True):
    stdscr.clear()
    agent = KeyboardAgent(stdscr, None)
    game = Game()
    game.reset(10, 10)
    game.play(agent, 999)
    stdscr.addstr(15, 0, '\npress any key to play again (q to quit)\n')
    char = stdscr.getch()
    if char == 113: return 0


if __name__ == '__main__':
  print('starting!')
  result = curses.wrapper(main)
  print(f'result: {result}')
  if result == -1:
    print('something went wrong')