phonebook = { #Main dictionary
    "p1": { #Sub dictionary 
        "Name": "Thomas Kovacs",       # \
        "Phone": "(587)-501-0314",     #  > Parts of Phonebook
        "Address": "14616 31 Street",  # /
        },
    "p2": {
        "Name": "Kent Summers",
        "Phone": "(776)-133-4458",
        "Address": "59140 66 Street",
        },
    "p3": {
        "Name": "Isaac Blakesley",
        "Phone": "(930)-509-5270",
        "Address": "76603 Fort Road",
        },
    "p4": {
        "Name": "Lucas Arrington",
        "Phone": "(292)-278-2079",
        "Address": "56771 144 Ave",
        },
    "p5": {
        "Name": "Lucy Dixon",
        "Phone": "(161)-260-0491",
        "Address": "7515 118 Ave",
        },
}
#functions
def logo():
    print("""
*****************************
|                           |
|  Epic Phonebook Programm  |
|                           |
*****************************
""")

def keys(): 
    print("""Please input the key for the info of the person you are trying to access

*************************
Keys
↓
p1: Name: Thomas Kovacs
p2: Name: Kent Summers
p3: Name: Isaac Blakesley
p4: Name: Lucas Arrington
p5: Name: Lucy Dixon
*************************""")

def outro(): 
    print("""Thank you for using

*****************************
|                           |
|  Epic Phonebook Programm  |
|                           |
*****************************

please rate 5 ★""")
