from flask import Flask, jsonify

app = Flask(__name__)
app.users = {}

# 유저 정보 조회 API
@app.route("/user/<int:user_id>", methods=['GET'])
def get_user(user_id):

    if user_id not in app.users:
        return '사용자가 존재하지 않습니다.', 400

    return jsonify(app.users[user_id])
