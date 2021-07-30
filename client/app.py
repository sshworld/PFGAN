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

app = Flask(__name__)

@app.route('/')
def main() :
    return render_template('main.html')

@app.route('/index')
def index():
    return render_template('index.html')

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
    
    folderName = str(now.tm_year) + str(now.tm_mon) + str(now.tm_mday) + str(now.tm_hour) + str(now.tm_min)
    
    createFolder('./static/images/' + folderName)
    
    img.save('./static/images/' + folderName + '/upload_image.png')

    img = Image.open('./static/images/' + folderName + '/upload_image.png')

    img = img.resize((rw, rh))
    
    img.save('./static/images/' + folderName + '/upload_image.png')

    crop(x - x0, y - y0, w, h, folderName)
    
    for i, model in enumerate(modelName) :
        generatorImage(model, folderName, str(i))
        
        makePartOfImage(folderName, str(i))
        
        changeBackground(folderName, str(i))
        
        combineImage(x - x0, y - y0, w, h, folderName, str(i))
    
    return url_for('index')

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

if __name__ == '__main__':
    Generator(1)
        
    app.run(debug=True, host='0.0.0.0', port=5000)
    

