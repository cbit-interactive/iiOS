import time
import os
import socket
import psutil
import time
from loadbar import LoadBar

battery = psutil.sensors_battery()
login_pass = open('user/password.txt')
login_name = open('user/username.txt')
l_p = login_pass.read()
l_n = login_name.read()

bar = LoadBar(max=100)
bar.start()
for i in range(100):
    time.sleep(0.05)
    bar.update(step=i)
bar.end()

print("""

╔╦╦═╦══╗
╠╬╣║║══╣
║║║║╠══║
╚╩╩═╩══╝

Version 0.1.1a Beta 2

""")
print("Welcome " + l_n + " to iiOS!")

bar = LoadBar(max=300)
bar.start()
for i in range(300):
    time.sleep(0.05)
    bar.update(step=i)
bar.end()

print(" ")
print("==================================================")
print(" ")
print(time.strftime("%m/%d/%y"))
print("--------------------------------------------------")
print("Battery level: ")
print(battery.percent)
print("--------------------------------------------------")
print("""
All programs
[1] Para Omnia Browser for Python (POBP) (0.1)
[2] Textpro Text Editor for Python (TTEP) (0.1)
[3] Coolfile (0.1) - Coolfile 0.1 is not available to open
[4] Terminus (0.1)
[5] POMail (0.1) - Not available to open
[6] PicEdit
[7] Gamemaster
[8] Configure and Open BIOS
[9] Save and Exit iiOS
""")
print("""
List of Unavailable programs:
[1] Coolfile
[2] POMail
[3] PicEdit
[4] Gamemaster
""")
print("""
List of programs in TESTING:
[1] Coolfile
[2] POMail
""")
select = input(">> ")

if select == '1':
    os.startfile('brows.py')
if select == '2':
    os.startfile('edit.py')
if select == '3':
    os.startfile('error.py')
if select == '4':
    os.startfile('terminus.py')
if select == '5':
    os.startfile('error.py')
if select == '8':
    while True:
        b_login = input(str("Please enter the password for " + l_n + " to enter BIOS: "))
        if b_login == l_p:
            os.startfile("bios.py")
            os.exit
