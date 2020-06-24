import random

number = random.randint(1, 20)

guess = int(input("I am thinking of a number between 1 and 20. Take a guess! "))

while guess != number:
	if guess > number:
		print("Your guess is too high, guess again!")
	elif guess < number:
		print("Your guess is too low, guess again!")
	guess = input()
	guess = int(guess)
print("You guessed right, great job!")