from flask import Flask, render_template
 
app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/translate')
def about():
    return 'translate 페이지'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)