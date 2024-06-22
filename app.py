from flask import Flask, render_template, request, jsonify
import random
import string

# Initialiser l'application Flask
app = Flask(__name__)

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    length = int(request.form['length'])
    password = generate_password(length)
    return jsonify({'password': password})

if __name__ == '__main__':
    app.run(debug=True)