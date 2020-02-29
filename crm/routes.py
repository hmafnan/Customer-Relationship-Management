from crm import app

from flask import render_template

touches = [
    {
        'description': 'This desc',
        'date': 'new date'
    },
    {
        'description': 'New description',
        'date': 'to date'
    }
]

@app.route('/')
def home():
    return render_template('home.html',  touches=touches)

@app.route('/about')
def hello_about():
    return render_template('about.html')