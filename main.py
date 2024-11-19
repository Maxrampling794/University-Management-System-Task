class person:
    def __init__(self,name, age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def set_details(self, new_name, new_age, new_gender):
        self.name = new_name
        self.age = new_age
        self.gender = new_gender
         

    def return_detils(self):
        print("Name: " + self.name)
        print("Age: " + self.age)
        print("Gender: " + self.gender)

class student(person):
    def __init__(self, name, age,gender, student_id, course):
        super().__init__(self,name, age,gender)
        self.student_id = student_id
        self.course = course
        self.grades = []
    
    def set_student_detials(self,new_student_id, new_course):
        self.student_id = new_student_id
        self.course = new_course
    
    def add_grade(self, new_grade):
        self.grades = new_grade
        self.grades.append(new_grade)
    
    def calculate_average_grades(self):
        if len(self.grades) == 0:
            return 0
        total = sum(self.grades)
        total = total/ len(self.grades)
        return total
    def get_student_summary(self):
        print ("name: ", self.name)
        print ("age: ", self.age)
        




