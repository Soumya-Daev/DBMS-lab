class Student:
    def __init__(self, roll, dept_code, name, addr, phone):
        self.roll = roll
        self.dept_code = dept_code
        self.name = name
        self.addr = addr
        self.phone = phone

class Department:
    def __init__(self, dept_code, dept_name):
        self.dept_code = dept_code
        self.dept_name = dept_name

def initialize():
    std1 = Student(10, 1, "John", "Delhi", "1234567890")
    std2 = Student(11, 2, "Jane", "Mumbai", "0987654321")
    std3 = Student(12, 3, "Jack", "Chennai", "1234567890")
    std4 = Student(13, 1, "Mike", "Bombay", "0987654321")
    std5 = Student(14, 2, "Alice", "Kolkata", "1234567890")
    std6 = Student(15, 3, "Alisa", "Assam", "0987654321")
    std7 = Student(16, 1, "Sakura", "Bihar", "1234567890")
    std8 = Student(17, 2, "Hari", "Kashmir", "0987654321")
    students = [std1, std2, std3, std4, std5, std6, std7, std8]

    dept1 = Department(1, "CSE")
    dept2 = Department(2, "ECE")
    dept3 = Department(3, "EEE")
    departments = [dept1, dept2, dept3]

    return students, departments

def add_student(std, students):
    valid = True
    for student in students:
        if std.roll == student.roll:
            valid = False
            break
    if valid:
        students.append(std)
        return True, students
    else:
        return False, students

def delete_student(roll, students):
    valid = False
    for student in students:
        if roll == student.roll:
            valid = True
            break
    if valid:
        students.remove(student)
        return True, students
    else:
        return False, students

def update_student(std, students):
    valid = False
    for student in students:
        if std.roll == student.roll:
            valid = True
            student.name = std.name
            student.addr = std.addr
            student.phone = std.phone
            break
    return valid, students

def get_student(roll, students):
    valid = False
    for student in students:
        if roll == student.roll:
            valid = True
            break
    if valid:
        return True, student
    else:
        return False, None