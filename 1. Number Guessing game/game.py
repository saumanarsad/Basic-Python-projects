import random
print("Welcome to the number guessing game \n")
lower = int(input("Enter the lower bound"))
upper = int(input("Enter the upper bound"))

number = random.randint(lower,upper)

print("You have only 7 guesses to get to the number")
guess = 0
chances = 1
while(chances <=7 ):
    guess = int(input("Enter the number"))
    if (guess < number):
        print("Wrong, you guessed small")
    elif(guess > number):
        print("Wrong , you guessed too high")
    else:
        print("Congrats, You did it in %d try" % chances)

    chances +=1

