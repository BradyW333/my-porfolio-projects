import random
import os
import time

def printBoard(board):
  os.system("clear")
  for guess,display in board:
      for i in range(5):
        if display[i] == "green":
          print(green_box.format(guess[i]),end = " ")
        if display[i] == "yellow":
          print(yellow_box.format(guess[i]),end = " ")
        if display[i] == "grey":
          print(grey_box.format(guess[i]),end = " ")
      print("\n")
  

board = []
for i in range(6):
  guess = "     "
  display = ["grey"]*5
  board.append((guess,display))
  
wordbank = []
secretwords = []

f = open("wordbank.txt", "r")
lines = f.readlines()
for line in lines:
  word = line.strip()
  wordbank.append(word)
f.close()

f = open("secretword.txt", "r") 
lines = f.readlines()
for line in lines:
  word = line.strip()
  secretwords.append(word)
f.close()

yellow_box = "\033[0;37;43m {} \033[0m"
green_box = "\033[0;37;42m {} \033[0m"
grey_box = "\033[0;37;40m {} \033[0m"

secretWord = random.choice(secretwords)

lives = 6
guess_number = 0

while guess_number < lives:
  printBoard(board)
  guess = input("Type a five letter word  ")
  if len(guess) != 5 or not guess.isalpha():
    print(" can you not read ")
    time.sleep(1)
    continue
  guess = guess.lower()
  
  if guess not in wordbank:
    print("Word not in word bank")
    time.sleep(1)
    continue
  

  display = ["grey", "grey", "grey", "grey", "grey" ]
  answer = secretWord
  for i in range(len(guess)):
    if guess[i] == answer[i]:
      display[i] = "green"
      answer = answer[:i] + " " + answer[i+1:]

  for i in range(len(guess)):
    if guess[i] in answer and display[i] != "green":
      display[i] = "yellow"
      answer = answer.replace(guess[i], " ", 1)

  board[guess_number] = (guess,display)
  guess_number += 1


  if guess == secretWord:
    print("You win")
    break
if guess != secretWord:
  print("The wordle was " + secretWord + ". You lose")
