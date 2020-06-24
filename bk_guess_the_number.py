# This is a guess the number game from the book

# import the random module
import random

# assign a random number between 1 and 20 to the variable 'number'
number = random.randint(1, 20)

# print a string
print('I am thinking of a number between 1 and 20.')

# a for loop, after each iteration the variable guesses is incremented by 1
# range(1, 7) start the variable guesses at 1 and go up to 6, when guesses goes
# past 6, it exits the for loop
for guesses in range(1, 7):
	# print a string
	print('Take a guess: ')
	# take the user's input, convert it to an integer, and assign it to the
	# variable 'guess'
	guess = int(input())

	# check if the user guessed the right number
	# if user's guess is less than the number, tell them its too low
	if guesses == 5:
		if guess < number:
			print('Your guess is too low, last guess!')
		elif guess > number:
			print('Your guess is too high, last guess!')

	elif guesses == 6:
		break
	elif guess < number:
		print('Your guess is too low! You have ' + str(6 - guesses) + ' more '
			'guesses.')
	# if user's guess is higher than the number, tell them its too high
	elif guess > number:
		print('Your guess is too high! You have ' + str(6 - guesses) + ' more '
			'guesses.')
	# this allows the program to break from the if loop if you guess the number
	else:
		break

# check if the guess variable equals the number variable
if guess == number:
	# if the guess variable equals the number variable, tell the user
	print('Good job! You guessed my number after ' + str(guesses) + ' guesses!')
# otherwise, tell the user the number if they ran out of tries
else:
	print('Sorry, the number I was thinking of was ' + str(number) + '!')