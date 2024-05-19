from utils.user import User

class UserManager(User):
    def __init__(self):
        super().__init__('', '', 0)
        self.users = self.load_user()

    def validate_password(self):
        if len(self.password) >= 8:
            return True
        else:
            raise ValueError("Password must be at least 8 characters long")
        
    def validate_username(self):
        if len(self.username) >= 4:
            return True
        else:
            raise ValueError("Username must be at least 4 characters long")

    def login(self):
        print("Login to your account")
        username = input("Enter username: ")
        password = input("Enter password: ")
        for user in self.users:
            if user[0] == username and user[1] == password:
                print("Log in successful!")
                return User(username, password, int(user[2]))
        print("Invalid username or password")
        return None
    
    def register(self):
        print("Register an account")
        while True:
            self.username = input("Enter username: ")
            try:
                if not self.username:
                    return
                if not self.validate_username():
                    continue
                if any(username == self.username for username, _, _ in self.users):
                    print("Username already exists.")
                    continue

                self.password = input("Enter password: ")
                if not self.validate_password():
                    continue
                else:
                    self.users.append((self.username, self.password, 0))
                    self.save_users(self.users)
                    print("You have registered successfully!")
                    return
            except ValueError as e:
                print(e)
