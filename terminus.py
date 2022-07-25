import subprocess
import platform
import socket
import time
import os

path = "C:/"
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)

print("""
████████╗███████╗██████╗░███╗░░░███╗██╗███╗░░██╗██╗░░░██╗░██████╗
╚══██╔══╝██╔════╝██╔══██╗████╗░████║██║████╗░██║██║░░░██║██╔════╝
░░░██║░░░█████╗░░██████╔╝██╔████╔██║██║██╔██╗██║██║░░░██║╚█████╗░
░░░██║░░░██╔══╝░░██╔══██╗██║╚██╔╝██║██║██║╚████║██║░░░██║░╚═══██╗
░░░██║░░░███████╗██║░░██║██║░╚═╝░██║██║██║░╚███║╚██████╔╝██████╔╝
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝░╚═════╝░╚═════╝░

████╗░█████╗░░░░░█████╗░░░░░░███╗░░░█████╗░████╗
██╔═╝██╔══██╗░░░██╔══██╗░░░░████║░░██╔══██╗╚═██║
██║░░██║░░██║░░░██║░░██║░░░██╔██║░░███████║░░██║
██║░░██║░░██║░░░██║░░██║░░░╚═╝██║░░██╔══██║░░██║
████╗╚█████╔╝██╗╚█████╔╝██╗███████╗██║░░██║████║
╚═══╝░╚════╝░╚═╝░╚════╝░╚═╝╚══════╝╚═╝░░╚═╝╚═══╝""")
print("Copyright Imperator Interactive AB (IIAB) and the EliCorp Family of Companies™. All Rights Reserved.")
print("If you need help, type in command 'help' for a full list of commands.")
print("...")
while True:
    code = input(">>> ")

    if code == 'help':
        print("Command not fully available.")
        print("Terminus is a shell that is able to do some things. It is in Alpha Stage.")
    if code == 'ping':
        host = input("Enter the website you want to Ping: ")
        number = input("Enter the amount of times you want to Ping: ")

        def ping(host):
            param = '-n' if platform.system().lower() == 'windows' else '-c'
            command = ['ping', param, number, host]
            return subprocess.call(command)
        print(ping(host))
    if code == 'local':
        print("Computer's date         =      " + time.strftime("%m/%d/%y"))
        print(" ")
        print("-------------------------------------------")
        print("Computer's user         =      " + host_name)
        print("Computer's IP           =      " + host_ip)
    if code == 'list':
        dir_list = os.listdir(path)
        print("Files and Directories in '", path, "':")
        print(dir_list)
    if code == 'list -a':
        file = input("Enter a file path to read: ")
        dir_list2 = os.listdir(file)
        print("Files and Directories in '" + file + "':")
        print(dir_list2)
    if code == 'echo':
        echo = input("What do you want to say: ")
        print(echo)
    else:
        print("Command " + code + " is not a command that is recognized.")