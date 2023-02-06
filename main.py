#Imports
import os
import time
import book
#Variables
info = None #user input
logo = ("""
*****************************
|                           |
|  Epic Phonebook Programm  |
|                           |
*****************************
""")
keys = ("""Please input the key for the info of the person you are trying to access

*************************
Keys
↓
p1: Name: Thomas Kovacs
p2: "Name: Kent Summers
p3: "Name: Isaac Blakesley
p4: "Name: Lucas Arrington
p5: Name: Lucy Dixon
*************************""")
outro = ("""Thank you for using

*****************************
|                           |
|  Epic Phonebook Programm  |
|                           |
*****************************

please rate 5 ★""")
#Processing
print(logo)
print(keys)
info = input("> ")
os.system("cls")
print ("fetching data...")
time.sleep(3)
os.system("cls")

if info in book.phonebook:
    print ("""↓ Your requested page ↓

************************************************************************************************""")
    key_list = list(book.phonebook[info].keys())
    for key in key_list:
        print(key + ":" , book.phonebook[info][key])
    print ("************************************************************************************************")
    time.sleep(7)
    os.system("cls")
else:
    print("sorry wrong key")
print (outro)