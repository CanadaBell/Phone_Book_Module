#Imports
import os
import time
import book
#Variables
info = None #user input
#Processing
book.logo()
book.keys()
info = input("> ")
os.system('cls' if os.name =='nt' else 'clear')
print ("fetching data...")
time.sleep(3)
os.system('cls' if os.name =='nt' else 'clear')

if info in book.phonebook:
    print ("""↓ Your requested page ↓

************************************************************************************************""")
    key_list = list(book.phonebook[info].keys())
    for key in key_list:
        print(key + ":" , book.phonebook[info][key])
    print ("************************************************************************************************")
    time.sleep(7)
    os.system('cls' if os.name =='nt' else 'clear')
else:
    print("sorry wrong key")
book.outro()
