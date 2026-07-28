
from flask import Flask, jsonify

app = Flask(__name__)

students = [
    {"id":1,"name":"Amit"},
    {"id":2,"name":"Neha"}
]


@app.route("/students/<int:id>", methods=["GET"])
def delete_student(id):

    for student in students:
        if student["id"] == id:
            students.remove(student)
            return jsonify({"message":"Deleted Successfully"})

    return jsonify({"message":"Student Not Found"}),404

if __name__ == "__main__":
    app.run(debug=True)