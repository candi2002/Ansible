import os
from flask import Flask, redirect, url_for, render_template, request
from werkzeug.utils import secure_filename
import socket

app = Flask(__name__)

# Hàm lấy địa chỉ IP
def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]  # Lấy IP nội bộ
    except Exception:
        ip_address = '127.0.0.1'
    finally:
        s.close()
    return ip_address

# Hàm tạo tên tệp duy nhất với hậu tố _1, _2, _3,...
def get_unique_filename(filename):
    name, ext = os.path.splitext(filename)
    counter = 1
    new_filename = filename

    # Kiểm tra xem tên tệp đã tồn tại chưa, nếu tồn tại thì thêm hậu tố _1, _2, _3...
    while os.path.exists(os.path.join(app.config['UPLOAD_PATH'], new_filename)):
        new_filename = f"{name}_{counter}{ext}"
        counter += 1
    
    return new_filename

@app.route("/")
def uploader():
    path = 'static/uploads/'
    uploads = sorted(os.listdir(path), key=lambda x: os.path.getctime(path + x))  # Sắp xếp theo thời gian
    uploads = ['uploads/' + file for file in uploads]
    uploads.reverse()

    ip_address = get_ip_address()  # Lấy địa chỉ IP mạng nội bộ

    return render_template("index.html", uploads=uploads, server_ip=ip_address)  # Truyền IP vào template

# Đặt đường dẫn lưu trữ tệp tải lên
app.config['UPLOAD_PATH'] = 'static/uploads'

@app.route("/upload", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        unique_filename = get_unique_filename(filename)  # Tạo tên tệp duy nhất với hậu tố
        f.save(os.path.join(app.config['UPLOAD_PATH'], unique_filename))  # Lưu tệp với tên duy nhất
        return redirect("/")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
