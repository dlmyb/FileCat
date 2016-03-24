# from __future__ import unicode_literals
# -*- coding:utf-8 -*-
__author__ = 'calculusma'

from flask import Flask,request,render_template,redirect,send_from_directory,abort
from tiquma import prepare
from storage import session
from sms import sendemail
from requests.exceptions import ReadTimeout
import os,requests
import time

app = Flask(__name__)
app.debug = True
s = session()
q = prepare()

LOCALHOST = "http://localhost:5000"

@app.route("/",methods=['GET'])
def index():
    return render_template("index.html",title=u"欢迎使用")

@app.route("/save",methods=['GET'])
def save():
    return render_template("save.html",title=u"储存页面")

@app.route("/file",methods=['POST'])
def upload():
    f = request.files['file']
    if not f:
        abort(404)
    email = request.form.get("email")
    code = q.get()
    t = int(time.time())
    os.system("mkdir upload/%s"%t)
    filename = f.filename
    if isinstance(filename,unicode):
        filename = filename.encode("utf-8")
    root = "upload/%s/%s"%(t,filename)
    f.save(root)
    s.set(code,LOCALHOST+"/upload/%d/%s"%(t,filename))
    if email:
        j = {
            "filename":filename,
            "code":code,
            "email":email.encode("utf-8")
        }
        try:
            requests.get(url=LOCALHOST+"/mail",json=j,timeout=1)
        except ReadTimeout:
            pass
    return render_template("success.html",title=u"上传成功",code=code)

@app.route("/get",methods=['GET'])
def check():
    code = request.args['code']
    root = s.get(code)
    if root:
        return redirect(root)
    else:
        abort(404)

@app.route("/upload/<t>/<path:path>",methods=['GET'])
def static_file(path,t):
    return send_from_directory('upload/%s'%t,path)

@app.route("/about",methods=['GET'])
def about():
    return render_template("about.html",title=u"关于我们")

@app.route("/mail")
def send_email():
    j = request.get_json()
    filename = j['filename'].encode("utf-8")
    code = j['code'].encode("utf-8")
    email = j['email'].encode("utf-8")
    sendemail(filename,code,email)
    return "ok"

@app.errorhandler(404)
def error(error):
    return render_template("404.html",title=u"失败"),404

if __name__ == '__main__':
    app.run()