#!/bin/bash
sudo apt update -y
sudo apt install python3-pip -y
pip3 install flask requests

git clone https://github.com/your-username/AI-Driven-Cloud-Based-Cybersecurity-Threat-Detection-System.git
cd AI-Driven-Cloud-Based-Cybersecurity-Threat-Detection-System/flask_web_dashboard/
python3 app.py
