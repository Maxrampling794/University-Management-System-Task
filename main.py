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
        print ("gender: ", self.gender)
        print ("student_id: ", self.student_id)
        print ("average grades: ", self.total)

class professor(person):
    def __init__(self, name, age, gender, staff_id, department, salary):
        super().__init__(self,  name, age, gender)
        self.staff_id = staff_id
        self.department = department
        self.salary = salary
    
    def set_professors_detials(self, new_staff_id, new_department, new_salary):
        self.new_staff_id = new_staff_id
        self.new_department = new_department
        self.new_salary = new_salary
    
    def give_feedback(self, student, feedback):
        self.feedback = feedback
        print ("feedback for: ",student(self.name), ": ", self.feedback)
    
    def increase_salary(self, percentage):
        self.paercentage = percentage
        self.percentage = 1.02
        self.salary = self.salary * self.percentage
    def get_professor_summary(self):
        print ("name: ",self.name)
        print ("age: ", self.age)
        print ("gender: ", self.gender) 
        print ("staff id: ", self.staff_id)
        print ("department: ", self.department)
        print ("salary: ", self.salary)

class administor(person):
    def __init__(self,name, age,gender, admin_id, office, years_of_service):
        super().__init__(self,name, age,gender)
        self.admin_id = admin_id
        self.office = office
        self.years_of_service = years_of_service
    
    def set_admin_details(self, new_admin_id, new_office, new_years_of_service):
        self.new_admin_id = new_admin_id
        self.new_office = new_office
        self.new_years_of_service = new_years_of_service

    def increment_serive_years(self):
        self.years_of_service += 1
    
    def get_admin_summary(self):
        print ("name: ",self.name)
        print ("age: ", self.age)
        print ("gender: ", self.gender) 
        print ("admin id: ", self.admin_id)
        print ("office: ", self.office)
        print ("years_of_service: ", self.years_of_serive)

student1 =student("max",17,"male","1E32Y", "computer science")

student2 = student("david", 16, "male", "GHJ78", "computer science")

professor1 = professor("dr mahdi", 27, "male", "432FL", "computer science", 50,000)

professor2 = professor("mr stoker", 25, "male", "432FP", "maths ", 49,999)

administator = administor("mr hatchet", 45, "male", "DFG54","U01", 12)

add_grade()






       


    






