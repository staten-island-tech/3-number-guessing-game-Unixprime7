import random

randomnumber = random.randint(1,10)

randomguess = input("Pick a number from 1-10 or else... ")
guess_value = int(randomguess)
guess_list = []

while guess_value != randomnumber:
    guess_list.append(guess_value)
    print("Here are the guesses you've made so far: ", guess_list)
    if guess_value > randomnumber:
        closeness = "The number is a bit smaller, try again! "
    else:
        closeness = "The number is a bit bigger, try again! "
    randomguess = input(closeness)
    guess_value = int(randomguess)
guess_list.append(randomnumber)
print("Nice you did it")
print('Guess history:', guess_list)