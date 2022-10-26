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
      if item in myAgenda:
        print("No duplicates!")
        time.sleep(2)
        continue
      myAgenda.append(item)
      printList()
      time.sleep(2)
    elif menu == "remove":
      item = input("What do you want to remove?: ")
      question = input("Are you sure? (Y/N)\n")
      if question == "Y":
        if item in myAgenda:
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
    elif menu == "change":
      item = input("What do you want to change?\n")
      new_item = input("What do you want to change it for?\n")
      myAgenda.remove(item)
      myAgenda.append(new_item)
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