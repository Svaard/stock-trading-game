from webapp import app
from flask import jsonify

@app.route('/')
@app.route('/index')
def index():
    return jsonify({'This': 'is', 'A': 'test'})