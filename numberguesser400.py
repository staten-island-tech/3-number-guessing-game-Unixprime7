import random

randomnumber = random.randint(1,10)

randomguess = input("Pick a number from 1-10 or else... ")
guess_value = int(randomguess)

while guess_value != randomnumber:
    if guess_value > randomnumber:
        closeness = "The number is a bit smaller, try again! "
    else:
        closeness = "The number is a bit bigger, try again! "
    randomguess = input(closeness)
    guess_value = int(randomguess)
print("Nice you did it")