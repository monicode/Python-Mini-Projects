# --- MASTERMIND --- #

import random

print (" --- MASTERMIND --- \n")
print ("Guess the secret color code in as few tries as possible.\n")
print ("Please, enter your color code.\nYou can use red(R), green(G), blue(B), yellow(Y), white(W) and pink(P)")

colors = ["R", "G", "B", "Y", "W", "P"]
attempts = 0
game = True

# computer randomly picks four-color code
color_code = random.sample(colors,4)	
print (color_code)

# player guesses the number	
while game:
	correct_color = ""
	guessed_color = ""
	player_guess = input().upper()
	attempts += 1
	
	# checking if player's input is correct
	if len(player_guess) != len(color_code):
		print ("\nThe secret code has exactly four colors. I know, you can count to four. Try again!")
		continue
	for i in range(4):
		if player_guess[i] not in colors:
			print ("\nLook up what colors you can use in this game. You are not a daltonist, are you?")
			continue
			
	# comparison between player's input and secret code
	if correct_color != "XXXX":
		for i in range(4):
			if player_guess[i] == color_code[i]:
				correct_color += "X"
			if  player_guess[i] != color_code[i] and player_guess[i] in color_code:
				guessed_color += "O"
		print (correct_color +  guessed_color + "\n")		
		
	if correct_color == "XXXX":
		if attempts == 1:
			print ("Wow! You guessed at the first attempt!")
		else:
			print ("Well done... You needed " + str(attempts) + " attempts to guess.")
		game = False
		
	if attempts >= 1 and attempts <6 and correct_color != "XXXX":
		print ("Next attempt: ")
	elif attempts >= 6:
		print ("You didn't guess! The secret color code was: " + str(color_code))	

	# play or not to play
	while game == False:
		finish_game = input("\nDo you want to play again (Y/N)?").upper()	
		attempts = 0
		if finish_game =="N":
			print ("Thanks for the game! Bye, bye!")
		elif finish_game == "Y":
			game = True
			print ("So, let's play again... Guess the secret code: ")

# --- end --- #			