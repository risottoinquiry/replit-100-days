import os, time
lives = 6
word = "amongus"
letterPicked = []
lives = 6

while True:
  time.sleep(1)
  os.system("clear")
  letter = input("Guess a letter: ").lower().strip()
  if letter in letterPicked:
    print("You already tried this one!")
    time.sleep(1)
    continue
  letterPicked.append(letter)
  if letter in word:
    print("Nice job! You found a letter!")
  elif letter not in word:
    print("Oops! This letter isn't in the word...")
    lives -= 1

  completion = True
  print()
  for i in word:
    if i in letterPicked:
      print(i, end="")
    else:
      print("_",end="")
      completion = False
  print()
  time.sleep(1)

  if completion:
    print(f"Nice job! You won with {lives} lives left!")
    exit()
  if lives == 0:
    print("You've lost!")
    time.sleep(0.5)
    exit()