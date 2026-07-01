from sqlalchemy.orm import sessionmaker, joinedload
from models import engine, Department, Student, Course, Enrollment

"""
OBSERVATION FOR TASK 3:
Standard Query (N+1): Issues 1 query for enrollments, plus 1 query for EACH student and course lookup.
Joinedload Query: Issues exactly 1 query using SQL JOINs to fetch all related data at once.
"""

# Step 80: Open a Session
Session = sessionmaker(bind=engine)
session = Session()

# Step 81: INSERT 3 Departments and 5 Students
dept_cs = Department(dept_name='Computer Science')
dept_math = Department(dept_name='Mathematics')
dept_phy = Department(dept_name='Physics')
session.add_all([dept_cs, dept_math, dept_phy])
session.commit()

student1 = Student(name='Alice', email='alice@test.com', enrollment_year=2024, department=dept_cs)
student2 = Student(name='Bob', email='bob@test.com', enrollment_year=2024, department=dept_cs)
student3 = Student(name='Charlie', email='charlie@test.com', enrollment_year=2023, department=dept_math)
student4 = Student(name='Diana', email='diana@test.com', enrollment_year=2025, department=dept_phy)
student5 = Student(name='Eve', email='eve@test.com', enrollment_year=2024, department=dept_cs)
session.add_all([student1, student2, student3, student4, student5])
session.commit()

# Step 82: INSERT 3 Courses and 4 Enrollments
course1 = Course(course_name='Database Systems')
course2 = Course(course_name='Calculus')
course3 = Course(course_name='Quantum Mechanics')
session.add_all([course1, course2, course3])
session.commit()

enr1 = Enrollment(student=student1, course=course1)
enr2 = Enrollment(student=student2, course=course1)
enr3 = Enrollment(student=student3, course=course2)
enr4 = Enrollment(student=student4, course=course3)
session.add_all([enr1, enr2, enr3, enr4])
session.commit()

print("\n--- Data Inserted Successfully ---\n")

# Step 83: READ all students in 'Computer Science'
print("--- CS Students ---")
cs_students = session.query(Student).join(Department).filter(Department.dept_name == 'Computer Science').all()
for s in cs_students:
    print(s.name)

# Step 84: READ all enrollments (Demonstrating N+1 Query)
print("\n--- All Enrollments (N+1 Issue) ---")
all_enrollments = session.query(Enrollment).all()
for e in all_enrollments:
    print(f"{e.student.name} is enrolled in {e.course.course_name}")

# Step 85: UPDATE a student's enrollment_year
student_to_update = session.query(Student).filter(Student.email == 'alice@test.com').first()
if student_to_update:
    student_to_update.enrollment_year = 2026
    session.commit()
    print("\n--- Updated Alice's enrollment_year ---")

# Step 86: DELETE an enrollment record
enr_to_delete = session.query(Enrollment).filter(Enrollment.student_id == student2.id).first()
if enr_to_delete:
    session.delete(enr_to_delete)
    session.commit()
    print("--- Deleted Bob's enrollment ---\n")

# Task 3 (Steps 87-90): Eager Loading with joinedload
print("--- Optimized Enrollments (Fixing N+1) ---")
optimized_enrollments = session.query(Enrollment).options(
    joinedload(Enrollment.student), 
    joinedload(Enrollment.course)
).all()

for e in optimized_enrollments:
    print(f"{e.student.name} is enrolled in {e.course.course_name}")