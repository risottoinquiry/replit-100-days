import os,time
name_list = []
def printList():
 print()
 for i in name_list:
   print(i)
 print()
def list():
  while True:
    name = input("What's your name (first and last)?: ").capitalize().strip()
    if name not in name_list:
      name_list.append(name)
      printList()
    elif name:
      print("ERROR: No duplicates.")
    time.sleep(2)
    os.system("clear")
print("Name list-er 9000!")
list()