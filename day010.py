print("Tip Calculator")
print("--------------")
money_spent = float(input("How much did you spend?: "))
tip = int(input("What percentage did you want to tip?: "))
money_spent = tip/100*money_spent+money_spent
people = int(input("How many people are in your group? "))
money_spent_per_person = money_spent / people 
total_amount = round(money_spent_per_person, 2)
print("You each owe",total_amount,"$")