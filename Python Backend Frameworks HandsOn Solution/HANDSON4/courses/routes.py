from flask import Blueprint, jsonify, request

# Create Blueprint with URL prefix
courses_bp = Blueprint('courses', __name__, url_prefix='/api/courses')

# Temporary in-memory database for testing
courses_list = []
course_id_counter = 1

# Helper function (Task 2, Step 44)
def make_response_json(data, status_code=200):
    return jsonify({'status': 'success', 'data': data}), status_code

@courses_bp.route('/', methods=['GET'])
def get_courses():
    return make_response_json(courses_list)

@courses_bp.route('/', methods=['POST'])
def create_course():
    global course_id_counter
    data = request.get_json()
    
    # Task 2, Step 42: Validate JSON payload
    if not data:
        return jsonify({'error': 'Invalid or missing JSON payload'}), 400
        
    required_fields = ['name', 'code', 'credits']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'Missing required field: {field}'}), 400
    
    new_course = {
        'id': course_id_counter,
        'name': data['name'],
        'code': data['code'],
        'credits': data['credits']
    }
    courses_list.append(new_course)
    course_id_counter += 1
    
    return make_response_json(new_course, 201)

@courses_bp.route('/<int:course_id>', methods=['GET'])
def get_course(course_id):
    course = next((c for c in courses_list if c['id'] == course_id), None)
    if not course:
        return jsonify({'error': 'Course not found'}), 404
    return make_response_json(course)

@courses_bp.route('/<int:course_id>', methods=['PUT'])
def update_course(course_id):
    course = next((c for c in courses_list if c['id'] == course_id), None)
    if not course:
        return jsonify({'error': 'Course not found'}), 404
        
    data = request.get_json()
    if data:
        course['name'] = data.get('name', course['name'])
        course['code'] = data.get('code', course['code'])
        course['credits'] = data.get('credits', course['credits'])
        
    return make_response_json(course)

@courses_bp.route('/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    global courses_list
    course = next((c for c in courses_list if c['id'] == course_id), None)
    if not course:
        return jsonify({'error': 'Course not found'}), 404
        
    courses_list = [c for c in courses_list if c['id'] != course_id]
    return jsonify({'status': 'success', 'message': 'Course deleted'}), 204