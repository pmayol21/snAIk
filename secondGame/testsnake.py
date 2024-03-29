from pygame.locals import *
from random import randint
import pygame
import time
import sys
sys.path.insert(1,"/mnt/c/Users/Mayolp/AIFACT/snAIk")
import net
import genetic_methods

class Apple:
    x = 0
    y = 0
    step = 44

    def __init__(self,x,y):
        self.x = x * self.step
        self.y = y * self.step

    def draw(self, surface, image):
        surface.blit(image,(self.x, self.y))


class Player:
    x = [0]
    y = [0]
    step = 44
    direction = 0
    length = 3

    updateCountMax = 2
    updateCount = 0


    def __init__(self, length, _network):
       self.length = length
       for i in range(0,2000):
           self.x.append(-100)
           self.y.append(-100)

       # initial positions, no collision.
       self.x[0] = 5 * 44
       self.x[1] = 4*44
       self.x[2] = 3*44
       self.y[0] = 5*44
       self.y[1] = 5*44
       self.y[2] = 5*44

       self.network = _network
       #print(self.network.weights)

    def update(self):

        self.updateCount = self.updateCount + 1
        if self.updateCount > self.updateCountMax:

            # update previous positions
            for i in range(self.length-1,0,-1):
                self.x[i] = self.x[i-1]
                self.y[i] = self.y[i-1]

            # update position of head of snake
            if self.direction == 0:
                self.x[0] = self.x[0] + self.step
            if self.direction == 1:
                self.x[0] = self.x[0] - self.step
            if self.direction == 2:
                self.y[0] = self.y[0] - self.step
            if self.direction == 3:
                self.y[0] = self.y[0] + self.step

            self.updateCount = 0


    def moveRight(self):
        self.direction = 0

    def moveLeft(self):
        self.direction = 1

    def moveUp(self):
        self.direction = 2

    def moveDown(self):
        self.direction = 3

    def draw(self, surface, image):
        for i in range(0,self.length):
            surface.blit(image,(self.x[i],self.y[i]))

class Game:
    def isCollision(self,x1,y1,x2,y2,bsize):
        if x1 >= x2 and x1 < x2 + bsize:
            if y1 >= y2 and y1 < y2 + bsize:
                return True
        #check for out of bounds
        if x1 > 800 or x1 < 0:
            return True
        if y1 > 600 or y1 < 0:
            return True
        return False

class App:

    windowWidth = 800
    windowHeight = 600
    player = 0
    apple = 0

    #first param is time in ms to pause the screen to slow the loop, 30 is a good number for humans
    #second param is 0 or 1 for show-graphics?
    def __init__(self, sleepTime, showGraphics, _net):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._apple_surf = None
        self.game = Game()
        self.player = Player(3, _net)
        self.apple = Apple(5,5)
        self.sleepTime = sleepTime
        self.showGraphics = showGraphics


    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)

        pygame.display.set_caption('Pygame pythonspot.com example')
        self._running = True
        self._image_surf = pygame.image.load("C:/Users/Mayolp/AIFACT/snAIk/secondGame/index2.png").convert()
        self._apple_surf = pygame.image.load("C:/Users/Mayolp/AIFACT/snAIk/secondGame/apple.png").convert()

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        self.player.update()

        # does snake eat apple?
        for i in range(0,self.player.length):
            if self.game.isCollision(self.apple.x,self.apple.y,self.player.x[i], self.player.y[i],44):
                self.apple.x = randint(2,9) * 44
                self.apple.y = randint(2,9) * 44
                self.player.length = self.player.length + 1


        # does snake collide with itself?
        for i in range(2,self.player.length):
            if self.game.isCollision(self.player.x[0],self.player.y[0],self.player.x[i], self.player.y[i],40):
                print("You lose! Collision: ")
                print("x[0] (" + str(self.player.x[0]) + "," + str(self.player.y[0]) + ")")
                print("x[" + str(i) + "] (" + str(self.player.x[i]) + "," + str(self.player.y[i]) + ")")
                return False

        return True

        pass

    def on_render(self):
        self._display_surf.fill((0,0,0))
        self.player.draw(self._display_surf, self._image_surf)
        self.apple.draw(self._display_surf, self._apple_surf)
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while( self._running ):
            time.sleep (self.sleepTime / 1000.0);

            pygame.event.pump()
            keys = pygame.key.get_pressed()
            
            poss_moves = self.player.network.feedForward([self.player.x[0] * 100.3, self.player.y[0]* 100.3,self.player.direction,self.apple.x* 100.3, self.apple.y* 100.3])
            #self.player.network.randomizeWeights()
            #print(poss_moves)
            max_value = 0
            max_index = 0
            for i in range(0, len(poss_moves)):
                if(poss_moves[i] > max_value):
                    max_value = poss_moves[i]
                    max_index = i

            #max_index += 1
            if (keys[K_RIGHT] or max_index == 0):
                self.player.moveRight()

            if (keys[K_LEFT] or max_index == 1):
                self.player.moveLeft()

            if (keys[K_UP] or max_index == 2):
                self.player.moveUp()

            if (keys[K_DOWN] or max_index == 3):
                self.player.moveDown()

            if (keys[K_ESCAPE]):
                self._running = False

            if(not self.on_loop()):
                self._running = False
            if (self.showGraphics == 1):
                self.on_render()

        self.on_cleanup()
        return False

    #BELOW IS A BUNCH OF FUNCTIONS TO PROVIDE INFO FOR THE NEURAL NET

    #returns array of snake peices, index 0 is the head
    def getPositionX(self):
        return self.x.copy()

    def getPositionY(self):
        return self.y.copy()

    def getScore(self):
        return self.player.length
    
    def getFoodPos(self):
        return self.apple.x, self.apple.y


if __name__ == "__main__" :
    theApp = App(30, 1)
    theApp.on_execute()

def Run(_net):
    theApp = App(0, 1, _net)
    theApp
    theApp.on_execute()
    return theApp.player.network, theApp.player.length
