# Import the random module
import random

# Import the enchant module for checking the dictionary
import enchant
d = enchant.Dict("en_US")

# Define the list of vowels and consonants
vowels = ["a", "e", "i", "o", "u"]
consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

# Define a function to generate a random word
def generate_word():
  # Initialize an empty word
  word = ""
  # Choose a random length between 3 and 10
  length = random.randint(6, 10)
  # Choose a random starting letter, either vowel or consonant
  start = random.choice(vowels + consonants)
  # Add the starting letter to the word
  word += start
  # Loop until the word reaches the desired length
  while len(word) < length:
    # If the last letter was a vowel, choose a consonant next
    if word[-1] in vowels:
      next_letter = random.choice(consonants)
    # If the last letter was a consonant, choose a vowel next
    else:
      next_letter = random.choice(vowels)
    # Add the next letter to the word
    word += next_letter
  # Return the word
  return word

# Generate a random word that does not exist in the dictionary
n=0
word = generate_word()
while d.check(word) or n < 30:
  word = generate_word()
  n+=1
  print(word)
