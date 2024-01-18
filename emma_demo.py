import requests
import sys
from flask import Flask, render_template, request

# FLASK TO HTML
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('demo.html')

@app.route('/name', methods=['GET','POST'])
def name():
    if request.method == 'POST':
        name = request.form.get('name')
        return render_template('name.html', name = name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)