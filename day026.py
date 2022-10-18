from replit import audio # import stuff i guess
import os, time

def play():
  source = audio.play_file('rick.wav')
  source.paused = False # unpause the file
  while True:
    os.system("clear")
    stop_music = int(input("Press 2 at any time to stop the music. "))
    if stop_music == 2:
      print("Pausing the music!")
      source.paused = True
      break
while True:
  os.system("clear")
  print("Music player with definetly a lot of choices!")
  time.sleep(1)
  print("Press 1 to play music!")
  time.sleep(1)
  print("Press 2 to exit!")
  time.sleep(1)
  print("Press 3 to view the menu again!")
  user_command = int(input())
  if user_command == 1:
    play()
  if user_command == 2:
    exit()
  if user_command == 3:
    continue