print("""Exam Grade Calculator
""")
name = input("Name of the exam: ")
max_score = int(input("Max. Possible Score: "))
score = int(input("Your score: "))
print("")
pourcentage = score/max_score*100  
if pourcentage <60:
  letter = "E"
elif pourcentage <70:
  letter = "D"
elif pourcentage <80:
  letter = "C"
elif pourcentage <90:
  letter = "B"
elif pourcentage <100:
  letter = "A"
elif pourcentage == 100:
  letter = "A+"
else:
  print("what in oblivion")
print("You got",pourcentage,"% which is a",letter) 