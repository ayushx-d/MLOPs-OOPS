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
                         5.Press any other key to exit''')
        if user_input=='1':
            # self.signup() 
            pass
        elif user_input=='2':
            # self.signin()
            pass
        elif user_input=='3':   
            # self.writepost()
            pass
        elif user_input=='4':
            # self.messagefriend()
            pass
        else:
            exit()


obj=chatbook()