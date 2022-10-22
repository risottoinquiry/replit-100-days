import time, os
def colorChange(color):
   if color == "red":
    return ("\033[31m")
   elif color == "white":
    return ("\033[0m")
   elif color == "blue":
    return ("\033[34m")
   elif color == "yellow":
    return ("\033[33m")
   elif color == "green":
     return ("\033[32m")
   elif color == "purple":
    return ("\033[35m")
#first interface
title = f"{colorChange('green')}={colorChange('white')}={colorChange('red')}= {colorChange('yellow')} Musico Appo {colorChange('green')}={colorChange('white')}={colorChange('red')}="
current_track = f"{colorChange('white')}Current track: {colorChange('yellow')}Funiculì Funiculà 10 hours mix"
next = f"{colorChange('green')}NEXT"
pause = f"{colorChange('red')}PAUSE"
#second interface
title2 = f"{colorChange('white')}WELCOME TO{colorChange('blue')} TIWTERT"
catchphrase = f"{colorChange('yellow')}Complain about stuff here!"
on_god = f"{colorChange('red')}On god."
username = f"{colorChange('white')}Username:"
password = f"{colorChange('white')}Password:"
#print section or something
print(f"             {title:^35}")
print("")
print(f"   {current_track:^25}")
print("")
print(f"    {next:^20}")
print(f"          {pause:^20}")
time.sleep(5)
os.system("clear")
time.sleep(0.5)
print(f"             {title2:^35}")
print(f"                                   {catchphrase:>35}")
print("")
print(f"            {on_god:^35}")
print("")
print(f"{username}\n{password}")