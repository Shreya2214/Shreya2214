import random

count = 0
limit = 3
num = random.randint(1,50)

print("I am thinking about a number from 1 to 50")
print("Can you try and guess that?")

while count < limit:
    guess = input("Enter your guess: ")
    guess = int(guess)
    count += 1

if guess > num and count < limit:
    print("Try again! But this time lower")
elif guess < num and count< limit:
    print("Try again! But this time higher")
elif guess == num and count <= limit:
    print("You won!")
else:
    print(f"Nope the number i was guessing was {num}")
