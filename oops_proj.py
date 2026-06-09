class chatbook:
    def __init__(self):
        self.username=''
        self.password=''
        self.loggedin=False
        self.menu()

    def menu(self):
        user_input=input('''Welcome to Chatbook!! How would you like to proceed?
                         1.Press 1 to Sign Up
                         2.Press 2 to Sign In
                         3.Press 3 to write a post
                         4.Press 4 to message a friend
                         5.Press any other key to exit
                         ->''')
        if user_input=='1':
            self.signup()
        elif user_input=='2':
            self.signin()
        elif user_input=='3':   
            self.my_post()
            pass
        elif user_input=='4':
            self.sendmsg()
        else:
            exit()
        
    def signup(self):
        email=input("Enter your email: ")
        password=input("Setup your password: ")
        self.username=email
        self.password=password
        print("You have successfully signed up!!\n")
        self.menu()

    def signin(self):
        if self.username=='' and self.password=='':
            print("Please signup first by pressing 1 in the main menu\n")
            self.menu()
        else:
            uname=input("Enter your email/username: ")
            pwd=input("Enter your passoword: ")
            if self.username==uname and self.password==pwd:
                print("You have signed in successfully!!\n")
                self.loggedin=True
            else:
                print("Please enter correct credentials!!\n")
            self.menu()
    
    def my_post(self):
        if self.loggedin:
            txt=input("What's on your mind? ")
            print(f"Following content has been posted:{txt}\n", txt)
        else:
            print("Please sign in first to write a post!!\n")
        self.menu()

    def sendmsg(self):
        if self.loggedin:
            txt=input("Enter your message:")
            frnd=input("Whom to send the message?")
            print(f"Your message has been sent to {frnd}!!\n")
        else:
            print("Please sign in first!\n")
        self.menu()

        
        


user1=chatbook()
