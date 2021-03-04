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
    if check_skin(photo):
        preds_dict = predict_class(photo)

        dict_dis = sorted(preds_dict.items(), key=lambda x: x[1], reverse=True)
        dict_dis = dict(sorted(preds_dict.items(), key=lambda x: x[1], reverse=True)[:3])
        print(dict_dis)

        max_val = max(dict_dis, key=dict_dis.get)
        if dict_dis[max_val] <= 30:
            print('healthy')
            return jsonify({'message': 'Healthy Skin Detected'})
        else:
            print('Done')
            description = (disease_description(str(max_val)))
            return jsonify({'message': str(max_val), 'percentage': str(dict_dis[max_val]),
                            'description': description['description'],
                            'symptoms': description['symptoms'],
                            'causes': description['causes'],
                            'treatement-1': description['treatement-1'],
                            'treatement-2': description['treatement-2']})
    else:
        print({'message': 'Please upload image of Infected Area'})
        return jsonify({'message': 'Please upload image of Infected Area'})


if __name__ == '__main__':
    app.run(debug=any)
