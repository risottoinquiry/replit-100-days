print("""List generator

""")
start = int(input("Start at: "))
end = int(input("End before: "))
increment = int(input("Increment between values: "))
print("")
for x in range (start,end,increment):
  print(x)