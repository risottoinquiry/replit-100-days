counter = 0
print("""Fill in the blank Lyrics!
(type in the blank lyrics

""")
while True:
 print("Might as well ____!")
 answer = input()
 if answer == "jump":
   print("Well done, it only took you",counter,"attempts! 💀")
   break
 else:
   print("Not quite that one, try again.") 
   print("")
   counter += 1