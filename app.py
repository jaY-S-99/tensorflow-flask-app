from flask import Flask,render_template,redirect,url_for,request
import os
import inference

app = Flask(__name__)

"""
Routess
"""
@app.route('/',methods=['GET','POST'])
def index():
    if request.method == "POST":
        uploaded_image= request.files['file']
        if uploaded_image.filename != '':
            image_path = os.path.join('static',uploaded_image.filename)
            uploaded_image.save(image_path)
            class_name = inference.get_predictions(image_path)
            result = {
                'class_name': class_name,
                'image_path': image_path
            }
            return render_template('result.html',result=result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
