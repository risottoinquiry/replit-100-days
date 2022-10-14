import random
number = random.randint(1, 1000000)
attempts = 0
print("NUMBER GUESSER! ! !")
while True:
  guess = int(input("What is your guess?: "))
  attempts += 1
  if guess < 0:
    exit()
  if guess > number:
    print("Too high")
  elif guess < number:
    print("Too low")
  else:
    break

guess_word = "guesses" if attempts > 1 else "guess"
print("It took you",attempts,guess_word,"to get it correct!")
