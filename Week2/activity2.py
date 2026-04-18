class student_info():
    def get_info(self):
        self.name = input("Please enter student name: ")
        self.age = input("Please enter student age: ")
        self.student_id = input("Please enter student ID: ")
    
    def display(self):
        print(f"Student name: {self.name}, age: {self.age}, id: {self.student_id}")
        

def main():
    students = []
    for x in range(1, 4):
        print(f"Please enterh the information of student #{x}")
        student = student_info()
        student.get_info()
        students.append(student)
        
    for student in students:
        student.display()

if __name__ == "__main__":
    main()
