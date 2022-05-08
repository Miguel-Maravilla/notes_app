
import users.user as model #indicate "package" and "module"
import notes.actions 


class Actions:

    def registration(self):
        print("\nGreat! let's register in the system!!")

        name = input("What's your name? ")
        last_name = input("What's your last name? ")
        email = input("What's your email? ")
        password = input("Create a password please: ")

        user = model.User(name, last_name, email, password) # create "user object"
        registration = user.to_register() # register in db this new "user object" you've just created

        if registration[0] >= 1:  #"registration[0]" is the "cursor.rowcount" index
            print(f"\nPerfect!! {registration[1].name} you've registered with the email {registration[1].email}")
        else:
            print("\nThe registration process wasn't correct")    


    def login(self):
        print("\nPlease identify yourself on the system: ")

        try:
            email = input("What's your email? ")
            password = input("Introduce your password please: ")

            user = model.User('', '', email, password)
            login = user.to_identify()

            if email == login[3]:    #verify if email provided by user is the same of the email in db
                print(f"\nWelcome {login[1]}, you've registered in the system the {login[5]}")
                self.next_actions(login)
        
        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print(f"Incorrect login, try it later")


    def next_actions(self, user): #"self" to access to properties on the class and "user" that ios the "user object" that is idetified (after login)
        print("""
        Available actions:
            - Create notes (create)
            - Show your notes (show)
            - Delete notes (delete)
            - Exit (exit)
        """)

        action = input("What would you like to do? ").lower()
        makeThe = notes.actions.Actions()

        if action == "create":
            makeThe.create(user)
            self.next_actions(user)

        elif action == "show":
            makeThe.show(user)
            self.next_actions(user)

        elif action == "delete":
            makeThe.delete(user)
            self.next_actions(user)

        elif action == "exit":
            print(F"See you later {user[1]}!!")
            exit()                 
