def login():
  while True:
   username = input("What is your username? ")
   password = input("What is your password? ")
   if username == "notarisotto" and password == "amongus":
     print("Welcome to Replit, notarisotto!")
     break
   else:
     print("User or password not found! Please verify your informations are correct or visit this link to reset your password: https://youtu.be/xvFZjo5PgG0 ")
print("LOG INTO REPLIT!")
login()