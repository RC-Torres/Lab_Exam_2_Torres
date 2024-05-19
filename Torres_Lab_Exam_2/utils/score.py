import os

class Score:
    def __init__(self):
        self.data_files = 'data'
        self.scores_file = 'scores.txt'
        self.path = os.path.join(self.data_files, self.scores_file)

    def load_scores(self):
        scores = []
        
        if os.path.exists(self.path):
            with open(self.path, 'r') as file:
                for line in file:
                    scores.append(line.strip().split(', '))
            return scores
        else:
            print("No scores recorded yet.")
            return None

    def save_scores(self, username, f_score, f_wins, date):
        try:
            with open(self.path, 'w') as file:
                file.write(f"{username}, {f_score}, {f_wins}, {date}\n")
        except PermissionError as e:
            print(f"Permission error: {e}")