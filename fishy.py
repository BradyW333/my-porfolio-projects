import random
import time
import os

fishy = {
  "tiger shark": 33333,
  "shark" : 500,
  "goldfish": 1,
  "lionfish": 30,
  "catfish": 15,
  "leopard whipray": 100,
  "sword": -20, 
  "salmon": 5
}

score = 0

while True:
  print("You have {} points".format(score))
  catch = random.choice(list(fishy))
  
  print("Press enter to start the game. Then Press enter to cast your line or the fish will swim away you will also only have two seconds.")
  input()

  time.sleep(random.randint(0,8))
  
  time_to_catch = 2
  startTime = time.time()
  
  print("You got a bite press enter to reel it in")
  input()

  endTime = time.time()
  reeTime = endTime - startTime
  print("Reeled in after {:.3f} seconds".format(reeTime))
  if reeTime < .08:
    print("CHEATER You")
    print("CHEATER reeled")
    print("CHEATER in")
    print("CHEATER too")
    print("CHEATER fast")
    
  elif reeTime <= time_to_catch:
    points = fishy[catch]
    score += points
    print("You caught a {}. It was worth {} points.".format(catch,points))

  else:
    print("Oh no it has seemed that the fish swam away")

  print()
  
    