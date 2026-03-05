class StudentMarks:
    def __init__(self, marks):
        self.marks = marks

    def last_three_avg(self):
        try:
            if len(self.marks) < 3:
                raise Exception("List must contain at least 3 marks")

            avg = (self.marks[-1] + self.marks[-2] + self.marks[-3]) / 3
            print("Average of last three marks:", avg)

        except Exception as e:
            print("Error:", e)


# Example usage
marks_list = [78, 85, 90, 88, 92]
student = StudentMarks(marks_list)
student.last_three_avg()