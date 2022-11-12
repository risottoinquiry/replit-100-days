import time
name = input("Name: ").capitalize().strip()
birthday = input("Date of birth (YYYY/MM/DD): ").strip()
number = input("Telephone number: ").strip()
email = input("Email: ").strip()
address = input("Address: ").strip()
contactCard = {"name": name, "birthday": birthday, "number": number, "email": email, "address": address}
print("""
----------------------------------------------------------------------

""")
time.sleep(1)
print("Here's your contact card")
print()
time.sleep(1)
print("Name:",contactCard["name"])
time.sleep(0.25)
print("Date of birth:",contactCard["birthday"])
time.sleep(0.25)
print("Tel:",contactCard["number"])
time.sleep(0.25)
print("Email:",contactCard["email"])
time.sleep(0.25)
print("Address:",contactCard["address"])