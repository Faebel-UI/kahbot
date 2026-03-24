from os import system

from kahootSpam import main as kahoot

print("---------------------------------------")
print("         Roeppli's Exploit Hub")
print("---------------------------------------\n")

MODE = int(input("[1] Kahoot\n[2] Coming Soon\n--> "))
if MODE == 1:
  system("clear")
  kahoot()
