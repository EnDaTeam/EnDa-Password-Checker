#The EnDa Password Checker's source code

#Import the custom module
from Tools.Essentials import *

#Random value
value = random.randint(1,3)

#Create a start-up
clearConsole()
space()
banner(value)
print(Fore.CYAN + "Welcome to EnDa Password Checker!")
countes = True
countes1 = True
while countes:
    while countes1:
        space()
        print(Fore.LIGHTYELLOW_EX + "Please Select an option form the list!")
        space()
        options()
        space()
        option = input(Fore.WHITE + "Option : ")
        space()
        try:
            int(option)
        except:
            error("The inputed option does not exist!")
        else:
            countes1 = False
    if int(option) == 1:
        print(Fore.BLUE + "Please enter your Password!" + Fore.WHITE)
        password = input("Password : ")
        space()
        if password == "" or password[1] == " ":
            error("Sorry, something went wrong about the input!")
            time.sleep(10)
            exit()
        count = pwned_api_check(password)
        if count:
            print(Fore.LIGHTRED_EX + f"{password} was found {count} times on our Database!")
            print(Fore.LIGHTYELLOW_EX + "[TIP]" + Fore.WHITE + " >> " + Fore.LIGHTYELLOW_EX + "You should change it!")
            save(f"{password} was found {count} times on our Database!")
        else:
            print(Fore.GREEN + f"{password} is a very strong password!")
            save(f"{password} is a very strong password!")
    elif int(option) == 2:
        print(Fore.BLUE + "Please enter the file name with your passwords!" + Fore.WHITE)
        password_list = input("File : ")
        file_exists = exists(password_list )
        if file_exists:
            file = open(password_list, "r")
            new_list = []
            for line in file.read().split("\n")[::2]:
                new_list.append(line)
        else:
            space()
            error("Something went wrong about opening the file!")
            time.sleep(10)
            exit()
        for i in f(new_list):
            if i == "" or i[1] == " ":
                error("Sorry, something went wrong about the input!")
                time.sleep(10)
                exit()
            counti = pwned_api_check(i)
            if counti:
                print(Fore.LIGHTRED_EX + f"{i} was found {counti} times on our Database!")
                print(Fore.LIGHTYELLOW_EX + "[TIP]" + Fore.WHITE + " >> " + Fore.LIGHTYELLOW_EX + "You should change it!")
                save(f"{i} was found {counti} times on our Database!")
            else:
                print(Fore.GREEN + f"{i} is a very strong password!")
                save(f"{i} is a very strong password!")
            time.sleep(1.5)
        

    space()
    print(Fore.RED + "Do you want to do another verification?" + Fore.LIGHTRED_EX)
    calculation = input("(Y)es or (N)o : ")
    space()
    if str(calculation).lower() in ("y","yes","(y)es","(y)"):
        countes = True
        countes1 = True
    else:
        print(Fore.BLUE + "Roger, thank you for using EnDa Password Checker!" + Fore.RESET)
        time.sleep(2)
        exit()