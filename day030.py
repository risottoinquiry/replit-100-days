import os, time
for i in range(1,31):
  os.system("clear")
  days = "30 days down, what do you think?"
  print(f"{days: ^50}")
  print(f"Day {i}: ")
  opinion = input("")
  text = f"You thought Day {i} was {opinion: <2}"
  print(f"{text: ^50}")
  time.sleep(3)