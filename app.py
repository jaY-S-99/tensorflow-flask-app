from flask import Flask,render_template,redirect

app = Flask(__name__)

"""
Routes
"""
@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
