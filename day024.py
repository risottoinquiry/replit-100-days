def rollDice():
  while True:
    import random
    max = int(input("How many sides? "))
    dice = random.randint(1, max)
    print("You rolled",dice)
    question = input("Role again? (Y/N): ")
    if question == "Y":
      continue
    elif question == "N":
      print("See ya!")
      break
  else:
      print("bruh")
print("I N F I N I T Y  D I C E 🤯🎲")
rollDice()