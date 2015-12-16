# This allows the creation of something.
import random
# This will assign random_number to a number chosen by the program in between 1 and 1000, 
# which will make it into an integer variable.
random_number = random.randint(1,1001)
# This will print, "I'm thinking of a number between 1 and 1000. Enter your guess!"
# This will print, "Now, try to guess it in the least amount of guesses. You will be awarded points accordingly."
# This will print, "I'm thinking of a number between 1 and 1000. Enter your guess!"
print("For this game, you will guess what number I am thinking of.")
print("Now, try to guess it in the least amount of guesses. You will be awarded points accordingly.")
print("I'm thinking of a number between 1 and 1000. Enter your guess!")
# This will make a variable called guessed_number, and will assign it to the value of whatever
# was typed in by the user. This would ultimately make it into an integer variable.
guessed_number = int(raw_input())
# This makes a variable with the value of 0.
howmanyroundstakentoguess = 0

# This is a while statement, and it is saying that if the value of the variable guessed_number is 
# not the same as the value of the variable random_number, then the rest would print.
while guessed_number != random_number:
# This is an if statement, and it is saying that if the value of the variable guessed_number is
# more than the value of the variable random_number, then it would print:
# "Oops! The number that you have chosen is too high. Try again."
        if guessed_number > random_number:
                print("Oops! The number that you have chosen is too high. Try again.")

# This is an if statement, and it is saying that if the value of the variable guessed_number
# is less than the value of the variable random_number, then it would print,
# "Oops! The number that you have chosen is too low, Try again."
        if guessed_number < random_number:
                print("Oops! The number that you have chosen is too low. Try again.")
# Either way, it would ask for another number from the user, and would assign
# guessed_number to that number that the user typed in.
        guessed_number = int(raw_input())
# This is saying that the value of the variable howmanyroundstakentoguess plus one will be assigned
# to the variable howmanyroundstakentoguess, making that number the variable's next value.
        howmanyroundstakentoguess = howmanyroundstakentoguess + 1
# This is saying that if the while statement is not True, then it would print,
# "You guessed correctly, so you won the game! I wonder if you cheated.."
else:
        print("You guessed correctly, so you won the game! I wonder if you cheated...")

# This is setting the value of the variable howmanyrooundstakentoguess acordingly,
# so depending on its original value, it will be set to a specific number.


if howmanyroundstakentoguess > 1000:
        howmanyroundstakentoguess = 1
elif howmanyroundstakentoguess > 800:
        howmanyroundstakentoguess = 2
elif howmanyroundstakentoguess > 400:
        howmanyroundstakentoguess = 3
elif howmanyroundstakentoguess > 100:
        howmanyroundstakentoguess = 4
elif howmanyroundstakentoguess > 50:
        howmanyroundstakentoguess = 5
elif howmanyroundstakentoguess > 25:
        howmanyroundstakentoguess = 6
elif howmanyroundstakentoguess > 15:
        howmanyroundstakentoguess = 7
elif howmanyroundstakentoguess > 6:
        howmanyroundstakentoguess = 8
elif howmanyroundstakentoguess > 3:
        howmanyroundstakentoguess = 9
elif howmanyroundstakentoguess <> 1:
        howmanyroundstakentoguess = 10

# This will print, "You get (value of the variable howmanyroundstakentoprint) points!")
print("You get " + str(howmanyroundstakentoguess) + " points!")

