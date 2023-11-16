import sqlite3
from flask import Flask, jsonify

app = Flask(__name__)

# 配置数据库路径
app.config['DATABASE'] = 'D:/Works/db/test.db'

@app.route('/', methods=['GET'])
def get_users():
    # 连接到SQLite3数据库
    conn = sqlite3.connect(app.config['DATABASE'] )
    cursor = conn.cursor()

    # 执行SQL查询
    cursor.execute('SELECT * FROM TEST')
    rows = cursor.fetchall()

    # 将查询结果转换为JSON格式
    users = []
    for row in rows:
        user = {
            'id': row[0],
            'name': row[1],
            'age': row[2],
            'address': row[3]
        }
        users.append(user)

    # 关闭数据库连接
    cursor.close()
    conn.close()

    # 返回JSON响应
    return jsonify(users)

if __name__ == '__main__':
    app.run()