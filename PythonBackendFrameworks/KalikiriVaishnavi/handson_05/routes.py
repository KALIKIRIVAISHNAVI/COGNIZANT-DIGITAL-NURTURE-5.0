from flask import Blueprint, jsonify, request
from app import db
from HO5app.models import Course, Student, Enrollment, Department

# Define the Blueprint routing with your /api/courses prefix
courses_bp = Blueprint('courses', __name__, url_prefix='/api/courses')

def make_response_json(data, status_code):
    envelope = {
        'status': 'success' if status_code < 400 else 'error',
        'data': data
    }
    return jsonify(envelope), status_code

# 52. GET all courses from the DB
@courses_bp.route('/', methods=['GET'])
def get_courses():
    courses = Course.query.all()
    return jsonify([course.to_dict() for course in courses])

# 54. POST a new course to the DB
@courses_bp.route('/', methods=['POST'])
def create_course():
    req_data = request.get_json()
    if not req_data:
        return make_response_json({'message': 'Invalid JSON format.'}, 400)
        
    required_fields = ['name', 'code', 'credits', 'department_id']
    missing_fields = [f for f in required_fields if f not in req_data]
    if missing_fields:
        return make_response_json({'message': f'Missing fields: {", ".join(missing_fields)}'}, 400)
    
    new_course = Course(
        name=req_data['name'],
        code=req_data['code'],
        credits=req_data['credits'],
        department_id=req_data['department_id']
    )
    
    db.session.add(new_course)
    db.session.commit()  # Save to courses.db file
    
    return make_response_json(new_course.to_dict(), 201)

# 55. GET, PUT, and DELETE handlers by ID using get_or_404
@courses_bp.route('/<int:course_id>', methods=['GET'])
def get_course(course_id):
    course = Course.query.get_or_404(course_id)
    return make_response_json(course.to_dict(), 200)

@courses_bp.route('/<int:course_id>', methods=['PUT'])
def update_course(course_id):
    course = Course.query.get_or_404(course_id)
    req_data = request.get_json()
    
    if req_data:
        course.name = req_data.get('name', course.name)
        course.code = req_data.get('code', course.code)
        course.credits = req_data.get('credits', course.credits)
        course.department_id = req_data.get('department_id', course.department_id)
        db.session.commit()
        
    return make_response_json(course.to_dict(), 200)

@courses_bp.route('/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    course = Course.query.get_or_404(course_id)
    db.session.delete(course)
    db.session.commit()
    return make_response_json({'message': f'Course {course_id} successfully deleted.'}, 200)

# 56. JOIN query route fetching students linked to specific courses
@courses_bp.route('/<int:course_id>/students', methods=['GET'])
def get_course_students(course_id):
    Course.query.get_or_404(course_id)  # Returns 404 if the course doesn't exist
    
    enrolled_students = db.session.query(Student).\
        join(Enrollment, Student.id == Enrollment.student_id).\
        filter(Enrollment.course_id == course_id).all()
        
    return jsonify([student.to_dict() for student in enrolled_students])