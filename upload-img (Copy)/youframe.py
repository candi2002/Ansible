import requests, os, re
from flask import Flask, redirect, url_for, render_template, request
from werkzeug.utils import secure_filename
import socket

app = Flask(__name__)

# Hàm lấy địa chỉ IP động
def get_ip_address():
    # Lấy IP của máy chủ
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

@app.route("/")
def uploader():
    path = 'static/uploads/'
    uploads = sorted(os.listdir(path), key=lambda x: os.path.getctime(path + x))  # Sorting as per image upload date and time
    uploads = ['uploads/' + file for file in uploads]
    uploads.reverse()

    ip_address = get_ip_address()  # Lấy địa chỉ IP động của server

    return render_template("index.html", uploads=uploads, server_ip=ip_address)  # Truyền IP vào file HTML

app.config['UPLOAD_PATH'] = 'static/uploads'

@app.route("/upload", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_PATH'], filename))
        return redirect("/")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
