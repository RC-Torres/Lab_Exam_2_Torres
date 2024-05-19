import os

class User:
    def __init__(self, username, password, score):
        self.username = username
        self.password = password
        self.score = score
        self.data_folder = "data.txt"
        self.users_file = "users.txt"
        self.path = os.path.join(self.data_folder, self.users_file)

    def load_user(self):
        users = []
        if not os.path.exists(self.data_folder):
            os.makedirs(self.data_folder)

        if os.path.exists(self.path):
            try:
                with open(self.path, 'r') as file:
                    for line in file:
                        username, password, f_score = line.strip().split(', ')
                        users.append((username, password, f_score))
            except PermissionError as e:
                print(f"Permission error: {e}")
                return []
        return users

    def save_users(self, users):
        if not os.path.exists(self.data_folder):
            os.makedirs(self.data_folder)

        try:
            with open(self.path, 'w') as file:
                for username, password, f_score in users:
                    file.write(f"{username}, {password}, {f_score}\n")
        except PermissionError as e:
            print(f"Permission error: {e}")