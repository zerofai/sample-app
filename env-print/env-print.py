from flask import Flask, render_template
import os

template_dir = os.path.abspath('')  # Set the template directory to the current directory
CONTAINER_PORT = os.getenv('containerPort', '8000')  # Read containerPort from environmental variable

app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def home():
    username = os.environ.get('USERNAME', 'Not set')
    password = os.environ.get('PASSWORD', 'Not set')
    return render_template('index.html', username=username, password=password)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=CONTAINER_PORT)