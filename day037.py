print("🌟Star Wars Name Generator🌟")
print()
first_name = input("Input your first name > ").capitalize()
print()
last_name = input("Input your last name > ").lower()
print()
maiden_name = input("Input your mother's last name > ").capitalize()
print()
city = input("Input the city where you were born > ").capitalize()
print()
name = f"{first_name[:3]}{last_name[:3]} {maiden_name[:3]}{city[-3:]}"
print("Your Star Wars name is",name)