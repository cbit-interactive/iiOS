import time
import os
import socket
import psutil
import time

host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
battery = psutil.sensors_battery()
login_pass = open('user/password.txt')
login_name = open('user/username.txt')
l_p = login_pass.read()
l_n = login_name.read()

print("""

╭━━╮╱╱╱╱╱╱╱╱╱╭━╮╱╱╱╱╱╱╱╭━━━┳━━━╮
┃╭╮┃╱╱╱╱╱╱╱╱╱┃╭╯╱╱╱╱╱╱╱┃╭━╮┃╭━╮┃
┃╰╯╰┳┳━━┳━━╮╭╯╰┳━━┳━╮╭┳┫┃╱┃┃╰━━╮
┃╭━╮┣┫╭╮┃━━┫╰╮╭┫╭╮┃╭╯┣╋┫┃╱┃┣━━╮┃
┃╰━╯┃┃╰╯┣━━┃╱┃┃┃╰╯┃┃╱┃┃┃╰━╯┃╰━╯┃
╰━━━┻┻━━┻━━╯╱╰╯╰━━┻╯╱╰┻┻━━━┻━━━╯

""")
print("[1] USERNAME: " + l_n)
print("[2] PASSWORD: " + l_p)
print("HOST NAME: " + host_name)
print(" HOST IP: " + host_ip)

edit_b = input("Enter [?] to change a BioS setting: ")
if edit_b == '1':
    edit_n = input("Enter new USERNAME: ")
    with open('user/username.txt', 'w') as f:
        f.writelines(edit_n)
        print("USERNAME changed to " + edit_n)
        input("Press <ENTER> to exit the program")
if edit_b == '2':
    edit_p = input("Enter new PASSWORD: ")
    with open('user/password.txt', 'w') as f:
        f.writelines(edit_p)
        print("PASSWORD changed to " + edit_p)
        input("Press <ENTER> to exit the program")