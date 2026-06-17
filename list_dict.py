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
    
    stored_password = user_db[username][password]
    
    if writtenpassword != stored_password:
        print("password didnt match")
        return False
    print("login successful welcome @",username)
    return True

        
        