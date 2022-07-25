import wget
import os
from zipfile import ZipFile 

print("""
╱╱╭━━━┳━━━╮╭━━━╮╱╱╱╱╱╱╱╱╭╮/////////
╱╱┃╭━╮┃╭━╮┃┃╭━╮┃╱╱╱╱╱╱╱╭╯╰╮////////
╭┳┫┃╱┃┃╰━━╮┃┃╱┃┣━━┳━━┳━┻╮╭╋━━┳━┳━━╮
┣╋┫┃╱┃┣━━╮┃┃╰━╯┃╭╮┃╭╮┃━━┫┃┃╭╮┃╭┫┃━┫
┃┃┃╰━╯┃╰━╯┃┃╭━╮┃╰╯┃╰╯┣━━┃╰┫╰╯┃┃┃┃━┫
╰┻┻━━━┻━━━╯╰╯╱╰┫╭━┫╭━┻━━┻━┻━━┻╯╰━━╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃╱┃┃///////////////
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰╯╱╰╯///////////////
""")
gold = 100

print("What game or app do you want to download?")
print("""
[1] Tic Tac Toe
[2] Tetris
[3] EC Calculator (iiOS Edition)

UPCOMING:
[1] Codepro IDE
[2] Codepro Elisis IDE
[3] Codepro Elisis Extension
[4] Elisis Compress
""")

select = input(">> ")

######################################################
# Tic Tac Toe                                        #
######################################################

if select == '1':
    print("Downloading Tic Tac Toe")
    wget.download("https://github.com/iiab76/tic-tac-toe-python/archive/refs/tags/Releases.zip")
  
    # specifying the name of the zip file
    file = "tic-tac-toe-Releases.zip"
  
    # open the zip file in read mode
    with ZipFile(file, 'r') as zip: 
    # list all the contents of the zip file
        zip.printdir() 
  
        # extract all files
        print('Extracting!') 
        zip.extractall() 
        print('Done!')

######################################################
# Tetris                                             #
######################################################

if select == '2':
    print("Downloading Tetris Game")
    wget.download("https://github.com/iiab76/tetris/archive/refs/tags/versions.zip")

    # specifying the name of the zip file
    file2 = "tetris-versions.zip"
  
# open the zip file in read mode
    with ZipFile(file2, 'r') as zip: 
    # list all the contents of the zip file
        zip.printdir() 
  
    # extract all files
        print('Extracting!') 
        zip.extractall() 
        print('Done!')

######################################################
# EC Calculator (iiOS Edition)                       #
######################################################

if select == '3':
    print("Downloading EC Calculator (iiOS Edition)")
    wget.download("https://github.com/iiab76/ec-calculator-iios/archive/refs/tags/0.1.1.zip")

# specifying the name of the zip file
    file3 = "ec-calculator-iios-0.1.1.zip"
  
# open the zip file in read mode
    with ZipFile(file3, 'r') as zip: 
    # list all the contents of the zip file
        zip.printdir() 
  
    # extract all files
        print('Extracting!') 
        zip.extractall() 
        print('Done!')