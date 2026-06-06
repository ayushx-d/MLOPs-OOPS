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
                         ''')
        if user_input=='1':
            self.signup()
        elif user_input=='2':
            self.signin()
        elif user_input=='3':   
            # self.writepost()
            pass
        elif user_input=='4':
            # self.messagefriend()
            pass
        else:
            exit()
        
    def signup(self):
        email=input("Enter your email: ")
        password=input("Setup your password: ")
        self.uesrname=email
        self.password=password
        print("You have successfully signed up!!\n")
        self.menu()

    def signin(self):
        if self.uesrname=='' and self.password=='':
            print("Please signup first by pressing 1 in the main menu\n")
            self.menu()
        else:
            uname=input("Enter your email/username: ")
            pwd=input("Enter your passoword: ")
            if self.uesrname==uname and self.password==pwd:
                print("You have signed in successfully!!\n")
                self.loggedin=True
            else:
                print("Please enter correct credentials!!\n")
            self.menu()

        


obj=chatbook()
