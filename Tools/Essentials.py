#The EnDa Password Checker's Essentials Module

#Import needed modules
import os
from pystyle import Colors, Colorate
import requests
import hashlib
import sys
from colorama import Fore
import time
from os.path import exists
import datetime
import random

#Define a space function
def space():
    print()

#Define a clear console function
def clearConsole():
    command = "clear"
    if os.name in ("dos","nt"):
        command = "cls"
    os.system(command)

#Define a banner
def banner(option):
    if int(option) == 1:
         print(Colorate.Horizontal(Colors.green_to_blue,R"""
  ______       _____          _____                                    _    _____ _               _             
 |  ____|     |  __ \        |  __ \                                  | |  / ____| |             | |            
 | |__   _ __ | |  | | __ _  | |__) |_ _ ___ _____      _____  _ __ __| | | |    | |__   ___  ___| | _____ _ __ 
 |  __| | '_ \| |  | |/ _` | |  ___/ _` / __/ __\ \ /\ / / _ \| '__/ _` | | |    | '_ \ / _ \/ __| |/ / _ \ '__|
 | |____| | | | |__| | (_| | | |  | (_| \__ \__ \\ V  V / (_) | | | (_| | | |____| | | |  __/ (__|   <  __/ |   
 |______|_| |_|_____/ \__,_| |_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_|  \_____|_| |_|\___|\___|_|\_\___|_|   
                                                                                                                                                                                                                                                                                                                                                                                              
        """,1))
    elif int(option) == 2:
        print(Colorate.Horizontal(Colors.green_to_blue,R"""                                                                                            
 _____     ____         _____                             _    _____ _           _           
|   __|___|    \ ___   |  _  |___ ___ ___ _ _ _ ___ ___ _| |  |     | |_ ___ ___| |_ ___ ___ 
|   __|   |  |  | .'|  |   __| .'|_ -|_ -| | | | . |  _| . |  |   --|   | -_|  _| '_| -_|  _|
|_____|_|_|____/|__,|  |__|  |__,|___|___|_____|___|_| |___|  |_____|_|_|___|___|_,_|___|_|  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
        """,1))
    elif int(option) == 3:
        print(Colorate.Horizontal(Colors.green_to_blue,R"""                                                                                            
▒█▀▀▀ █▀▀▄ ▒█▀▀▄ █▀▀█ 　 ▒█▀▀█ █▀▀█ █▀▀ █▀▀ █░░░█ █▀▀█ █▀▀█ █▀▀▄ 　 ▒█▀▀█ █░░█ █▀▀ █▀▀ █░█ █▀▀ █▀▀█ 
▒█▀▀▀ █░░█ ▒█░▒█ █▄▄█ 　 ▒█▄▄█ █▄▄█ ▀▀█ ▀▀█ █▄█▄█ █░░█ █▄▄▀ █░░█ 　 ▒█░░░ █▀▀█ █▀▀ █░░ █▀▄ █▀▀ █▄▄▀ 
▒█▄▄▄ ▀░░▀ ▒█▄▄▀ ▀░░▀ 　 ▒█░░░ ▀░░▀ ▀▀▀ ▀▀▀ ░▀░▀░ ▀▀▀▀ ▀░▀▀ ▀▀▀░ 　 ▒█▄▄█ ▀░░▀ ▀▀▀ ▀▀▀ ▀░▀ ▀▀▀ ▀░▀▀                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
        """,1))

#Define a function which error something
def error(string):
    print(Fore.RED + "[ERROR]" + Fore.WHITE + " >> " + Fore.LIGHTRED_EX + str(string) + Fore.WHITE)

#Define an options list
def options():
    print(Fore.MAGENTA + "[1]" + Fore.WHITE + " >> " + Fore.LIGHTYELLOW_EX + "Check a Password")
    print(Fore.MAGENTA + "[2]" + Fore.WHITE + " >> " + Fore.LIGHTYELLOW_EX + "Check all Passwords from a file")

#Define useful functions
def request_api_data(query_char):
    url = "https://api.pwnedpasswords.com/range/" + str(query_char)
    res = requests.get(url)
    if res.status_code != 200:
        error("The API is OFFLINE!")
        time.sleep(10)
        exit()
    return res

def get_password_leaks_count(hashes,hash_to_check):
    hashes = (line.split(":") for line in hashes.text.splitlines())
    for h , count in hashes:
        if h == hash_to_check:
            return count
    return 0

def pwned_api_check(password):
    hashed = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first5char, tail = hashed[:5],hashed[5:]
    response = request_api_data(first5char)
    return get_password_leaks_count(response,tail)

#Define a function which writes down checked passwords
def save(string):
    e = datetime.datetime.now()
    today = e.strftime("%d/%m/%Y | %I:%M %p")
    try:
        with open("Checked.txt","a") as file:
            file.write(today + " - " + string + "\n")
    except:
        print(Fore.RED + "[ERROR] >> Something went wrong in saving this verification to file!")
        space()
        time.sleep(10)
        exit()

def f(x):
    new_list = []
    for i in x:
        l = len(i)
        removed = i[:l:-2]
        new_list.append(removed)
    new_list[-1] = x[-1]
    return new_list