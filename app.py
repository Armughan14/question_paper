from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

def fetch_data():
    url = "https://script.google.com/macros/s/AKfycbzTnmDwDi8Gl60qzrJmB6hRJ1rSnifiu87wM3vX-rGjA2PwgA0drepbni0u3mv5KL0I/exec"
    response = requests.get(url)
    return response.json()

@app.route('/')
def index():
    data = fetch_data()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
