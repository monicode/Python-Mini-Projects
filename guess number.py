# --- GUESS THE NUMBER --- #

import random

print(" --- GUESS THE NUMBER --- \n")
print("Please guess the secrets number between 0 and 100. You have 6 attempts")

# computer chooses random number
secret_number = random.randrange(0, 100)
# max number of remaining guesses
remaining_guesses = 6

while True:

	# player guesses the secret number
	guess = input("Your number is: ")
	guess = int(guess)	
	
	# player attempts decrease 
	remaining_guesses -= 1
	
	if guess == secret_number:
		print("Correct! You win!\n")
		break
	elif guess > secret_number and remaining_guesses > 0:
		print("Lower\n")
	elif guess < secret_number and remaining_guesses > 0:
		print("Higher\n")
		
	# number of remaining guesses
	if remaining_guesses > 0:
		print("Number of remaining guesses:", remaining_guesses)
	else:
		print("\nSorry, you lose! The number was: ", secret_number)
		break
		
# --- end ---#
