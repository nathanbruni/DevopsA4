# In order for this program to run properly, it is recommended that the program or the IDE is run in administrator mode

import ctypes

# Global Variables to hold the websites and track the current time
websites = []

# Asks the user for the websites they would like to block.
def website_ask():
    print("What website would you like to block?")
    to_block = str(input())
    # Ensures the website starts url notation
    if to_block.startswith("www.") == False:
        raise Exception("Please enter a valid website")
    # Adds website to websites list
    else:
        websites.insert(1, to_block)
        website_ask_2()

# Asks users if they would like to add another webstie or move onto the time frame    
def website_ask_2():
    flag = ""
    print("Would you like to add another website? Y/N")
    flag = str(input()).upper()
    # Returns to the website_ask function
    if flag == "Y":
        website_ask()
    # If not, move onto the website_blocker function
    elif flag == "N":
        website_blocker()
    # If error, retry the function/recursion
    else:
        print("Invalid entry")
        website_ask_2()

# Helper Function taken from the code at https://github.com/Kalebu/Website-blocker-python/blob/master/app%20v2.py
# Removed the time aspect from the original code and turned it into an option for the user to block the website or remove the website from the hosts file.
# Note, the website must be removed from the hosts file before it can be used again
# This program will only work on Windows computers
# It is advisable that the user clears their browser cache before trying to check if the website is blocked
def website_blocker():
    print("Would you like to block or unblock listed websites? (B/U)")
    answer = str(input()).upper()
    # If user wants to block the websites, it adds each website with the prefix of 127.0.0.1 to the hosts file
    if answer == "B":
        for website in websites:
            print(websites[0])
            ctypes.windll.wininet.InternetSetOptionW(0, 39, ctypes.c_void_p(0), 0)
            with open(r"C:\Windows\System32\drivers\etc\hosts", "a") as file:
                file.write(f"127.0.0.1 {website}\n")
    # If user wants to unblock, it reads the file and rewrites the file with every line that does not contain the websites specified in the websites list.
    elif answer == "U":
            with open(r"C:\Windows\System32\drivers\etc\hosts", "r+", encoding="UTF8") as file:
                lines = file.readlines()
                file.seek(0)
                for line in lines:
                    if not any(website in line for website in websites):
                        file.write(line)
                    file.truncate()
    # Any other response causes an error and restarts the function/recursion.
    else:
        print("An error has occured, please try again.")
        website_blocker()

# Runs the first function
website_ask()
