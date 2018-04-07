from app import app

@app.route('/')
@app.route('/index')
@app.route('/ashwin')
def index():
    return 'Hello World!'
