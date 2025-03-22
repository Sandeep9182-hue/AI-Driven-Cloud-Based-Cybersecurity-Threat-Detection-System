from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)
API_URL = "https://your-api-gateway.amazonaws.com/prod/predict"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    login_attempts = int(request.form['login_attempts'])
    failed_attempts = int(request.form['failed_attempts'])

    response = requests.post(API_URL, json={
        "login_attempts": login_attempts,
        "failed_attempts": failed_attempts
    })

    result = response.json()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
