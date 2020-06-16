from flask import Flask

app = Flask(__name__)

"""
Routes
"""
@app.route('/',methods=['GET'])
def index():
    return "<h1>BEEEYA</h1>"

if __name__ == '__main__':
    app.run(debug=True)
