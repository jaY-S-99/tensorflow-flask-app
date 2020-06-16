from flask import Flask,render_template,redirect,url_for,request
import os
import inference
import uuid

app = Flask(__name__)

"""
Routess
"""
@app.route('/',methods=['GET','POST'])
def index():
    if request.method == "POST":
        image_path = request.data['imageURL']
        if image_path is not None:
            class_name = inference.get_predictions(image_path)
            result = {
                'class_name': class_name,
                'image_path': image_path
            }
            return render_template('result.html',result=result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
