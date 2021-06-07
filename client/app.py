import sys
from flask import Flask, render_template, request, jsonify

import torch

from crop import crop
from generatorImage import Generator, generatorImage
from makePartOfImage import makePartOfImage
from changeBackground import changeBackground
from combineImage import combineImage

app = Flask(__name__)

@app.route('/')
def main() :
    return render_template('main.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    value = request.form

    print(value.getlist('h')[0])

    x = int(float(value.getlist('x')[0]))
    y = int(float(value.getlist('y')[0]))
    w = int(float(value.getlist('w')[0]))
    h = int(float(value.getlist('h')[0]))
    x0 = int(float(value.getlist('x0')[0]))
    y0 = int(float(value.getlist('y0')[0]))
    
    img = request.files['upload_image']
    
    img.save('../images/upload_image.png')

    crop(x - x0, y - y0, w, h)
    

    
    makePartOfImage()
    
    changeBackground()
    
    combineImage(x - x0, y - y0, w, h)
    
    return jsonify(value.getlist('left'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)