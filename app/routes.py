from app import app

@app.route('/')
def index():
    return 'Hello World'

@app.route('/test')
def name():
    return 'Test123'