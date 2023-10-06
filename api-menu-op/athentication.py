# Set, list, dict 

# dict format kyle : Del
# set format 'kyle'


def login (username = None, password = None):
    db = open("database.txt", "r")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if not len (username or password) < 1:
        user = [] # Stores an empty username
        passw = []
        
        for i in db:
            a, b = i.split(", ")
            b = b.strip() # The strip() method removes any leading, and trailing whitespaces. Leading means at the beginning of the string, trailing means at the end.
            user.append(a)
            passw.append(b)
            
        data = dict(zip(user, passw)) # match username and pass -> Murag zipper like joining both sides together
        
        try:
            if data[username]:
                try:
                    if password == data[username]:
                        print("Login Success: Welcome " + username)
                    else:
                        print("Username or Password is incorrect")
                except:
                    print("Username or password incorrect")
            else:
                    print("Username doesn't exist")
        except:
            print("login error")
    else:
        print("Please enter your username and password")
            
def register(username = None, password = None, confPass = None):
    db = open("database.txt", "r") # "r" -> Read file only or --> 'r'
    username = input("Create your username: ")
    password = input("Create your password: ")
    confPass = input("Confirm password: ")
    
    user = []
    passw = []
    
    for i in db:
        a, b = i.split(", ")
        b = b.strip() # The strip() method removes any leading, and trailing whitespaces. Leading means at the beginning of the string, trailing means at the end.
        user.append(a)
        passw.append(b)
    data = dict(zip(user, passw))
    
    if password != confPass:
        print("Password do not match")
        register()
    else:
        if len(password) <=6:
            print("Password must be greater than 6 characters")
            register()
        elif username in user:
            print("Username exist in database")
            register() 
        else:
            db = open("database.txt", "a") # "a" -> append to dictionary / add item to list
            db.write(username + ", " + password + "\n")
            print("Register Success")
            
def show():
    account = open("database.txt", "r") # explicit argument mode
    content = account.read()
    print(content)
    account.close()
            
def option(choice = None):
    
    print("Welcome to MyLogin Page")
    print("Press 1 -> Register")
    print("Press 2 -> Login")
    print("Press 3 -> Show accounts")
    
    choice = int(input("Choose option: "))
    
    if choice == 1:
        register()
    if choice == 2:
        login()
    if choice == 3:
        show()

option()

"""

'r'	Open for text file for reading text
'w'	Open a text file for writing text
'a'	Open a text file for appending text

"""