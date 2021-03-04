from flask import Flask, request, jsonify
import os
from datetime import datetime
import numpy as np

from skin_detection import check_skin
from predict import predict_class
from disease_description import disease_description

import cv2

app = Flask(__name__)
UPLOAD_FOLDER = './UPLOAD_FOLDER/'


@app.route('/')
def hello():
    return 'Welcome to the HealthCare App Back-End !'


@app.route('/disease/skin/test', methods=['POST', 'GET'])
def get_image():
    filename = UPLOAD_FOLDER + str(np.random.randint(0, 5000)) + '.png'
    print('Image is incoming')
    photo = request.files['photo']
    # photo.save(filename)
    print('Image Saved..')
    retutn "done"


if __name__ == '__main__':
    app.run(debug=any)
