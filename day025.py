def CharacterStats():
  while True:
    import random
    dice6 = random.randint(1,6)
    dice8 = random.randint(1,8)
    dice_total = dice6*dice8
    name = input("What's your character's name? ")
    print("Name of your warrior: ",name)
    print("Their health is: ",dice_total)
    reroll = input("Do you want to reroll? (Y/N) ")
    if reroll == "Y":
      continue
    elif reroll == "N":
      print("See ya!")
      break
print("Character Stats Generator!")
CharacterStats()