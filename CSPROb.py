import random
random_number = random.randint(1,6)
print(random_number)
print("I'm thinking of a number between 1 and 5. Enter your guess!")
guessed_number = int(raw_input())

while guessed_number > random_number:
        print("The number is wrong. Try again.")
        guessed_number = raw_input()
while guessed_number < random_number:
        print("The number is wrong. Try again.")
        guessed_number = raw_input()
else:
        print("You guessed correctly, so you won the game! I wonder if you cheated...")

