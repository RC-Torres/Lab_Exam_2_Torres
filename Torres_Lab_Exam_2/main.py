from utils.dice_game import Dicegame
from utils.user_manager import UserManager


class Main:
    def __init__(self):
        self.user_manager = UserManager()
        self.dice_game = Dicegame()

    def main(self):

        while True:
            print("1. Register")
            print("2. Login")
            print("3. Exit")

            choice = int(input("Enter your choice (1-3): "))

            try:
                if choice == 1:
                    self.user_manager.register()
                elif choice == 2:
                    logged_in_user=self.user_manager.login()
                    if logged_in_user:
                        self.dice_game.menu(logged_in_user)
                elif choice == 3:
                    exit()
                else:
                    print("Enter a valid number.")
            except ValueError as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    game = Main()
    game.main()