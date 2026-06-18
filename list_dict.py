#step 1 :database initialization 
user_db = {}  #fast lookup of username to get name,age,password

social_graph = {} #set for follower and following count

post_db = [] #allows chronological order hence new post to append 

#functions
def signup(username,name,password,confirmpassword,DOB):
    if username in user_db:
        print("THIS USERNAME IS TAKEN")
        return False
    if password != confirmpassword:
        print("password didnt matched")

    user_db[username]={"name" : name.upper(),
                        "password": password,
                       "confirm_password":confirmpassword,
                       "DOB":DOB
                     }
    
    social_graph[username] = {
        "followers":set(),  # o(1) lookup and no duplicates like lists
        "following" : set() #new set created set()meaning 
    }
    print("sign up successful \n account created for",username)
    return True


def login(username,writtenpassword):
    
    if username not in user_db:
        print("NO ACCOUNT FOUND CREATE ONE")
        return False
    
    stored_password = user_db[username]['password']
    
    if writtenpassword != stored_password:
        print("password didnt match")
        return False
    print("login successful welcome @",username)
    return True

def main_menu():
    while True :
        a = int(input("ENTER A CHOICE\n1.sign in\n2.log in\n3.exit\n"))
        if a == 3 :
            break
        elif a == 1 :
            # sign in
            username = input("Enter username ")
            name =input("enter name ")
            dob = input("date of birth ")
            password = input("Enter password ")
            confirm_password =input("confirm password ")
            signup(username,name,password,confirm_password,dob)

        elif a  == 2 :
            username = input("Enter username ")
            writtenpassword =input("password ")
            login(username,writtenpassword)


        else:
            print("enter a valid num")
        