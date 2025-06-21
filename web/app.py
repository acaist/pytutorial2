# app.py
'''
from flask import Flask, jsonify

# 初始化 Flask 应用实例
app = Flask(__name__)

# 定义路由：根路径（/）
@app.route('/', methods=['GET'])
def home():
    return "Hello, Flask + Gunicorn!"  # 返回字符串

# 定义路由：/about（返回 HTML）
@app.route('/about', methods=['GET'])
def about():
    return "<h1>About Page</h1><p>This is a simple Flask application.</p>"

# 定义路由：/contact（返回纯文本）
@app.route('/contact', methods=['GET'])
def contact():
    return "Contact us at   "


# 定义 API 接口：/api/data（返回 JSON）
@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({
        "message": "This is data from Flask!",
        "status": "success"
    })


# 启动开发服务器（仅用于本地调试，生产环境用 Gunicorn）
if __name__ == '__main__':
    app.run(debug=True, port=5000)
'''

from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # 用于会话加密（生产环境应使用更安全的密钥）

# 模拟用户数据库（实际项目应使用数据库存储）
MOCK_USERS = {
    "admin": "123456",  # 用户名: 密码（实际应存储哈希值）
    "password": "123456"
}

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        remember = 'remember' in request.form  # 是否勾选“记住我”

        # 验证用户（实际项目应查询数据库并校验密码哈希）
        if username in MOCK_USERS and MOCK_USERS[username] == password:
            # 登录成功，设置会话
            session['user_id'] = username
            session['remember'] = remember
            # return jsonify({"success": True, "message": "登录成功"})
            return render_template('dashboard.html', username=username)
        else:
            # return jsonify({"success": True, "message": "用户名或密码错误"})
            return render_template('dashboard.html', username=username)

    # GET 请求返回登录页面
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    # 检查用户是否已登录（通过会话）
    if 'user_id' not in session:
        # return redirect(url_for('login'))
        pass
    
    # 获取当前用户信息（实际项目从数据库查询）
    user = session['user_id']
    return render_template('dashboard.html', username=user)

@app.route('/logout')
def logout():
    # 清除会话
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)