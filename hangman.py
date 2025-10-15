"""
imports allow us to pull in functions/modules/etc from installed libraries/packages
because we want to randomize word picking, we import the built-in random module
"""
import random

def pickWord() -> str: # only touch the words list, otherwise this works fine
	"""
	this function picks our word for us from a list we defined
	"""
	words = ["apple", "computer", "fun", "python", "word", "another"]
	return random.choice(words)

def verifyGuess(guess:str) -> bool:
	"""
	here we need to check if a user's guess is in the word (correct)
	"""
	global lives, guessedLetters, word

	# if a guess is repeated
	if guess in guessedLetters:
	#	tell the user	
		print("Already used this letter")
	#	don't process the guess
		return False
	
	guessedLetters.append(guess)

	# if the guess is not in the word (wrong)
	if guess not in word:
	#	remove a life
		lives -= 1
		return False
	
	return True

def validateGuess(guess:str) -> bool:
	"""
	This should make sure the user put a valid guess (no !@#$% or abc or anything else weird)
	"""
	# Check if the guess is exactly 1 character
	if len(guess) != 1:
		print("Hey, the guess can only be 1 character")
	# Check if the character is in our valid characters
	elif guess not in "abcdefghijklmnopqrstuvwxyz":
		print("Char not valid")
	#	If any of these were false, tell the user
	# Otherwise, process the guess
	else:
		return True
	return False

def checkState():
	"""
	This makes sure that the game is either playing or ended (win or lose)
	"""
	global state, blankWord, lives

	# If we don't have any more blanks to fill, the word is guess, update the state to a win!
	if "-" not in blankWord:
		state = "Win"

	# If we ran out of lives.... update the state to a lose :(
	if lives == 0:
		state = "Lose"

def fillBlanks(guess:str):
	"""
	Here we want to fill the blanks from the user's guesses
	"""
	global word, blankWord

	# for each letter in the word
	#	if the guess is equal to that letter
	#		fill in the blank
	for index, letter in enumerate(word):
		if guess == letter:
			blankWord[index] = guess

# These are our global game variablesa
lives = 6 # if this runs down to 0, game over
state = "playing" # tells the game if it should keep going
word = pickWord() # lets replace this to pick our word
blankWord = ["-"] * len(word) # this is what we show the user for their progress
guessedLetters = [] # this holds all the user's guesses

while state == "playing":
	"""
	This is the game loop

	Each step happens one at a time, until the game is no longer "playing"
	"""
	# Show the user their progress
	print("lives", lives)
	print(" ".join(blankWord))

	# Ask the user for a guess
	userGuess = input("Guess a letter: ").lower()

	# Make sure their guess is what we expected
	if not validateGuess(userGuess):
		print()
		continue

	# Fill in any blanks is it's a good guess
	if verifyGuess(userGuess):
		fillBlanks(userGuess)

	# Lets check if we won or lost
	checkState()
	
	print()

# We'll show the word here
print(word)

# Then show the user if they won or lost depending on the final state
if state == "Win":
	print("Congrats, you Win!")
else:
	print("BooHoo, too bad soo sad")