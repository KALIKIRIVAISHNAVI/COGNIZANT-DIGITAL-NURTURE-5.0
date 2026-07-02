from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, Numeric, Boolean, Time
from sqlalchemy.orm import declarative_base, relationship

# Keep your existing engine connection string here
engine = create_engine('mysql+mysqlconnector://root:725145@localhost:3306/college_db_orm', echo=True)
Base = declarative_base()

class Department(Base):
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True)
    dept_name = Column(String(100), unique=True, nullable=False)
    students = relationship('Student', back_populates='department')

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    enrollment_year = Column(Integer)
    is_active = Column(Boolean, default=True)
    department_id = Column(Integer, ForeignKey('departments.id'))
    department = relationship('Department', back_populates='students')
    enrollments = relationship('Enrollment', back_populates='student')

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    course_name = Column(String(150), nullable=False)
    enrollments = relationship('Enrollment', back_populates='course')

class Professor(Base):
    __tablename__ = 'professors'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)

class Enrollment(Base):
    __tablename__ = 'enrollments'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    course_id = Column(Integer, ForeignKey('courses.id'))
    student = relationship('Student', back_populates='enrollments')
    course = relationship('Course', back_populates='enrollments')

class CourseSchedule(Base):
    __tablename__ = 'course_schedules'
    schedule_id = Column(Integer, primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'))
    day_of_week = Column(String(20))
    start_time = Column(Time)
    end_time = Column(Time)

Base.metadata.create_all(engine)