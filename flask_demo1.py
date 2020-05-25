#1.导入flask扩展
from flask import Flask, render_template
from flask import request
from flask import jsonify
import base64
from urllib.parse import quote, unquote

#2.创建flask应用程序实例
# 需要传入 __name__，是为了确定资源所在路径
app = Flask(__name__)

#3.定义路由及视图函数
# 是通过装饰器来实现的
@app.route('/')
def index():
    return render_template('evil4.html');

@app.route('/log', methods=['POST'])
def accessLog():
    reqMethod = request.method
    content = request.form.get("content").strip()
    ret = jsonify(reqMethod=reqMethod, reqParam=content)

    # 将数据保存到文件
    s = base64.b64decode(content.encode('utf-8')).decode('utf-8')
    print(s)
    realContent = unquote(s, 'utf-8')
    print(realContent)
    with open('tmp/data.txt', 'w+', encoding='utf-8') as f:
        f.write(realContent)

    return ret

#4.启动程序
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=17374, debug=True)
