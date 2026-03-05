class StudentPerformance:
    def __init__(self, scores):
        self.scores = scores

    def score_difference(self):
        try:
            if len(self.scores) == 0:
                raise Exception("Score list is empty")

            difference = self.scores[-1] - self.scores[0]
            print("Difference between last and first score:", difference)

        except Exception as e:
            print("Error:", e)


# Example usage
scores_list = [70, 82, 88, 95]
student = StudentPerformance(scores_list)
student.score_difference()