from app import app
from app.models.users import User
from flask import jsonify


@app.route('/users', methods=['GET'])
def get_users():
    users = map(lambda user: user.as_dict(), User.query.all())
    return jsonify(users)


@app.route('/users/<int:user_id>', methods=['GET'])
def get_users_by_id(user_id):
    users = User.query.get(user_id).as_dict()
    return jsonify(users)
