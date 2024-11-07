sudo apt update
sudo apt install python3 git -y
//Nếu đã cài ansible
ansible --version
sudo apt remove ansible -y

sudo apt install pipx -y
pipx ensurepath
//Sau cái này phải tắt  rồi mở lại terminal nha!!!
pipx install --include-deps ansible
ansible --version

//Tải file từ trang web: https://dev.mysql.com/downloads/repo/apt/
cd Downloads
sudo dpkg -i mysql-apt-config_0.8.32-1_all.deb
-> OK
sudo apt update
sudo apt install mysql-server mysql-client -y
-> Nhập password cho root, nên để khó 1 tí
-> OK

sudo mysql_secure_installation
-> nhập password root
-> y
->2
->n
->y
->y
->y
->y
sudo systemctl status mysql
// Nếu có 3 cái màu xanh là thành công
mysql -u root -p
-> Nhập mật khẩu
-> CREATE DATABASE semaphore;
-> CREATE USER 'semaphore'@'localhost' IDENTIFIED BY 'Matkhau@123';
//Nhập mật khẩu rtheo ý thích
-> GRANT ALL PRIVILEGES ON semaphore.* TO 'semaphore'@'localhost';
->EXIT;

mysql -u semaphore -p
//Chỗ này xài mật khẩu của Semaphore ở trên
-> SHOW DATABASES;
// Nếu nhìn vô cái bảng thấy có 3 giá trị, và có 1 giá trị là semaphore thì là đúng rồi
->EXIT;

wget https://github.com/semaphoreui/semaphore/releases/\
download/v2.10.18/semaphore_2.10.18_linux_amd64.deb

sudo dpkg -i semaphore_2.10.18_linux_amd64.deb

sudo useradd -m -d /opt/semaphore -s /bin/bash semaphore
sudo passwd semaphore
//Chỗ này đặt mật khẩu cho semaphore nha
sudo  chmod 770 /opt/semaphore
sudo groupadd ansiblegroup
sudo gpasswd -M candi,semaphore ansiblegroup
// Chỗ candi ở trên, thay bằng tên người dùng

sudo su semaphore 
//Tên người dùng đổi thành semaphore
cd
pwd
//Hai lệnh trên là để chắc chắn, nếu thấy /opt/semaphore là đã vào thành công
semaphore setup
-> "enter"
-> "enter"
-> semaphore
-> Mật khẩu semaphore của bạn, vì đã chọn strong nên phải theo đúng cú pháp
-> "enter"
-> /opt/semaphore
-> "enter"
-> yes
-> mailrise.homelab.lan
-> 8025
-> semaphore@homelab.lan
-> "enter"
-> "enter"
-> "enter"
-> "enter"
-> "enter"
-> "enter"
-> admin
-> slack@mailrise.xyz
-> Admin
-> mật khẩu cho tài khoản semaphore, khác với mật khẩu ở trên nha
ls -l
//Thấy total 4 là được
which semaphore
//Thấy usr/bin/semaphore là được


ansible --version
pipx ensurepath
exit
sudo su semaphore 
cd
pwd
//Hai lệnh trên là để chắc chắn, nếu thấy /opt/semaphore là đã vào thành công
echo $PATH
//nó sẽ hiện ra một mớ, k lỗi là oke
pipx install --include-deps ansible
ansible --version
pipx inject ansible pywinrm

nano .ansible.cfg
//Nội dung trong file nè
[defaults]
interpreter_python=auto_silent
host_key_checking=False

////////////////////// Lưu lại
exit
//Thoát ra
sudo nano /etc/systemd/system/semaphore.service
/////////////Nội dung file nè
[Unit]
Description=Ansible Semaphore
Documentation=https://docs.semui.co/
Wants=network-online.target
After=network-online.target
ConditionPathExists=/usr/bin/semaphore
ConditionPathExists=/opt/semaphore/config.json
Requires=mysql.service

[Service]
User=semaphore
Group=semaphore
Environment="PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/semaphore/.local/bin"
Restart=always
RestartSec=10s
ExecStart=/usr/bin/semaphore service --config=/opt/semaphore/config.json
ExecReload=/bin/kill -HUP $MAINPID
StandardOutput=journal
StandardError=journal
SyslogIdentifier=semaphore

[Install]
WantedBy=multi-user.target
/////////////////////////////////////////////////

sudo systemctl daemon-reload
sudo systemctl enable semaphore
sudo systemctl start semaphore
sudo systemctl status semaphore



sudo mkdir /opt/ansible
sudo chown -R candi:ansiblegroup /opt/ansible
sudo chmod -R 770 /opt/ansible
cd /opt/ansible
git init demo
//Demo là tên cái project
cd demo
git branch -m main

/opt/ansible/demo

nano /opt/ansible/inventory

sudo su semaphore
cd
ls -l /opt/semaphore/.ssh/
ssh-keygen -t ed25519 -f /opt/semaphore/.ssh/id_ed25519
chmod 600 /opt/semaphore/.ssh/id_ed25519
ssh-copy-id -i /opt/semaphore/.ssh/id_ed25519.pub candi@192.168.1.132
ssh -i /opt/semaphore/.ssh/id_ed25519 candi@192.168.9.116
exit

ssh-copy-id -i /opt/semaphore/.ssh/id_ed25519.pub candi@192.168.1.108
exit 

cat /opt/semaphore/.ssh/id_ed25519
//In cái đó copy vô

sudo vi /opt/ansible/inventory
[all]
192.168.0.63 ansible_ssh_user=candi ansible_become=yes ansible_become_user=root ansible_become_pass=candi
192.168.0.71 ansible_ssh_user=candi ansible_become=yes ansible_become_user=root ansible_become_pass=candi
