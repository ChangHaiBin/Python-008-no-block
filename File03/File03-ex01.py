# Take a look at the following file first.
# Play with the game if you want.

import random

def give_hint(guess, answer):
    if guess < answer:
        print(f"Your guess of {guess} is less than the answer.")
    elif guess > answer:
        print(f"Your guess of {guess} is more than the answer.")
    else:
        print("You have gotten the right answer.")

answer = random.randint(1, 100)
print("A random number from 1 to 100 has been generated")
guess = -1

while guess != answer:
    print("Please guess the number:")
    guess = int(input())
    give_hint(guess=guess, answer=answer)

print("You win!")
