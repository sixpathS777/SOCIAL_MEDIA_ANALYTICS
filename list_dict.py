import datetime
#step 1 :database initialization 
user_db = {}  #fast lookup of username to get name,age,password

social_graph = {} #set for follower and following count

post_db = [] #allows chronological order hence new post to append 

message_db = []

notification_db = {}

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
    notification_db[username] = []
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
        "likes": set(), # to avoid duplicate likes
        'comments':[]
    }
    post_db.append(post_dict)
    print("succesfully [posted]")
    return

def send(username1,username2):
    if username1 not in user_db or username2 not in user_db:
        return "messaging not possible"
    content = input("enter content ")
    if content.strip() == "":
        print("cannot send empty messages")
        return
    mess_dict ={
      'content':content,
      'timestamp' : datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
      'sender' : username1,
      'receiver' : username2
    }
    message_db.append(mess_dict)
    print("msg_send")

    notification_db[username2].append(f" messages from {username1}")
    return
def view_notification(username):
    if username in user_db:
        if len(notification_db[username])>0:
            print(notification_db[username])
            return
        else:
            print("no notifications")
            return
    else:
        print("no such user")
        return

def clear_notifications(username):

    if username not in user_db:
        print("No such user")
        return

    if len(notification_db[username]) == 0:
        print("No notifications to clear")
        return

    notification_db[username] = []

    print("All notifications cleared successfully")

    




def view_chat(user1, user2):
    found = False

    for msgs in message_db:
        if ((msgs['sender'] == user1 and msgs['receiver'] == user2) or
            (msgs['sender'] == user2 and msgs['receiver'] == user1)):

            print(f"[{msgs['timestamp']}] @{msgs['sender']}: {msgs['content']}")
            found = True

    if not found:
        print("No chat history found")



def delete_post(username,postid):
  for posts in post_db:
     if posts['postid'] == postid:
      if username != posts['author']:
        print("you can only delete your own post")
        return
      content = posts['content']
      post_db.remove(posts)
      print(f"{content} deleted")
      return 
  print("no such posts")
  return

def viewuser_posts(username):
    found = False

    for posts in post_db:
        if username == posts['author']:
            print("-" * 30)
            print(f"Post ID : {posts['postid']}")
            print(f"Content : {posts['content']}")
            print(f"Posted on : {posts['timestamp']}")
            print(f"Likes : {len(posts['likes'])}")
            print("-" * 30)

            found = True

    if not found:
        print(f"@{username} has not posted anything yet.")

def add_comments(postid,username,content):
    for posts in post_db:
        if postid == posts['postid']:
            comment_dict ={
                "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "username" : username,
                "content" : content
            }
            posts['comments'].append(comment_dict)
            print("comment added")
            username1 = posts['author']
            if username1!=username:
                notification_db[username1].append(f"{username} added a comment on {postid} do check it out")
            return
    print("no such posts")

def delete_comment(postid,username,content):
    for posts in post_db:
        if postid == posts['postid']:
            for comments in posts['comments']:
                if (comments['username'] == username and comments['content'] == content):
                    posts['comments'].remove(comments)
                    print("comment deleted successfully")
                    return 
            print("no such comments")
            return
    print("no such posts")

def view_comments(postid):
    for posts in post_db:
        if postid == posts['postid']:
            for comments in posts['comments']:
                print(comments)
            return
        print("no comments")
        return
    print("no post like that gang")

def user_profile(username):

    if username not in user_db:
        print("No such user")
        return

    print("@" * 15)
    print(f"Username : {username}")
    print(f"DOB : {user_db[username]['DOB']}")
    print(f"FOLLOWING : {len(social_graph[username]['following'])}")
    print(f"FOLLOWERS : {len(social_graph[username]['followers'])}")

    total_post = 0

    for posts in post_db:
        if username == posts['author']:
            total_post += 1

    print(f"TOTAL POSTS : {total_post}")

def edit_post(username,postid):
  for posts in post_db:
    if posts['postid']==postid:
      if username != posts['author']:
        print("you cannot edit")
        return
      old_content = posts['content']
      new_content = input("what to edit ")
      posts['content']=new_content
      print(f"{old_content} success changed to [[[[{new_content}]]]]")
      return 
  print("no such posts")
  return
    
def search(search_letter):
    found = False
    for username in user_db:
        if username.startswith(search_letter) :  # if search_letter in username
            print(username)
            found = True
    if found == False:
        print(f"no such user {search_letter}")
    

def view_feed(username):
    #shows latest content of following to the user 
    my_following = social_graph[username]['following']
    feed_count = 0
    for post in reversed(post_db):
        if post['author'] in my_following or post['author'] == username:
            print(f"\n {post['author']},{post['timestamp']}")
            print(f"{post['content']}")
            print(f"❤️ {post['likes']} likes")
            print('*'*25)
            feed_count+=1

    if feed_count == 0 :
        print("Your feed is empty\npost or follow others to view their feed ")

def follow(current_user,follow_name):
    if follow_name not in user_db:
        print("no such user exists")
        return 
    if follow_name == current_user:
        print("you cannot follow yourself")
        return
    if follow_name  in social_graph[current_user]['following']:
        print(f"already following {follow_name}")
        return
    social_graph[current_user]['following'].add(follow_name)
    social_graph[follow_name]['followers'].add(current_user)
    print(f"{current_user} now follows @{follow_name}")
    notification_db[follow_name].append(f"{follow_name} started following you ")

def unfollow(current_user,unfollow_name):
    if unfollow_name not in user_db:
        print("no such user exists")
        return 
    if unfollow_name == current_user:
        print("you cannot unfollow yourself")
        return
    if unfollow_name  not in social_graph[current_user]['following']:
        print(f"you didnt even followed @ {unfollow_name}")
        return
    
    social_graph[current_user]['following'].remove(unfollow_name)
    social_graph[unfollow_name]['followers'].remove(current_user)
    print(f"{current_user} now unfollows @{unfollow_name}")

#---#-------#------------#--------------#-------------------------#---------------
def likes_post(current_user,posts_id):
    for posts in post_db:
        if posts_id == posts["postid"]:
            if current_user not in posts['likes']:
                posts['likes'].add(current_user)
                print(f"you liked the posts {posts['postid']}")
                print(f"current likes {len(posts['likes'])}")
                username = posts['author']
                notification_db[username].append(f"{current_user} liked your post {posts_id}")
                return 
            else:
                print("already liked it")
                return
    
    print("no such posts")

def unlike_post(current_user,posts_id):
    for posts in post_db:
        if posts_id == posts["postid"]:
            if current_user in posts['likes']:
                posts['likes'].remove(current_user)
                print(f"removing like from {posts['postid']}")
                print(f"current likes {len(posts['likes'])}")
                return 
            else:
                print("you never liked it ")
                return
    
    print("no such posts")
#------------#------------------#-----------------------------#------------------------------


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

#main_menu()

#checking signup
signup("mage", "John", "1234", "1234", "01-01-2000")
#print(user_db)
#print(social_graph)

#chcking login
print(login("mage", "1234"))    # True
print(login("mage", "wrong"))   # False
print(login("unknown", "123"))  # False

#checking post
create_post("mage", "Hello world!")
create_post("mage", "My second post")

print(post_db)

view_feed('mage')

def add_users():                                   #10 users with different names, passwords, DOBs, and one post each.

    signup("alex01", "Alex", "alex123", "alex123", "12-03-1998")
    create_post("alex01", "Just finished learning Python dictionaries!")

    signup("emma02", "Emma", "emma456", "emma456", "25-07-1999")
    create_post("emma02", "Good morning everyone ☀️")

    signup("liam03", "Liam", "liam789", "liam789", "08-11-2000")
    create_post("liam03", "Workout completed 💪")

    signup("olivia04", "Olivia", "olivia321", "olivia321", "15-01-1997")
    create_post("olivia04", "Reading a new book on AI.")

    signup("noah05", "Noah", "noah654", "noah654", "30-09-2001")
    create_post("noah05", "Anyone watching the match tonight?")

    signup("ava06", "Ava", "ava987", "ava987", "22-05-1998")
    create_post("ava06", "Coffee + Coding = Perfect day ☕")

    signup("ethan07", "Ethan", "ethan111", "ethan111", "18-12-1996")
    create_post("ethan07", "Started learning Data Structures today.")

    signup("mia08", "Mia", "mia222", "mia222", "05-04-2002")
    create_post("mia08", "Beautiful weather outside!")

    signup("james09", "James", "james333", "james333", "14-08-1995")
    create_post("james09", "Debugging code for 2 hours 😭")

    signup("sophia10", "Sophia", "sophia444", "sophia444", "27-10-2000")
    create_post("sophia10", "Consistency beats motivation.")

    print("\n10 users and their posts have been added.")

add_users()
'''
follow('mia08','james09')
print(social_graph['mia08']['following'])
print(social_graph['james09']['followers'])
unfollow('mia08','james09')
print(social_graph["mia08"]['following'])
print(post_db)
likes_post("james09",7)
likes_post('ethan07',7)
likes_post('ethan07',7)
unlike_post('ethan07',7)'''
add_comments(1,'james09','sikee')
add_comments(1,'mia08','superb')
view_comments(1)
'''
user_profile('noah05')
search('a')
delete_post('ava06',9)
print(post_db[7])
viewuser_posts('mia08')
likes_post('ethan07',10)
viewuser_posts('mia08')

edit_post('mia08',10)
send("ava06",'mia08')
send('mia08','ava06')
view_chat("mia08","ava06")'''