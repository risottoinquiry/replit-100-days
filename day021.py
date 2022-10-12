points = 0

print("""Math Game!

""")
multiples = int(input("Name your multiples: "))
print("")
for x in range(1, 11):
  good_answer = x*multiples
  print(x,"x",multiples)
  answer = int(input("= "))
  if answer == good_answer:
   print("Good answer!")
   points += 1
  else:
   print("Wrong! The correct answer is",good_answer)
print("You have a score of",points,"out of 10!")
if points == 10:
  print("Perfect run! Nice job.")
elif points >= 7:
  print("Almost there!")
elif points < 7:
  print("Practice makes perfect!")