import random, os, time
def roll_health():
  dice_six1 = random.randint(1,6)
  dice_twelve1 = random.randint(1,12)
  health = (dice_six1*dice_twelve1)/2+10
  return health
def roll_strenght():
  dice_six2 = random.randint(1,6)
  dice_twelve2 = random.randint(1,12)
  strenght = (dice_six2*dice_twelve2)/2+12
  return strenght
while True:
  os.system("clear")
  print("Character Creator")
  print()
  time.sleep(1)
  name = input("What's the name of your character?: ")
  time.sleep(1)
  race = input("What's your character's race? (Human, Elf, Wizard, GNOMEEE): ")
  print()
  print("Processing...")
  time.sleep(5)
  print("Name: ",name)
  print("")
  time.sleep(1)
  print("Race: ",race)
  print("")
  time.sleep(1)
  print("Strenght: ",roll_strenght())
  print("")
  print("Health: ",roll_health())
  time.sleep(3)
  print("Long life to you, Warrior!")
  print("")
  time.sleep(2)
  question = input("Again? (Y/N) ")
  if question == "Y":
    continue
  if question == "N":
    exit()