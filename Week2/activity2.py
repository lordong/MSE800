class student_info():
    def get_info(self):
        self.name = input("Please enter student name: ")
        self.age = input("Please enter student age: ")
        self.student_id = input("Please enter student ID: ")
    
    def display(self):
        print(f"Student name: {self.name}, age: {self.age}, id: {self.student_id}")
        

def main():
    students = []
    for x in range(3):
        print(f"Please enterh the information of student #{x + 1}")
        student = student_info()
        student.get_info()
        students.append(student)
    
    sorted_students = sorted(students, key=lambda x: x.age)
    for student in sorted_students:
        student.display()

if __name__ == "__main__":
    main()
