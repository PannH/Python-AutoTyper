from os import system as cmd
from time import sleep
from pyautogui import *

def print_banner():
    banner = r"""  /$$$$$$              /$$            /$$$$$$$$                                     
 /$$__  $$            | $$           |__  $$__/                                     
| $$  \ $$ /$$   /$$ /$$$$$$    /$$$$$$ | $$ /$$   /$$  /$$$$$$   /$$$$$$   /$$$$$$ 
| $$$$$$$$| $$  | $$|_  $$_/   /$$__  $$| $$| $$  | $$ /$$__  $$ /$$__  $$ /$$__  $$
| $$__  $$| $$  | $$  | $$    | $$  \ $$| $$| $$  | $$| $$  \ $$| $$$$$$$$| $$  \__/
| $$  | $$| $$  | $$  | $$ /$$| $$  | $$| $$| $$  | $$| $$  | $$| $$_____/| $$      
| $$  | $$|  $$$$$$/  |  $$$$/|  $$$$$$/| $$|  $$$$$$$| $$$$$$$/|  $$$$$$$| $$      
|__/  |__/ \______/    \___/   \______/ |__/ \____  $$| $$____/  \_______/|__/      
                                             /$$  | $$| $$                          
                                            |  $$$$$$/| $$                          
                                             \______/ |__/                          """
    print(banner)
    print()

def type_text():
    cmd("cls")
    print_banner()
    text_file = open("text.txt", "r")
    text_lines = text_file.readlines()
    for line in text_lines:
        sleep(interval)
        typewrite(line)
        press("enter")

    program_end()

def timer():
    number_zero = r"""  /$$$$$$                               
 /$$$_  $$                              
| $$$$\ $$                              
| $$ $$ $$                              
| $$\ $$$$                              
| $$ \ $$$                              
|  $$$$$$/       /$$       /$$       /$$
 \______/       |__/      |__/      |__/"""
    number_one = r"""   /$$                                
 /$$$$                                
|_  $$                                
  | $$                                
  | $$                                
  | $$                                
 /$$$$$$       /$$       /$$       /$$
|______/      |__/      |__/      |__/"""
    number_two = r"""  /$$$$$$                               
 /$$__  $$                              
|__/  \ $$                              
  /$$$$$$/                              
 /$$____/                               
| $$                                    
| $$$$$$$$       /$$       /$$       /$$
|________/      |__/      |__/      |__/"""
    number_three = r"""  /$$$$$$                               
 /$$__  $$                              
|__/  \ $$                              
   /$$$$$/                              
  |___  $$                              
 /$$  \ $$                              
|  $$$$$$/       /$$       /$$       /$$
 \______/       |__/      |__/      |__/"""
    number_four = r""" /$$   /$$                              
| $$  | $$                              
| $$  | $$                              
| $$$$$$$$                              
|_____  $$                              
      | $$                              
      | $$       /$$       /$$       /$$
      |__/      |__/      |__/      |__/"""
    number_five = r""" /$$$$$$$                               
| $$____/                               
| $$                                    
| $$$$$$$                               
|_____  $$                              
 /$$  \ $$                              
|  $$$$$$/       /$$       /$$       /$$
 \______/       |__/      |__/      |__/"""
    cmd("cls")
    print_banner()
    print(number_five)
    sleep(1)
    cmd("cls")
    print_banner()
    print(number_four)
    sleep(1)
    cmd("cls")
    print_banner()
    print(number_three)
    sleep(1)
    cmd("cls")
    print_banner()
    print(number_two)
    sleep(1)
    cmd("cls")
    print_banner()
    print(number_one)
    sleep(1)
    cmd("cls")
    print_banner()
    print(number_zero)
    sleep(1)
    type_text()

def start_program():
    cmd("cls")
    print_banner()
    print("Once the program launched,")
    print("click in the text area where the message should be sent.")
    print("You have 5 seconds to click in the text area.")
    print("Once ready, press 'ENTER' and the timer will start.")
    input("| ")
    timer()

def select_interval():
    cmd("cls")
    print_banner()
    print("Now, select an interval between each message (e.g. 0.5).")
    while True:
        try:
            selected_interval = float(input("Interval (in seconds) > "))
            selected_interval = round(selected_interval, 1)
            break
        except ValueError:
            cmd("cls")
            cmd("color 4")
            print_banner()
            print("ERROR: The value you entered is not a number!")
            print("Try again...")
            print()

    cmd("color 9")
    return selected_interval

def program_end():
    cmd("cls")
    print_banner()
    print("Program finished!")
    print("Press 'ENTER' to close it...")
    input("| ")
    exit()

cmd("color 9")
print_banner()
print("Welcome to AutoTyper!")
print("This program will send a text divided into several messages to your friend :D")
print("The text that will be sent must be in the file text.txt")
print("One line = One message")
print()
response = str(input("Ready? (yes/no) > "))

response = response.lower()
if not response or response != "yes" and response != "no":
    program_end()
else:
    try:
        open("text.txt", "r")
    except FileNotFoundError:
        open("text.txt", "x")

    file = open("text.txt", "r")
    lines = file.readlines()
    if response == "no":
        program_end()
    elif response == "yes":
        if not lines or lines[0] == "\n":
            cmd("cls")
            cmd("color 4")
            print_banner()
            print("ERROR: The file text.txt or its first line is empty!")
            print("Please, correct this and restart the program.")
            print()
            print("Press 'ENTER' to close the program...")
            input("| ")
            exit()
        else:
            interval = select_interval()
            print(f"Interval: {interval}s")
            start_program()