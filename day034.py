import os, time
listOfEmail = []
def colorChange(color):
   if color == "red":
    return ("\033[31m")
   elif color == "white":
    return ("\033[0m")
   elif color == "blue":
    return ("\033[34m")
   elif color == "yellow":
    return ("\033[33m")
   elif color == "green":
     return ("\033[32m")
   elif color == "purple":
    return ("\033[35m")


def SpamEm(max):
  for x in range(1,max):
    print(f"""Email {x}

    Dear {listOfEmail[x]},
    Own a musket for home defense, since that's what the founding fathers intended. Four ruffians break into my house. "What the devil?" As I grab my powdered wig and Kentucky rifle. Blow a golf ball sized hole through the first man, he's dead on the spot. Draw my pistol on the second man, miss him entirely because it's smoothbore and nails the neighbors dog. I have to resort to the cannon mounted at the top of the stairs loaded with grape shot, "Tally ho lads" the grape shot shreds two men in the blast, the sound and extra shrapnel set off car alarms. Fix bayonet and charge the last terrified rapscallion. He Bleeds out waiting on the police to arrive since triangular bayonet wounds are impossible to stitch up. Just as the founding fathers intended.
    
    My kindest wishes to the kids, 
    Bartolomey B. Watson""")
    time.sleep(3)
    os.system("clear")
    


def prettyPrint():
  os.system("clear") 
  print("listofEmail") 
  print() 
  for index in range(len(listOfEmail)): 
    print(f"{colorChange('red')}{index}: {listOfEmail[index]}{colorChange('white')}")  
  time.sleep(2)

  
while True:
  print("SPAMMER Inc.")
  menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
  if menu == "1":
    email = input("Email > ")
    listOfEmail.append(email)
  elif menu =="2":
    email = input ("Email > ")
    if email in listOfEmail:
      listOfEmail.remove(email)
  elif menu == "3":
    prettyPrint()
  elif menu == "4":
    SpamEm(10)
  time.sleep(1)
  os.system("clear")
