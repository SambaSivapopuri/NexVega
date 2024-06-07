from flask import Flask, request, jsonify
import Algorithm
import db

app = Flask(__name__)

user_data = {}

@app.route('/add_user', methods=['POST'])
def add_user():
    user_id = request.json['user_id']
    name = request.json['name']
    email = request.json['email']
    if user_id not in user_data:
        user_data[user_id] = Algorithm.User(user_id, name, email)
        db.add_user_to_database(user_id, name, email) 
        return jsonify({"message": "User added successfully."}), 201
    return jsonify({"message": "User already exists."}), 400

@app.route('/add_friend', methods=['POST'])
def add_friend():
    user_id = request.json['user_id']
    friend_id = request.json['friend_id']
    
    if user_id in user_data and friend_id in user_data:
        user_data[user_id].add_friend(friend_id)
        user_data[friend_id].add_friend(user_id)
        db.add_friendship_to_database(user_id, friend_id) 
        return jsonify({"message": "Friend added successfully."}), 201
    return jsonify({"message": "User not found."}), 404

@app.route('/suggest_friends', methods=['GET'])
def get_suggested_friends():
    user_id = int(request.args.get('user_id'))
    if user_id in user_data:
        suggestions = Algorithm.suggest_friends(user_id, user_data)
        print(suggestions)
        db.store_recommendations(user_id, suggestions) 
        return jsonify({"suggested_friends": suggestions}), 200
    return jsonify({"message": "User not found."}), 404

if __name__ == '__main__':
    app.run(debug=True)
