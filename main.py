
#The Game Of Life


#Food copy and paste
#π

WORLDXSIZE = 30
WORLDYSIZE = 30

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
  def __init__(self, x, y, char, iD):
    self.hunger = 100
    self.x = x
    self.y = y
    self.char = char
    self.iD = iD
    self.alive = True

  def move(self):

    #first step is take the list we're currently in and pop ourselves off it 
    #take our current position and for loop thru until you find the animal on the list with our ID 
    #the list we're on is just our x and y position on the grid 

    for i in range(0,len(wOrLd.grid[self.x][self.y])):
      if isinstance(wOrLd.grid[self.x][self.y][i], Animal):
        #just do a nested if 
        if wOrLd.grid[self.x][self.y][i].iD == self.iD:
          #now pop it out the list 
          wOrLd.grid[self.x][self.y].pop(i)
          #so now we dont exist in time or space

    moveBy = random.randint(0,3)
    if moveBy == 0:
      self.y += 1
    if moveBy == 1:
      self.x += 1
    if moveBy == 2:
      self.y -= 1
    if moveBy == 3:
      self.x -= 1

    #check if the y or x is bigger than or smaller than x size or y size of the world, if it is set the x or y to wrap
    
    if self.x > WORLDXSIZE - 1:
      self.x = 0
    if self.y > WORLDYSIZE - 1:
      self.y = 0
    if self.x < 0:
      self.x = WORLDXSIZE - 1
    if self.y < 0:
      self.y = WORLDYSIZE - 1
    
    wOrLd.grid[self.x][self.y].append(self)
      
    
  def isAlive(self):
    if self.hunger <= 0:
      self.isAlive = False
      self.id = "x"
  
  def update(self):
    #self.hunger -= 2
    #self.isAlive()
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








class World:
  def __init__(self, xSize, ySize, startingFood, startingAnimals):
    self.xSize = xSize
    self.ySize = ySize
    self.startingFood = startingFood
    self.grid = []
    self.time = 0
    self.foods = []
    self.animals = []
    self.createGrid()
    self.startingAnimals = startingAnimals
    self.placeAnimals()

  def placeAnimals(self):
    for i in range(0, self.startingAnimals):
      an = Animal(random.randint(0,self.xSize - 1), random.randint(0,self.ySize - 1),"δ",i)
      self.animals.append(an)
      self.grid[an.x][an.y].append(an)

  def placeFood(self):
    if(len(self.foods) < 1):
      for i in range (self.startingFood):
        food = Food(random.randint(0,self.xSize - 1), random.randint(0,self.ySize - 1))
        #push the food to the foods list 
        self.foods.append(food)
        #put the food in the grid 
        self.grid[food.x][food.y].append(food)
    else:
      #make food grow out from other food 
      for i in range(0, len(self.foods)):
        ranX = random.randint(-1, 1) + self.foods[i].x
        ranY = random.randint(-1, 1) + self.foods[i].y
        if (ranX < self.xSize and ranX >= 0) and (ranY < self.ySize and ranY >= 0):
    
    
            food = Food(ranX,ranY)
            #push the food to the foods list 
            self.foods.append(food)
            #put the food in the grid 
            self.grid[food.x][food.y].append(food)



  def createGrid(self):
    for i in range (self.ySize):
      row = []
      for j in range(self.xSize):
        space = []
        ter = Terrain(i,j)
        space.append(ter)
        row.append(space)
      self.grid.append(row)
    
  def printWorld(self):
    print("")
    for i in range (self.xSize):
      for j in range(self.ySize):
        if(len(self.grid[i][j]) > 1):
          #only print the char that isnt a Terrain
          print(self.grid[i][j][1].char,end = " ")     
        else: 
          print(self.grid[i][j][0].char,end = " ")
      print("")
    print("")
    print("Time : ", self.time)

  def update(self):
    if(self.time == 24):
      self.time = 0
    if(self.time == 0):
      self.placeFood()
   
    clear()

    #a for loop to update all animals 

    for animal in self.animals:
      animal.update()
    self.printWorld()
    self.time += 1
    sleep(0.5)
    
    
wOrLd = World(WORLDXSIZE, WORLDYSIZE, 10,15)
while(1):
  wOrLd.update()


  


