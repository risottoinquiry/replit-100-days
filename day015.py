exit = "N"
print("""ANIMAL SOUND SIMULATOR
""")
while exit == "N":
  animal = input("What animal do you want? (all in lowercase): ")
  if animal == "cow":
    print("Mooo")
  elif animal == "pig":
    print ("Oink!")
  elif animal == "sheep":
    print ("Baaa")
  elif animal == "duck":
    print("Quack")
  elif animal == "dog":
    print("Woof")
  elif animal == "cat":
    print("Meow")
  else: 
    print("Woops. I don't really know what this one is. Try again!")
  exit = input("Do you want to exit the software? (Y/N): ")