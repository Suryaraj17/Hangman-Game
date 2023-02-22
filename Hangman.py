import random
import os
import time
listOfWords = ["british", "suave", "integrity", "accent", "evil", "genius", "Downton"]

word = random.choice(listOfWords)
print(word)
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
print("🌟Hangman🌟")
print()
print("You have 6 lives")
print()
blanks = []
guessWords = []
lives = 6
count = 0
usedWords = []
joinedWords = ""
wordCount = len(word)
for i in word:
  guessWords.append(i)
for i in word:
  blanks.append("_")
while True:
  userInput = input("Choose a letter: ")
  userInput = userInput.lower()
  if userInput in guessWords:
    usedWords.append(userInput)
    print("Correct!")
    indexWord = guessWords.index(userInput)
    guessWords[indexWord] = "_"
    blanks[indexWord] = userInput
    joinedWords = "".join(blanks)
    print(joinedWords)
    print()
    print(HANGMANPICS[count])
    print()
    time.sleep(2)
    os.system('clear')
    print("🌟Hangman🌟")
    print()
    print(joinedWords)
    print()
    if len(usedWords) == wordCount:
      print(f"You win with {lives} lives left")
      print()
      print(HANGMANPICS[count])
      break
  elif userInput.isnumeric() or userInput == "":
    print('Enter a word!')
    print()
    time.sleep(2)
    os.system('clear')
    print("🌟Hangman🌟")
    print()
    print(joinedWords)
    print()
  elif userInput in usedWords:
    print("That letter has been picked!")
    print()
    time.sleep(2)
    os.system('clear')
    print("🌟Hangman🌟")
    print()
    print(joinedWords)
    print()
  elif userInput not in guessWords:
    print("Nope, not in there")
    lives = lives - 1
    print(f"{lives} lives left.")
    print()
    count = count + 1
    print(HANGMANPICS[count])
    print()
    time.sleep(2)
    os.system('clear')
    print("🌟Hangman🌟")
    print()
    print(joinedWords)
    print()
    if lives == 0:
      print("You lost!")
      print()
      print(HANGMANPICS[count])
      break