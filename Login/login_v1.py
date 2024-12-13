from flask import Flask, jsonify
import csv
from pathlib import Path

app = Flask(__name__)

def load_users():
    if not Path('users.csv').exists():
        with open('users.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['name', 'email', 'password'])
            writer.writerow(['admin', 'admin@example.com', 'admin123'])

def get_all_users():
    with open('users.csv', 'r') as f:
        reader = csv.DictReader(f)
        return list(reader)

@app.route('/users')
def users():
    return jsonify(get_all_users())

@app.route('/')
def home():
    return 'Hello, World!'

if __name__ == '__main__':
    load_users()
    app.run(debug=True)