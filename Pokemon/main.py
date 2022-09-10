import random
import turtle
#
#ProfOak = input("Hi welcome to the world of pokemon, Pick a starter pokemon of your choice from this list: Solgaleo, MewTwo, Meowth ")
# print function for our 2d list
def banana(field):
  for row in field:
    w = " ".join(row)
    print(w)
# place encouter
def placeEncouter():
  if length == 1:
    return
  xpoke = random.randint(0, length-1)
  ypoke = random.randint(0, length-1)
  
  while field[ypoke][xpoke] == "p":
    xpoke = random.randint(0, length-1)
    ypoke = random.randint(0, length-1)
  field[ypoke][xpoke] = "*"
  
def runEncouter():
  print("battlE")
  randompokemon = random.choice(pokemon)
  t.shape(randompokemon)
  
pokemon = ["shinx.png", "litten.png", "bb.jpeg", "incineroarpokedexthing.png", "Meowth.png, Solgaleo.png", "mewtwo.png", "litleo.png", "Luxio.png", "Luxray.png", "lycanroc.jpg", "Persian.png", "Torracat.png"]
t = turtle.Turtle() 
t.left(90) 
screen = turtle.Screen()

for image in pokemon:
  screen.addshape(image)
  
  
#create a 2d list
field = []
length = 5

# DO NOT SET THIS TO ONE OR ZERO OR AND DEDCIMAl

for i in range(length):
  row = ["_"]*length
  field.append(row)


#putting the player in the middle
x = length//2
y = length//2

field[y][x] = "p"
placeEncouter()

banana(field)

while True:
  move = input("Which way do u want to move? WASD?\n")
  field[y][x] = "_"
  if move == "w":
    y = y-1 
    if y < 0:
      y = length-1
  elif move == "s":
    y= y+1
    if y > length-1:
      y = 0
  elif move == "a":
    x = x-1
    if x < 0:
      x = length-1
  elif move == "d":
    x= x+1
    if x > length-1:
      x = 0
  else:
    print("press WASD")
    field[y][x] = "p"
    continue
  if field[y][x] == "*":
    field[y][x] = "p"
    placeEncouter()
    runEncouter()
  else:  
    field[y][x] = "p"
  banana(field)
  