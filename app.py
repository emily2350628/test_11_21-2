from flask import Flask, render_template, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'
@app.route('/')
def index():
    return 'If you see this, flask index is working.'

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/Brocoli')
def broc():
    return 'If you see this, flask brocoli is working.'

if __name__ == '__main__':
    app.run(debug=True)
