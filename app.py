from flask import Flask,url_for
from markupsafe import escape
app=Flask(__name__)
@app.route('/')
def hello():
    return 'Hello'
@app.route('/user/<name>')
def user_page(name):
    return f'User: {escape(name)}'
@app.route('/test')
def test_url_for():
    # 下面是一些调用示例（请访问 http://localhost:5000/test 后在命令行窗口查看输出的 URL）：
    print(url_for('hello'))  # 生成 hello 视图函数对应的 URL，将会输出：/
    # 注意下面两个调用是如何生成包含 URL 变量的 URL 的
    print(url_for('user_page', name='greyli'))  # 输出：/user/greyli
    print(url_for('user_page', name='peter'))  # 输出：/user/peter
    print(url_for('test_url_for'))  # 输出：/test
    # 下面这个调用
    print(url_for('test_url_for', num=2))  
    return 'Test page'
if __name__ == '__main__':
    app.run(debug=True)
