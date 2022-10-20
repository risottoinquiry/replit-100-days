import time
def colour(colour, word):
  if colour=="green":
    print("\033[32m", word, sep="",end="")
  elif colour=="red":
    print("\033[31m", word, sep="",end="")
  else:
    print("\033[0m", word, sep="", end="")
print("Epic god damn colour thing")
colour("green", "This goddamn text is in red")
time.sleep(1)
print("")
colour("reset", "oh boy")
time.sleep(1)
print("")
colour("red", "and now it's red holy crap")
time.sleep(1)
print("")
time.sleep(1)
print("If that ain't cool I don't know what is")