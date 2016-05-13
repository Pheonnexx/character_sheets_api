from app import app

@app.route('/')
@app.route('/hello')
def index():
    message = "Hello World"
    return message