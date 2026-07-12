import sqlite3
import requests
from flask import Flask, jsonify, request

app = Flask(__name__)
DB_FILE = "students.db"
COURSE_SERVICE_URL = "http://127.0.0.1:5001/api/courses/"

def init_db():
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS enrollments (
                student_id INTEGER NOT NULL,
                course_id INTEGER NOT NULL,
                PRIMARY KEY (student_id, course_id)
            )
        """)
        conn.commit()

@app.route("/api/students/<int:student_id>/enroll", methods=["POST"])
def enroll_student(student_id):
    payload = request.get_json() or {}
    course_id = payload.get("course_id")
    
    if not course_id:
        return jsonify({"error": "Missing parameter: course_id"}), 400

    # Inter-service HTTP call to check if the course exists
    try:
        response = requests.get(f"{COURSE_SERVICE_URL}{course_id}", timeout=2.0)
        if response.status_code == 404:
            return jsonify({"error": f"Enrollment rejected: Course {course_id} does not exist"}), 404
    except requests.exceptions.ConnectionError:
        return jsonify({
            "error": "Service Unavailable",
            "message": "The Course Management Service is down. Enrollment cannot be processed at this time."
        }), 503

    # Write the enrollment locally if verification passes
    with sqlite3.connect(DB_FILE) as conn:
        try:
            conn.execute("INSERT INTO enrollments (student_id, course_id) VALUES (?, ?)", (student_id, course_id))
            conn.commit()
        except sqlite3.IntegrityError:
            return jsonify({"message": "Student already registered for this course"}), 200

    return jsonify({"message": f"Successfully enrolled student {student_id} into course {course_id}"}), 201

if __name__ == "__main__":
    init_db()
    app.run(port=5002, debug=True)