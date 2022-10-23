import random, os, time
while True:
  os.system("clear")
  text = ["Hello", "Bonjour", "Ciao", "Hallo", "привет", "Dia dhuit", "Hola", "Olà", "Witam"]
  x = random.randint(0,7)
  print(text[x])
  question = input("Go again? (Y/N) ")
  if question == "Y":
    continue
  elif question == "N":
    print("See ya!")
    break