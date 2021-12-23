import sys
from flask import Flask, render_template, request, jsonify, redirect, url_for
from PIL import Image
from flask.helpers import url_for

from crop import crop

from generator import Generator
from generatorImage import generatorImage
from makePartOfImage import makePartOfImage
from changeBackground import changeBackground
from combineImage import combineImage
from comparison import comparison
from createFolder import createFolder
from imageSplit import imageSplit

import argparse
import os
import random
import torch
import torch.nn as nn
import torch.nn.parallel
import torch.backends.cudnn as cudnn
import torch.optim as optim
import torch.utils.data
import torchvision.datasets as dset
import torchvision.transforms as transforms
import torchvision.utils as vutils
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython.display import HTML
import cv2
import time
import glob

app = Flask(__name__)

@app.route('/')
def main() :
    return render_template('main.html')

@app.route('/index')
def index():
    name = request.args.get('name')
    index = request.args.get('index')
    
    
    return render_template('index.html', name = name, index = index)

@app.route('/choose')
def choose():
    name = request.args.get('name')
    count = len(os.listdir('./static/images/' + name + '/combine'))
    print(count)

    return render_template('choose.html', name = name, count = count)

@app.route('/translate', methods=['POST'])
def translate():
    
    modelName = ['apple', 'pepper', 'tomato']
    
    value = request.form

    print(value.getlist('h')[0])

    x = int(float(value.getlist('x')[0]))
    y = int(float(value.getlist('y')[0]))
    w = int(float(value.getlist('w')[0]))
    h = int(float(value.getlist('h')[0]))
    x0 = int(float(value.getlist('x0')[0]))
    y0 = int(float(value.getlist('y0')[0]))
    rw = int(float(value.getlist('rw')[0]))
    rh = int(float(value.getlist('rh')[0]))
    
    img = request.files['upload_image']
    
    now = time.localtime()
    
    date = str(now.tm_year) + str(now.tm_mon) + str(now.tm_mday) + str(now.tm_hour) + str(now.tm_min)
    
    folderName = './static/images/' + date
    
    createFolder(folderName)
    createFolder(folderName + '/combine')
    createFolder(folderName + '/changeBackground')
    
    img.save(folderName + '/upload_image.png')

    img = Image.open(folderName + '/upload_image.png')

    img = img.resize((rw, rh))
    
    img.save(folderName + '/upload_image.png')

    crop(x - x0, y - y0, w, h, folderName)
    
    imageSplit(rw, rh, folderName, 5)
    
    count = 1
    
    for i, model in enumerate(modelName) :
        generatorImage(model, folderName, str(i))
        
        makePartOfImage(folderName, str(i))
        
        for file in glob.glob(folderName + '/split/*.png') :
            changeBackground(folderName, file, str(i), str(count))
            count += 1
        
        changeBackground(folderName, folderName + '/crop.png', str(i), str(count))
        count += 1
        
    combineImage(x - x0, y - y0, w, h, folderName)
        
    comparison(folderName)
    
    return url_for('choose', name = date)

if __name__ == '__main__':
    Generator(1)
        
    app.run(debug=True, host='0.0.0.0', port=5000)
    

