import random
number = random.randint(1, 1000000)
attempts = 0
print("NUMBER GUESSER! ! !")
while True:
  guess = int(input("What is your guess?: "))
  if guess < 0:
     exit()
  if guess > number:
    print("Too high")
    attempts = attempts+1
  elif guess < number:
   print("Too low")
   attempts = attempts+1
  elif guess == number:
   attempts = attempts+1
   if attempts >1:
     print("It took you",attempts,"guesses to get it correct!")
     exit()
   if attempts == 1:
      print("It took you",attempts,"guess to get it correct!")
      exit()