import random
import os
import time

def rollDie(sides):
  roll = random.randint(1,sides)
  print("The die rolled a {}".format(roll))
  return roll
  
diceType = 6
tokens = 10

instructions = "\t\t\tWelcome to dicey dice\n  The first die will roll. Than you have to guess if it will be higher, lower or the same. If you guess correctly you will recive your money times 2 unless if you guess the same and than you will recieve 5 times the amount you bet .  If you ever want to quit just type quit. I dont know why you would want to quit but you can\n Current die {}\n".format(diceType)

print(instructions)

while tokens > 0:
  print("You have " + str(tokens) + " tokens")
  bet = input("How many tokens do you wish to bet? ")

  if bet == "quit":
    print("Your quitting! See you next time")
    break

  if not bet.isnumeric():
    print("Pick a whole number please")
    continue
    
  bet = int(bet)
    
  if bet > tokens:
    print("Not enough tokens")
    continue
 

  tokens = tokens - bet 

  die1 = rollDie(diceType)

  

  guess = ""

  while guess != "higher" and guess != "lower" and guess != "same number":
    guess = input("Do you think the next roll will be higher, lower or the same number?\nChoose carfully! ")
  
  die2 = rollDie(diceType)

  correct = False
  multiplier = 2
  
  if die2 > die1:
    print("THE SECOND roll IS HIGHER")
    if guess == "higher":
      correct = True

  if die2 < die1:
    print("THE SECOND roll IS LOWER")
    if guess == "lower":
      correct = True

  if die2 == die1:
    print("THE SECOND roll IS THE SAME AS roll ONE")
    if guess == "same number":
      correct = True
      multiplier = 6

  if correct: 
    print("You were correct!")
    print("You won {} tokens".format(bet))
    tokens += bet*multiplier
  else:
    print("You lost, you can always make your money back you know")

  time.sleep(2)
  os.system("clear")
  print(instructions)
  


if tokens == 0:
  print("You ran out of tokens")
  

  
  