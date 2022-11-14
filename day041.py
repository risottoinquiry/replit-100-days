import os, time

def colorChange(color): #thing for colors
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

name = input("Name: ").strip().capitalize()
url = input("Url: ").strip()
desc = input("Desc: ")
rating = input("Rating: ")

website = {"Name": name, "Url": url, "Desc": desc, "Rating": rating}
print()
os.system("clear")
time.sleep(1)

for name, value in website.items():
  print(f"{colorChange('red')}{name}: {value}")
  time.sleep(0.5)