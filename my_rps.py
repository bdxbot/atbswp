import random
import sys

weapon = ''
win = 0
loss = 0
tie = 0

computer_arsenal = ['ROCK', 'PAPER', 'SCISSORS']

print('ROCK, PAPER, SCISSORS')

while weapon != 'q':
	print('\nW: ' + str(win) + ' L: ' + str(loss) + ' T: ' + str(tie))
	print('Choose your weapon: (r)ock, (p)aper, (s)cissors or (q)uit')
	weapon = input()

	if weapon == 'r':
		weapon = 'ROCK'
	elif weapon == 'p':
		weapon = 'PAPER'
	elif weapon == 's':
		weapon = 'SCISSORS'
	elif weapon == 'q':
		print('\n		Thanks for playing, goodbye!')
		sys.exit()

	computer_weapon = computer_arsenal[random.randint(0, 2)]

	print('\nYou picked ' + weapon + ' and your opponent picked ' + computer_weapon)

	if weapon == 'ROCK' and computer_weapon == 'ROCK':
		print('Result: TIE!')
		tie += 1
	elif weapon == 'ROCK' and computer_weapon == 'PAPER':
		print('Result: YOU LOSE!')
		loss += 1
	elif weapon == 'ROCK' and computer_weapon == 'SCISSORS':
		print('Result: YOU WIN!')
		win += 1
	elif weapon == 'PAPER' and computer_weapon == 'PAPER':
		print('Result: TIE!')
		tie += 1
	elif weapon == 'PAPER' and computer_weapon == 'SCISSORS':
		print('Result: YOU LOSE!')
		loss += 1
	elif weapon == 'PAPER' and computer_weapon == 'ROCK':
		print('Result: YOU WIN!')
		win += 1
	elif weapon == 'SCISSORS' and computer_weapon == 'SCISSORS':
		print('Result: TIE!')
		tie += 1
	elif weapon == 'SCISSORS' and computer_weapon == 'ROCK':
		print('Result: YOU LOSE!')
		loss += 1
	elif weapon == 'SCISSORS' and computer_weapon == 'PAPER':
		print('Result: YOU WIN!')
		win += 1