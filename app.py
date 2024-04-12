from flask import Flask, render_template, request
from cryptography.fernet import Fernet

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Key for encryption
key = Fernet.generate_key()
cipher = Fernet(key)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    message = request.form['message'].encode()
    encrypted_message = cipher.encrypt(message)
    return encrypted_message.decode()

@app.route('/decrypt', methods=['POST'])
def decrypt():
    encrypted_message = request.form['message'].encode()
    decrypted_message = cipher.decrypt(encrypted_message)
    return decrypted_message.decode()

if __name__ == '__main__':
    app.run(debug=True)
