# --- HANGMAN --- #


import random

print(" --- HANGMAN --- \n")
print("Let's play! Guess the word if you don't want to hang!\n")

# computer chooses a word to guess
list_of_words = ["carrot", "dragon", "computer", "elephant", "letter", "window", "pearl", "house", \
                 "rabbit", "orange", "adventure", "mirror", "kitchen", "example", "picture", "telephone" \
				 "money", "weather", "beauty", "nothing", "birthday", "airport", "decision", "driver" \
				 "opportunity", "advertisement", "entertainment", "mountain", "button", "hairdresser"]
				 
secret_word = random.choice(list_of_words)
print(secret_word)
board =("*"*len(secret_word))
print (board)

missed_letters = []
guessed_letters = []
guess = 0
play = True

# let's play
while play:
	
	# player guesses
	letter = input("\nEnter a letter to guess: ").lower()
	
	if letter in guessed_letters or letter in missed_letters:
		print("You've entered this letter before.")
	
	if letter in secret_word:
		guessed_letters.append(letter)
	else:
		missed_letters.append(letter)
		guess += 1
	for i in range(len(secret_word)):
		if secret_word[i] == letter:
			board = board[:i] + secret_word[i] + board[i+1:] 		
	print(board)
	
	if board == secret_word:
		play = False
		print("\nCongratulation! You won!")

	print("")
	
	# draw hangman
	if guess >6:
		play = False
		print("Sorry but you didn,t guess and now you're a HANGMAN!")
		print("(BTW this is a secret word: " +  secret_word + ")")
		print("______ ")
	if guess >5:
		print("|/ |  ")
	if guess >4:
		print("|  O  ")
	if guess >3:
		print("| /|\ ")
	if guess >2:
		print("| / \ ")
	if guess >1:
		print("|      ")
	if guess >0:	
		print("======")	

print("\nBye, bye!")

# --- end --- #
