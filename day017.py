from getpass import getpass as input
RoundCounter = 1
Player1Score = 0
Player2Score = 0
print("A W E S O M E  🗿  P A P E R  S C I S S O R S  B A T T L E")
while True:
 print("")
 print("ROUND",RoundCounter)
 RoundCounter = RoundCounter+1
 print("Select your move (R, P or S)")
 print("")
 answer_1 = input("Player 1: ")
 answer_2 = input("Player 2: ")
 if (answer_1, answer_2) == ("R", "R"):
   print("Player1's rock hits Player2's rock and does...nothing?")
 elif (answer_1, answer_2) == ("R", "P"):
   print("Player1's rock is smoothered by Player2's paper! Player2 wins!")
   Player2Score = Player2Score+1
 elif (answer_1, answer_2) == ("R", "S"):
   print("Player1's rock SMASHES Player2's scissors. Player1 wins!")
   Player1Score = Player1Score+1
 elif (answer_1, answer_2) == ("P", "R"):
   print("Player2's rock is smoothered by Player1's paper! Player1 wins!")
   Player1Score = Player1Score+1
 elif (answer_1, answer_2) == ("P", "P"):
   print("Player1's paper goes flies super fast and smashes into Player2's paper! Nothing happens. What did you even expect?")
 elif (answer_1, answer_2) == ("P", "S"):
   print("Player2's scissors cut right through Player1's paper! Player2 wins!")
   Player2Score = Player2Score+1
 elif (answer_1, answer_2) == ("S", "R"):
   print("Player2's rock SMASHES Player1's scissors. Player2 wins!")
   Player2Score = Player2Score+1
 elif (answer_1, answer_2) == ("S", "P"):
   print("Player1's scissors cut right through Player2's paper! Player1 wins!")
   Player1Score = Player1Score+1
 elif (answer_1, answer_2) == ("S", "S"):
   print("What do you even do with 2 scissors? How disappointing.")
 else:
   print("Error 404") 
 if Player1Score == 3:
   print("Player1 wins the game!")
   exit()
 if Player2Score == 3:
   print("Player2 wins the game!")
   exit()