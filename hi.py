class Student:
    def __init__(self, name, id, grades):
        self.name = name
        self.id = id
        self.__grades = grades 

    def get_grades(self):
        return self.__grades

    def add_grades(self, grade):
        self.__grades.append(grade)

    def calculate_average(self):
        return sum(self.__grades) / len(self.__grades)

    def calculate_grade(self):
        if self.calculate_average() >= 50:
            return "Pass"
        else:
            return "Fail"

    def display_info(self):
        print("Name:", self.name)
        print("ID:", self.id)
        print("Grades:", self.get_grades())
        print("Average:", self.calculate_average())
        print("Grade:", self.calculate_grade())