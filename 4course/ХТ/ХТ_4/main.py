from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {"id": 1, "name": "John", "age": 30},
    {"id": 2, "name": "Jane", "age": 28},
]

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

@app.route("/users", methods=["POST"])
def create_user():
    user = request.json
    user["id"] = len(users) + 1
    users.append(user)
    return jsonify(user["id"])

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = next((user for user in users if user["id"] == user_id), None)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)

@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    user = next((user for user in users if user["id"] == user_id), None)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    updated_user = request.json
    user.update(updated_user)
    return jsonify(user)

@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    global users
    users = [user for user in users if user["id"] != user_id]
    return jsonify({"status": "success"})

if __name__ == "__main__":
    app.run(debug=True)

