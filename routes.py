from app import app

@app.route('/')
@app.route('/index')
@app.route('/ashwin')
ashwin
def index():
    return 'Hello World!'
