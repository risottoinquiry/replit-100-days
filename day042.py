import os, time, random


def colorChange(color):
  if color == "r":
    return '\033[31m'
  elif color == "w":
    return '\033[0m'
  elif color == "b":
    return '\033[34m'
  elif color == "y":
    return '\033[33m'
  elif color == "g":
    return '\033[32m'
  elif color == "p":
    return '\033[35m'
  elif color == "dark_red":
    return '\033[31;2m'
  elif color == "light_green":
    return '\033[92m'
  elif color == "light_yellow":
    return '\033[93m'
  elif color == "light_blue":
    return '\033[94m'
  elif color == "light_purple":
    return '\033[95m'
  elif color == "cyan":
    return '\033[36m'
  elif color == "light_gray":
    return '\033[37m'
  elif color == "dark_gray":
    return '\033[90m'
  elif color == "bright_red":
    return '\033[91m'
  elif color == "bright_green":
    return '\033[92m'
  elif color == "bright_yellow":
    return '\033[93m'
  elif color == "bright_blue":
    return '\033[94m'
  elif color == "bright_purple":
    return '\033[95m'


print(f"{colorChange('p')}Dokémon!{colorChange('w')}")  #literally just the title
print()
time.sleep(1)
first_question = input(f"Would you like to start a new game? ({colorChange('g')}Yes{colorChange('w')}/{colorChange('r')}No{colorChange('w')}) ")

  





if first_question == "No":
  time.sleep(1)
  print()
  print("bruh")  #comedy
  print()
  time.sleep(0.5)
  exit()

elif first_question == "Yes" or "Y" or "y" or "yes" or "oui" or "Oui":
  os.system("clear")
  print("Alright now, let's create your dokémon.")
  time.sleep(1)
  print()
  name = input("Input your dokémon's name > ")
  print()
  type = input("Input your dokémon's type > ")
  print()
  move = input("Input your dokémon's special move > ")
  print()
  hp = int(input("Input your dokémon's starting HP (not higher than 50) > "))
  print()
  if hp > 50:
    os.system("clear")
    time.sleep(0.5)
    colorChange('r')
    print("No cheating! (HP was higher than 50)")
    exit()
  mp = int(input("Input your dokémon's starting MP (not higher than 50) > "))
  if mp > 50:
    os.system("clear")
    time.sleep(0.5)
    colorChange('r')
    print("No cheating! (MP was higher than 50)")
    exit()
  time.sleep(3)
  print()
  print()
  colorChange("g")
  os.system("clear")

  
  print(f"Your dokémon is called {colorChange('p')}{name}{colorChange('w')}") #print all values
  time.sleep(1)
  print(f"It is a {colorChange('bright_yellow')}{type}{colorChange('w')} dokémon.")
  time.sleep(1)
  print(f"It's special move is {colorChange('y')}{move}{colorChange('w')}.")
  time.sleep(1)
  print(f"It has{colorChange('bright_red')} {hp}{colorChange('w')} starting health points and {colorChange('bright_blue')}{mp}{colorChange('w')} starting stamina.")
  time.sleep(2)
  os.system("clear")

  
  print(f"Now, let's roll it's {colorChange('r')}strenght{colorChange('w')}.") #strenght stat roll
  dice_one = random.randint(1, 5)
  dice_two = random.randint(1, 4)
  strenght = dice_one*dice_two
  print()
  time.sleep(2)
  print(f"Your dokémon has {colorChange('r')}{strenght} strenght {colorChange('w')}!")
  time.sleep(1)
  os.system("clear")
  time.sleep(0.5)
  print("Now for his rival...")
  print("")
  time.sleep(2)
  name2 = input(f"What's the name of his {colorChange('r')}opponent{colorChange('w')}? ")
  time.sleep(1)
  print()
  print("Let's roll his stats...")
  time.sleep(2)
  dice_three = random.randint(1, 5)
  dice_four = random.randint(1, 4)
  dice_five = random.randint(5, 10)
  dice_six = random.randint(1,5)
  strenght2 = dice_three*dice_four
  hp2 = dice_five*dice_six
  print()
  print(f"Your opponent has {colorChange('bright_red')} {hp2}{colorChange('w')} health points and{colorChange('r')} {strenght2}{colorChange('w')} strenght")
  time.sleep(2)
  time.sleep(1)
  os.system("clear")


  
  print("⚔ Let the battle begin! ⚔") #battle
  rounds = 1
  time.sleep(2)
  while True:
    os.system("clear")
    print("Round",rounds)
    time.sleep(2)
    print("")
    dice_good = random.randint(1,6)
    dice_bad = random.randint(1,6)
    if dice_good > dice_bad:
      print("Your character wins the round!")
      hp2 =- strenght
      rounds += 1
      time.sleep(2)
    elif dice_good < dice_bad:
      print("Your enemy wins the round...")
      hp =- strenght2
      rounds += 1
      time.sleep(2)
    elif dice_good == dice_bad:
      print("It's a draw!")
      rounds += 1
      time.sleep(2)
    if hp <= 0:
      time.sleep(2)
      rounds -= 1
      print("Your character has lost in",rounds,"rounds...play the sad trumpet music.")
      time.sleep(2)
      break
    if hp2 <= 0:
      rounds -= 1
      time.sleep(2)
      print("Your character has won in",rounds,"rounds! Glory of ages!")
      time.sleep(2)
      break
    print(name,"has",hp,"health left")
    time.sleep(1)
    print(name2,"has",hp2,"health left")
    time.sleep(3)


#whew


  
  os.system("clear")
  time.sleep(1)
  print(f"{colorChange('p')}Nice job on completing the game! You can try it again. You'll have to make a new character though (J'ai pas la moindre idée comment je pourrais faire un système de sauvegarde pour garder le même personnage et j'ai l'impression que le projet est déjà un peu long).")
  exit()



else:
  print()
  print("What? I didn't really catch you there. Let's try that again.")
  time.sleep(1)
  exit()


#200 lignes