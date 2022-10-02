print("How many seconds are there in a year?")
print("------------------------------------")
answer = input("Proceed? (Y/N): ")
if answer == "Y":
  minute = 60
  hour = 60*60
  day = hour*24
  number_of_days = int(input("How many days are there this year?: "))
  year = day*number_of_days
  print("There is",year,"seconds in a year!")
elif answer == "N":
  print("Okay! Nothing coming your way.")
else:
  print("error 404")