import os, time
def printList():
  print() 
  for item in myAgenda:
    print(item)
  print() 
def list():
  
  while True:
    os.system("clear")
    menu = input("Do you want to view your list, add something to it, remove something from it or leave?: ")
    print()
    time.sleep(1)
    if menu == "add":
      item = input("What's next on the Agenda?: ")
      myAgenda.append(item)
      printList()
      time.sleep(2)
    elif menu == "remove":
      item = input("What do you want to remove?: ")
      myAgenda.remove(item)
      printList()
      time.sleep(1)
    elif menu == "view":
      os.system("clear")
      print("This is your list.")
      print()
      printList()
      time.sleep(3)
    elif menu == "leave":
      break
print("List do-er 900!")
time.sleep(3)
while True:
  myAgenda = []
  list()
  time.sleep(1)
  question = input("Again? (Y/N) ")
  if question == "Y":
    continue
  if question == "N":
    exit()