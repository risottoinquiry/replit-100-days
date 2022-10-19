import random, os, time
def roll_health1():
  dice_six1 = random.randint(1,6)
  dice_twelve1 = random.randint(1,12)
  health = (dice_six1*dice_twelve1)/2+10
  return health
def roll_strenght1():
  dice_six2 = random.randint(1,6)
  dice_twelve2 = random.randint(1,12)
  strenght = (dice_six2*dice_twelve2)/2+12
  return strenght
def roll_health2():
  dice_six3 = random.randint(1,6)
  dice_twelve3 = random.randint(1,12)
  health2 = (dice_six3*dice_twelve3)/2+10
  return health2
def roll_strenght2():
  dice_six3 = random.randint(1,6)
  dice_twelve3 = random.randint(1,12)
  strenght2 = (dice_six3*dice_twelve3)/2+12
  return strenght2
health1 = roll_health1()
health2 = roll_health2()
strenght1 = roll_strenght1()
strenght2 = roll_strenght2()
while True:
  os.system("clear")
  print("Character Creator")
  health1 = roll_health1()
  health2 = roll_health2()
  strenght1 = roll_strenght1()
  strenght2 = roll_strenght2()
  print()
  time.sleep(1)
  name1 = input("What's the name of your character?: ")
  time.sleep(1)
  race1 = input("What's your character's race? (Human, Elf, Wizard, GNOMEEE): ")
  print()
  print("Processing...")
  time.sleep(5)
  print("Name: ",name1)
  print("")
  time.sleep(1)
  print("Race: ",race1)
  print("")
  time.sleep(1)
  print("Strenght: ",strenght1)
  print("")
  print("Health: ",health1)
  print("")
  time.sleep(3)
  print("Now for his enemy...")
  print("")
  time.sleep(3)
  name2 = input("What's the name of his enemy?: ")
  time.sleep(1)
  race2 = input("What's the race of his enemy?: ")
  print("")
  print("Processing...")
  time.sleep(5)
  print("Name: ",name2)
  print("")
  time.sleep(1)
  print("Race: ",race2)
  print("")
  time.sleep(1)
  print("Strenght: ",strenght2)
  print("")
  print("Health: ",health2)
  print("")
  time.sleep(5)
  os.system("clear")
  time.sleep(1)
  os.system("clear")
  print("⚔ Let the battle begin! ⚔")
  rounds = 1
  time.sleep(2)
  while True:
    os.system("clear")
    print("Round",rounds)
    time.sleep(5)
    print("")
    dice_good = random.randint(1,6)
    dice_bad = random.randint(1,6)
    if dice_good > dice_bad:
      print("Your character wins the round!")
      health2 =- strenght1
      rounds += 1
      time.sleep(5)
    elif dice_good < dice_bad:
      print("Your enemy wins the round...")
      health1 =- strenght2
      rounds += 1
      time.sleep(5)
    elif dice_good == dice_bad:
      print("It's a draw!")
      rounds += 1
      time.sleep(5)
    if health1 <= 0:
      time.sleep(2)
      rounds -= 1
      print("Your character has lost in",rounds,"rounds...play the sad trumpet music.")
      time.sleep(5)
      break
    if health2 <= 0:
      rounds -= 1
      time.sleep(2)
      print("Your character has won in",rounds,"rounds! Glory of ages!")
      time.sleep(5)
      break
    print(name1,"has",health1,"health left")
    time.sleep(2)
    print(name2,"has",health2,"health left")
    time.sleep(2)
  question = input("Again? (Y/N) ")
  if question == "Y":
    continue
  if question == "N":
    exit()