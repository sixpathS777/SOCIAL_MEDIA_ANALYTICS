import datetime
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

def create_post(username,content):
    
   
    post_id = len(post_db)+1
    
    post_dict = {
        "postid" : post_id,
        'author' : username,
        'content': content,
        'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "likes": 0
    }
    post_db.append(post_dict)
    print("succesfully [posted]")
    return True

def view_feed(username):
    #shows latest content of following to the user 
    my_following = social_graph[username]['following']
    feed_count = 0
    for posts in reversed(post_db):
        if post['author'] in my_following or post['author'] == username:
            print(f"\n {post['author']},{post[timestamp]}")
            print(f"{post[content]}")
            print(f"❤️ {post['likes']} likes")
            print('*'*25)
            feed_count+=1

    if feed_count == 0 :
        print("Your feed is empty\npost or follow others to view their feed ")




def dashboard(username):
    while True:
        print(f"welcome @{username}\n---------------------------")
        try:
            a = int(input("1.POST\n2.PEOPLES\n3.logout"))
        except ValueError:
            print("TYPE NUMBERS")
            continue

        if a == 1 :
            print("\n--- [POST MENU] ---")
            print("1. Create New Post")
            print("2. View News Feed")
            try :
                user_choice =int(input("enter the choice"))
            except ValueError :
                print('seriously brotato...')
                continue
            if user_choice == 1:
                content = input("whats on your mind | ")
                create_post(username,content)
            else :
                view_feed(username)

        elif a == 2:
            print("\n-] ---")
            print("1. Following ")
            print("2. Followers")
            user_choice = int(input(1 or 2 ))
            if user_choice == 1:
                following_set = social_graph[username]['following']
                    
                if not following_set:
                    print("this guy too nonchallant ")
                else:
                    print(f"@{username}",end="")
                    for users in following_set:
                        print(f"-->{users},",end =" ")
                    
            else :
                follower_set = social_graph[username]['followers']
                    
                if not follower_set :
                    print("NONE TO FOLLOW AND NONE TO VALIDATE")
                else:
                    print(f"@{username}",end = "")
                    for users in following_set:
                        print(f"-->{users}",end=" ")
        elif a== 3 :
            print("logging out")
            break
        else:
            print("enter from 1 to 3 ")
                




def main_menu():
    print("*-*"*20)
    while True :
        try :
            a = int(input("ENTER A CHOICE\n1.SIGNIN\n2.LOGIN\n3.EXIT\n"))
            print("*-*"*30)
        except ValueError :
            print("enter within the given constraint")
                  
        if a == 3 :
            print("Exiting now")
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
            if login(username,writtenpassword):
                dashboard(username)

            
        else:
            print("❌ Enter a valid number (1-3).")

main_menu()

        