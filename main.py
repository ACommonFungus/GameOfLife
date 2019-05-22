
#The Game Of Life


#Food copy and paste
#π


import random
from time import sleep
import os

clear = lambda: os.system('clear')


class Terrain:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.char = ","


class Animal:
  def __init__(self, hunger, age, x, y, char, iD):
    self.hunger = hunger
    self.age = age
    self.x = x
    self.y = y
    self.char = char
    self.iD = iD
    self.alive = True
    world[self.x][self.y].append(self)

  def move(self):

    for i in range (len(world[self.x][self.y])):
      if world[self.x][self.y][i] == self.iD:
        del world[self.x][self.y][i]

    moveBy = random.randint(0,4)
    if moveBy == 1:
      self.y += 1
    if moveBy == 2:
      self.x += 1
    if moveBy == 3:
      self.y -= 1
    if moveBy == 4:
      self.x -= 1

    world[self.x][self.y].append(self)
      
    
  def isAlive(self):
    if self.hunger <= 0:
      self.isAlive = False
      self.id = "x"
  
  def update(self):
    self.hunger -= 2
    self.isAlive()
    self.move()
    # self.checkForFood()

  def printAnimalStatus(self):
    print(self.hunger, " hunger")
  
  # def checkForFood(self):
  #   #if there is food in any of the tiles next to the animal it will eat it and get hunger back 
    
  #   for i in range(self.x - 1, self.x + 2):
  #     for j in range (self.y -1, self.y + 2):
  #       if(world[i][j] == "π"):
  #         self.hunger += 20
  #         world[i][j] = ","
      
  
      
  
class Food:
  def __init__(self, x, y,):
    self.nutrients = 10
    self.x = x
    self.y = y
    self.char = "π"
    world[self.x][self.y].append(self)









#grid creation
world = []
xSize = 10
ySize = 10
foodPerDay = 0
time = 0

def placeFood():
  for i in range (foodPerDay):
    food = Food(random.randint(0,xSize), random.randint(0,ySize))

def createGrid():
  for i in range (ySize):
    row = []
    for j in range(xSize):
      space = []
      ter = Terrain(i,j)
      space.append(ter)
      row.append(space)
    world.append(row)
    
def printWorld():
  print("")
  for i in range (xSize):
    for j in range(ySize):
      for k in range(len(world[i][j])):
        print(world[i][j][k].char,end = " ")
    print("")
  
  
  print("")
  print("Time : ", time)

  

    
createGrid()
printWorld()


#lets make an Animal
animal = Animal(100, 0, int(xSize/2), int(ySize/2), "Q", 1)

while(animal.isAlive):
  if(time == 0):
    placeFood()

  if(time == 24):
    time = 0
  animal.update()
  clear()
  printWorld()
  animal.printAnimalStatus()
  time += 1
  


