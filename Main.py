import imaplib, sys, os
import re

try:
    username = str(sys.argv[1])
    password = str(sys.argv[2])
    emailJ = str(sys.argv[3])
    passwordJ = str(sys.argv[4])
except:
    print("Please provide <gmail username> <password> arguments!")
    quit()

file = open("crs_ids.txt")

while 1:
    line = file.readline()
    if not line:
        break
    pass    
    
    os.system("send_email.py "+emailJ+" "+passwordJ)

#note that username and password arent used but are still read in for future needs
#ie logging into hall and booking meals - for the same reason i have archived logIn.pl
#ready for refactoring when we want to actually use a loggin in function - we dont actually
#need it for reading the caius menu atm as you dont have to log in to access that page
