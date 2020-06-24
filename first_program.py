# This program prints hello and asks for my name

# print Hello World
print('Hello World!')
# ask for the user's name
print('What is your name?')
# collect the user's input and put it into variable myName
myName = input()

print('It is good to meet you, ' + myName)
print('The length of your name is:')
# find the length of the string in variable myName and print it
print(len(myName))
test = len(myName)

# print('What is your age?')
myAge = input('What is your age?')
# take the user's input, add 1 to it, convert it to a strin, and print the text
print('You will be ' + str(int(myAge) + 1) + ' in a year.')

print(type(test))
