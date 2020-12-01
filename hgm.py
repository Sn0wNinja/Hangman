from pyfiglet import figlet_format
from termcolor import colored


wanna_play = True

title = figlet_format("HANGMAN")
title = colored(title, color = "red")
print("")
print(title)

while wanna_play:

	print("")
	print("Start game? Y or N")
	start = input().upper()

	if start == "Y":
		print("Player 1, please insert the hidden word: ")
		word = input().upper()
		print("Player 2, you have 6 possible tries")
		print("Good luck! May the force be with you!")
		mat = "_" * len(word)
		guessed_letters = []
		guesses = []
		guessed_word = []
		tries = 6
		guessed = False

		while not guessed and tries > 0:

			print("Player2, please guess a letter: ")
			guess = input().upper()

			if len(guess) == 1 and guess.isalpha():
				
				if guess in guesses:
					print(f"You already tried {guess}")

				elif guess not in word:
					print(f"Sorry, {guess} is not in the hidden word")		
					tries -= 1
					guessed_letters.append(guess)
					
				else: 
					print(f"Nice! {guess} is in the hidden word")
					guessed_letters.append(guess)
					word_as_list = list(mat)
					indices = [i for i, letter in enumerate(word) if letter == guess]
					for index in indices:
						word_as_list[index] = guess
					mat = "".join(word_as_list)

					if "_" not in mat:
						guessed = True

			elif len(guess) == len(word) and guess.isalpha():
				if guess in guessed_word:
					print(f"You already tried {guess}")
				
				elif guess != word:
					print(f"{guess} is not the word")
					tries -= 1
					guessed_words.append()
				
				else:
					guessed = True
					mat = word

			else:
				print("Not a valid guess!")

			print(mat)
			print("")

		if guessed:
			print(f"Player2 congratulations, you win. The word was {word}")

		elif tries == 0:
			print("Player2, you have 0 tries left. Player1 wins")

	elif start == "N":
			print("Thank you for using our App.")
			wanna_play = False
	else:
		print("Please enter a valid input")
