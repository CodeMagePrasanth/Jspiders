from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)
db_file = "employee.db"

def create_db():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employee (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                department TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
                )
            ''')
    conn.commit()
    conn.close()

def get_cursor():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    conn.row_factory = sqlite3.Row
    return conn
 
@app.route("/", methods=["GET"])
def index():
    return "hello, welcome to the employee directory"

@app.route("/employee", methods=["GET"])
def get_employee():
    emplyoee_list = []
    cursor = get_cursor()
    employees = cursor.execute("SELECT * FROM employee").fetchall()
    for employee in employees:
        employee_list.append(dict(employee_list))
    print(employee_list)
    return jsonify(employee_list)
    # return jsonify([dict(employee) for  employee in emplyoees])


    # return jsonify({"message":"got my employee"})

@app.route("/employee/<emp_id>", methods=["GET"])
def get_employee_by_id(emp_id):
    # cursor = get_cursor()
    # employee = sursor.execute(f'SELECT * FROM employee where id = {emp_id}').fetchone
    return jsonify({f"got employee details for id{emp_id}"})
    # return jsonify(dict(employee))

@app.route("/employee", methods=["POST"])
def add_employee():
    cursor = get_cursor()
    payload = request.get_json()
    cursor.execute('INSERT INTO employee (name, email, department) VALUES (?, ?, ?)',(payload["name"], payload["email"], payload["department"]))
    cursor.commit()
    print(payload)
    return jsonify({"message":"employee add"})
 
@app.route("/employee", methods=["PUT"])
def update_employee():
    return jsonify({"employee updated"})

@app.route("/employee", methods=["DELETE"])
def delete_employee():
    return jsonify({"employee deleted"})

if __name__ == "__main__":
    create_db()
    app.run(debug=True)