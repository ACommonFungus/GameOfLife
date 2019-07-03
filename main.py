
#The Game Of Life


#Food copy and paste
#π
# Ω
WORLDXSIZE = 30
WORLDYSIZE = 30
foods = []

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
    self.eaten = 0
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
          #temp fix 
          break

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

    #here in the code we know where we're moving its stored in our self.x and self.y variables 
    #we can look in the world grid and see if the space we're about to move into contains a food
    #see if you can figure out how to pop the food off 
    #first thing, check if a food exists on the same tile as us 
    
    self.eat()
    
    wOrLd.grid[self.x][self.y].append(self)
      
  def eat(self):
    for i in range(0,len(wOrLd.grid[self.x][self.y])):
      if isinstance (wOrLd.grid[self.x][self.y][i], Food):
        wOrLd.grid[self.x][self.y].pop(i)
        self.eaten += 1
        #pop from the foods list as well 
        #we need to know which food to pop 
        #we're gonna do that based on an x y coordinate match 
        #loop through foods and find the food with our xy coordinate and pop it from the foods list
        for i in range(0, len(foods)):
          if foods[i].x == self.x and foods[i].y == self.y:
            foods.pop(i)
            break
        break

  def resetHunger(self):
    self.eaten = 0
        
        
    
  
  def update(self):
    self.move()


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
    foods = []
    self.animals = []
    self.createGrid()
    self.startingAnimals = startingAnimals
    self.placeAnimals()
    self.initializeFood()

  def placeAnimals(self):
    for i in range(0, self.startingAnimals):
      an = Animal(random.randint(0,self.xSize - 1), random.randint(0,self.ySize - 1),"δ",i)
      self.animals.append(an)
      self.grid[an.x][an.y].append(an)

  def initializeFood(self):
     for i in range (self.startingFood):
        food = Food(random.randint(0,self.xSize - 1), random.randint(0,self.ySize - 1))
        #push the food to the foods list 
        foods.append(food)
        #put the food in the grid 
        self.grid[food.x][food.y].append(food)

  def placeFood(self):
      #make food grow out from other food 
      for i in range(0, len(foods)):
        ranX = random.randint(-1, 1) + foods[i].x
        ranY = random.randint(-1, 1) + foods[i].y
        if (ranX < self.xSize and ranX >= 0) and (ranY < self.ySize and ranY >= 0):
    
    
            food = Food(ranX,ranY)
            #push the food to the foods list 
            foods.append(food)
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
 
      
  def checkAnimals(self):
    #go through the animals list and check if any animal has 0 eaten 
    #if it has 0 eaten, then pop the animal and create a food with a special character at its position 
    #if it has 1 or more just reset its eaten variabale 
    
    for i in range(0, len(self.animals)):
      if self.animals[i].eaten == 0:
       
        #we need to pop it from the world as well 
        for j in range(0,len(wOrLd.grid[self.animals[i].x][self.animals[i].y])):
          if isinstance(wOrLd.grid[self.animals[i].x][self.animals[i].y][j], Animal):
            if wOrLd.grid[self.animals[i].x][self.animals[i].y][j].iD == self.animals[i].iD:
              wOrLd.grid[self.animals[i].x][self.animals[i].y].pop(i)
              break 
      self.animals.pop(i)
      break
        #god help us i hope that works 

    
        
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
      self.checkAnimals()
    

   
    clear()

    #a for loop to update all animals 

    for animal in self.animals:
      animal.update()
    self.printWorld()
    self.time += 1
    sleep(0.5)
    
    
wOrLd = World(WORLDXSIZE, WORLDYSIZE, 25,15)
while(1):
  wOrLd.update()


  


