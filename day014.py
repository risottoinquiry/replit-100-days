from getpass import getpass as input
print("A W E S O M E  🗿  P A P E R  S C I S S O R S  B A T T L E")
print("")
print("Select your move (R, P or S)")
print("")
answer_1 = input("Player 1: ")
answer_2 = input("Player 2: ")
if answer_1 == "R":
  if answer_2 == "R":
    print("Player1's rock hits Player2's rock and does...nothing?")
  elif answer_2 == "P":
    print("Player1's rock is smoothered by Player2's paper! Player2 wins!")
  elif answer_2 == "S":
    print("Player1's rock SMASHES Player2's scissors. Player1 wins!")
elif answer_1 == "P":
  if answer_2 == "R":
    print("Player2's rock is smoothered by Player1's paper! Player1 wins!")
  elif answer_2 == "P":
    print("Player1's paper goes flies super fast and smashes into Player2's paper! Nothing happens. What did you even expect?")
  elif answer_2 == "S":
    print("Player2's scissors cut right through Player1's paper! Player2 wins!")
elif answer_1 == "S":
 if answer_2 == "R":
    print("Player2's rock SMASHES Player1's scissors. Player2 wins!")
 elif answer_2 == "P":
   print("Player1's scissors cut right through Player2's paper! Player1 wins!")
elif answer_2 == "S":
  print("What do you even do with 2 scissors? How disappointing.")
else:
  print("Error 404")