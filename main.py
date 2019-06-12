
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








class World:
  def __init__(self, xSize, ySize, foodPerDay):
    self.xSize = xSize
    self.ySize = ySize
    self.foodPerDay = foodPerDay
    self.grid = []
    self.time = 0
    self.foods = []
    self.createGrid()
  


  def placeFood(self):

    if(len(self.foods) < 1):
      for i in range (self.foodPerDay):
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
        if ((ranX) > self.xSize and ranX >= 0) and ((ranY) > self.ySize and ranY >= 0):
        
    
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
    self.printWorld()
    self.time += 1
    sleep(0.5)
    
    
wOrLd = World(10, 10, 2)
while(1):
  wOrLd.update()


  


