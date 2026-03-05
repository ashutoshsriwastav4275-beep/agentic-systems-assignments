class StudentScores:
    def __init__(self, scores):
        self.scores = scores

    def highest_last_two(self):
        try:
            if len(self.scores) < 2:
                raise Exception("List must contain at least 2 scores")

            highest = max(self.scores[-1], self.scores[-2])
            print("Highest score among last two:", highest)

        except Exception as e:
            print("Error:", e)


# Example usage
scores_list = [65, 78, 82, 90]
student = StudentScores(scores_list)
student.highest_last_two()