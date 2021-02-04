import random
from hangman_art import stages, logo
from hangman_words import word_list

chosen_word = random.choice(word_list)

print(logo)
#Testing code
#print(f'solution: {chosen_word}.')

#List to display "_" 
display = []

for letter in chosen_word:
  display += "_"
print(" ".join(display))

#Fonction for guessing letter
def guessLetter():
  letterPosition = 0  
  for letter in chosen_word:
    if letter == guess:
      display[letterPosition] = guess
    letterPosition += 1
  print(" ".join(display))

lives = 6
triedLetter = []  

while display.count('_') and lives > 0:
  guess = input("Guess a letter: ").lower()

  if triedLetter.count(guess) == False:
    guessLetter()
    if display.count(guess) == False:
      lives -= 1
      print(f"{guess} is not a letter of the word you are looking for")
    print(stages[lives])
  else: 
    print("You already tried this letter")
  triedLetter += guess
else:
  if lives == 0:
    print("You losed")
  else:
    print("You win")
