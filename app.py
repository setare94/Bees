from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pickle as p
# import pandas as pd
import json

# UPLOAD_IMAGE = '/home/tarak/Pictures/Wallpapers/m31.jpg'

app = Flask(__name__)

    
@app.route('/api/', methods=['POST'])
def cuntbees():
    j_data = request.get_json()

    prediction = (model.predict(j_data))
#         f = request.files['UPLOAD_IMAGE']   

    return jsonify(prediction)


if __name__ == '__main__':

    modelfile = 'final_prediction.pickle'    

    model = p.load(open(modelfile, 'rb'))
    
    app.run(debug=True,host='0.0.0.0')