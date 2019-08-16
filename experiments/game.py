import random
try:
  import curses
except Exception as e:
  print("Looks like you're not on linux. pip install windows-curses and try again")
  exit()

class GameState:
  # (0,0) is top left corner
  def __init__(self, width, height):
    random.seed(5)
    assert width > 0
    assert height > 0
    self.width = width
    self.height = height
    self.snake_list = [(0, 0)]
    self.head = (0, 0)
    self.direction = 'RIGHT'
    self.snake_bools = [[False for i in range(width)] for j in range(height)]
    self.food_bools = [[False for i in range(width)] for j in range(height)]
    self.snake_bools[0][0] = True
    self.food_bools[random.randint(0, self.height - 1)][random.randint(0, self.width - 1)] = True

  def __str__(self):
    return (f'score: {len(self.snake_list)}\n\n' +
      '\n'.join([''.join(
      ['oo' if self.head[0] == i and self.head[1] == j else
      '()' if self.snake_bools[i][j] else
      'xx' if self.food_bools[i][j] else '__'
      for j in range(self.width)])
      for i in range(self.height)])) + '\n\n'

class Game:
  def __init__(self, width, height):
    self.directions = {'RIGHT' : (0, 1),
                       'LEFT' : (0, -1),
                       'UP' : (-1, 0),
                       'DOWN' : (1, 0)}

    self.state = GameState(width, height)
    print('Game initialized')
    # print(self.state)

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
      # be careful because now m and n are out of bounds
      print('collided with wall!')
      return 1
    if state.food_bools[m][n]:
      # found food
      state.food_bools[m][n] = False
      more_food = True
    else:
      # didn't find food, end of tail disappears
      state.snake_bools[tail[0]][tail[1]] = False
      state.snake_list.pop()

    if state.snake_bools[m][n]:
      # collision with self
      print('collided with yourself!')
      return 1
    state.snake_list.insert(0, (m, n))
    state.snake_bools[m][n] = True
    state.head = (m, n)
    if more_food:
      ## fix this to just pick one of the empty spaces
      while state.snake_bools[m][n]:
        m = random.randint(0, state.height - 1)
        n = random.randint(0, state.width - 1)
      state.food_bools[m][n] = True

  def play(self, agent):
    # agent.stdscr.nodelay(1)
    while (True):
      # print(self.state)
      agent.stdscr.addstr(0, 0, str(self.state))
      agent.stdscr.addstr('q to quit')
      # curses.curs_set(0)
      agent.stdscr.refresh()
      # agent.stdscr.refresh()
      self.state.direction = agent.getNextMove(self.state)
      if self.state.direction == 'QUIT': return 1
      result = self.timestep()
      if result == -1: return -1
      if result == 1: return 1

    print(f'game over, you scored {len(self.state.snake_list)} points (length of snake)')

class Agent:
  # eventually there will be AI agents
  def getNextMove(self, state):
    pass

class KeyboardAgent(Agent):
  # that's you! arrow keys for movement, q to quit
  def __init__(self, stdscr):
    self.stdscr = stdscr

  def getNextMove(self, state):
    char = self.stdscr.getch()
    if char == 113: next_move = 'QUIT'
    elif char == 454 or char == curses.KEY_RIGHT: next_move = 'RIGHT'
    elif char == 452 or char == curses.KEY_LEFT:  next_move = 'LEFT'
    elif char == 450 or char == curses.KEY_UP:    next_move = 'UP'
    elif char == 456 or char == curses.KEY_DOWN:  next_move = 'DOWN'
    return next_move

def main(stdscr):
  # Clear screen
  stdscr.addstr(0, 0, 'use the arrow keys or WASD to move around.\npress any key to begin!')
  char = stdscr.getch()
  while (True):
    stdscr.clear()
    # curses.curs_set(0)
    agent = KeyboardAgent(stdscr)
    game = Game(10, 10)
    game.play(agent)
    stdscr.addstr(15, 0, 'game over, press any key to play again (q to quit)')
    char = stdscr.getch()
    if char == 113: return 0


if __name__ == '__main__':
  print('starting!')
  result = curses.wrapper(main)
  print(f'result: {result}')
  if result == -1:
    print('something went wrong')