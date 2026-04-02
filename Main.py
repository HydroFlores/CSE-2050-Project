import csv

class Course:
    """Designed By Cristopher Hernandez"""
    def __init__(self, course_code, credits, students):
        self.course_code = course_code
        """unique identifer for the course, str"""
        self.credits = int(credits)
        """Credits earned, int"""
        self.students = students
        """Takes an object of the student class"""
    
    def add_student(self, student):
        """Designed By Cristopher Hernandez"""
        """adds a student object to roster"""
        if student in self.students:
            return
        else:
            self.students.append(student)
            return self.students
    
    def get_student_count(self):
        """Designed By Cristopher Hernandez"""
        """returns type: int of roster count"""
        return len(self.students)
    
class Student():
    """Designed by William Godfrey"""
    
    grade_points = {
            'A' : 4.0, 'A-' : 3.7,
            'B+': 3.3, 'B' : 3.0, 'B-' : 2.7,
            'C+': 2.3, 'C' : 2.0, 'C-' : 1.7,
            'D' : 1.0,
            'F' : 0.0
        }

    def __init__(self, student_id, name, courses):
        """Designed by William Godfrey"""
        self.student_id = student_id
        """str"""
        self.name = name
        """str"""
        self.courses = courses
        """
        (dict)
        Course object : grade
        where grade is a letter grade
        such as "A", "B+", etc.
        """

    def enroll(self, course, grade):
        """Designed by William Godfrey"""
        """
        Enrolls the student in a course with the given 
        grade and UPDATES THE COURSE ROSTER.
        """
        self.courses[course] = grade
        Course.add_student()
        return
    
    def update_grade(self, course, grade):
        """Designed by William Godfrey"""
        """
        modify the student grade 
        for a particular course
        """
        self.courses[course] = grade
        return
    
    def calculate_gpa(self):
        """Designed by William Godfrey"""
        """Computes GPA weighted by course credits."""
        """
        computes and returns the GPA 
        using all graded courses and their credits
        """
        
        grade_point_sum = 0
        credit_sum = 0
        for course, grade in self.courses.items():
            grade_val = self.grade_points.get(grade)
            grade_point_sum += (grade_val * course.credits)
            credit_sum += course.credits
        grade_point_average = grade_point_sum / credit_sum
        return grade_point_average
        """
        Use the following letter-grade to grade-point mapping when computing GPA:
        GRADE_POINTS = {
            'A' : 4.0, 'A-' : 3.7,
            'B+': 3.3, 'B' : 3.0, 'B-' : 2.7,
            'C+': 2.3, 'C' : 2.0, 'C-' : 1.7,
            'D' : 1.0,
            'F' : 0.0
        }

        GPA must be weighted by course credits:
        GPA =
        Sum of [ (grade points * credits) ]
        /
        Sum of [ credits ]
        """
    
    def get_courses(self):
        """Designed by William Godfrey"""
        """
        returns a list of course 
        objects taken by the student.
        """
        return [course.course_code for course in self.courses.keys()]
    
    def get_course_info(self):
        """Designed by William Godfrey"""
        """
        returns a structured summary 
        of all enrollments, including 
        course code, grade,
        and credits.
        """
        summary = []
        for course, grade in self.courses.items():
            summary.append({
                "Course_code": course.course_code,
                "grade": grade,
                "credits": course.credits
            })
        return summary
    
class University:
    """Designed by William Godfrey"""

    """
    Design note: 
    The dictionaries in University 
    are meant to make lookup fast and simple. 
    
    Use them to avoid repeatedly scanning
    lists to find a student or course.
    """

    def __init__(self, students, courses):
        """Designed by William Godfrey"""
        """
        Required Fields 
        • students (dictionary) — maps student_id → Student object
        • courses (dictionary) — maps course_code → Course object.
        """
        self.students = {}
        self.courses = {}

    def add_course(self, course_code, credits):
        """Designed by William Godfrey"""
        """
        if the course does not exist, 
        create and store it; 
        return the course object
        """
        if course_code not in self.courses:
            new_course = Course(course_code, credits, [])
            self.courses[course_code] = new_course
        return self.courses[new_course]
    
    def add_student(self, student_id, name):
        """Designed by William Godfrey"""
        """
        if the student does not exist, 
        create and store them; 
        return the student object
        """
        if student_id not in self.students:
            new_student = Student(student_id, name, [])
            self.students[student_id] = new_student
        return self.students[new_student]
    
    def get_student(self, student_id):
        """Designed by William Godfrey"""
        """
        returns the student object 
        for that ID (or None if not found).
        """
        if student_id in self.students.keys():
            return self.students[student_id]
        else:
            return "None"
        return self.students.get(student_id)

    def get_course(self, course_code):
        """Designed by William Godfrey"""
        """
        returns the course object 
        for that code (or None if not found).
        """
        if course_code in self.courses.keys():
            return self.courses[course_code]
        else:
            return "None"
        return self.students.get(self.student_id)
    
    def get_course_enrollment(self, course_code):
        """Designed by William Godfrey"""
        """
        returns the number of students 
        enrolled in the given course.
        """
        course = self.get_course(course_code)
        return course.get_student_count() if course else 0
    
    def get_students_in_course(self, course_code):
        """Designed by William Godfrey"""
        """
        returns a list of student 
        objects enrolled in the given course
        """
        course = self.get_course(course_code)
        return course.students if course else []
    
def load_from_csv(university, course_file, student_file):
    """Designed by William Godfrey"""
    with open(course_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            university.add_course(row['course_code'], row['credits'])

    with open(student_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            student = university.add_student(row['student_id'], row['name'])
            enrollments = row['courses'].split(';')
            for item in enrollments:
                if ':' in item:
                    code, grade = item.split(':')
                    course = university.get_course(code)
                    if course:
                        student.enroll(course, grade)
    
