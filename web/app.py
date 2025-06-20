# app.py
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