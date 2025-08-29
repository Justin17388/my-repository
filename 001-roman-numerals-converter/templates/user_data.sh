#! /bin/bash
yum update -y
yum install python3 -y
yum install python3-pip -y
pip3 install flask
yum install git -y
cd /home/ec2-user
wget -P templates https://raw.githubusercontent.com/Justin17388/my-repository/refs/heads/main/001-roman-numerals-converter/templates/index.html
wget -P templates https://raw.githubusercontent.com/Justin17388/my-repository/refs/heads/main/001-roman-numerals-converter/templates/result.html
wget https://raw.githubusercontent.com/Justin17388/my-repository/refs/heads/main/001-roman-numerals-converter/app.py
python3 app.py     