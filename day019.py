money = 1000
interest = 0.05
for time in range(10):
 money+=money*interest
 print("Year",time+1,"is",round(money,2),"$")