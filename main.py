from ai import *

lewis = Lewis()

isPlaying = True
def playJotto():
  soliciateUserGuess()

def computerSelectWord():
  return lewis.AIMakeGuess()

def soliciateUserGuess():
  userGuess = ""
  while len(userGuess) != 5:
    userGuess = input("Please guess a 5 letter word with no repeating letters\n")
  checkUserGuess(userGuess)

def checkUserGuess(userGuess):
  global isPlaying
  letters = []
  count = 0
  for letter in userGuess:
   #print(ord(letter))
  
   if ord(letter) in letters:
      print("Invalid word!")
      break
   else:
      letters.append(ord(letter))
  for i in computerSelectWord():
      if ord(i) in letters:
          count += 1
  if count == 5:
    print("Victory! The word was", userGuess)
    isPlaying = False
  else: 
    print(userGuess, count)

while isPlaying:
  playJotto()