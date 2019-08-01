from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import pickle
import numpy as np
import werkzeug
from skimage import io, filters,measure
app = Flask(__name__)
api = Api(app)


clf_path = 'final_prediction.pickle'
with open(clf_path, 'rb') as f:
    model.clf = pickle.load(f)

parser = reqparse.RequestParser()
parse.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')

class PredictSentiment(Resource):
    def get(self):
        args = parser.parse_args()
        user_image = args['file']

	vector=np.reshape(user_image,(-1,240,320,3))
        prediction = model.predict(vector)
	pred=np.reshape(preds,(x, y))
	val = filters.threshold_otsu(pred)
	im2=pred>val
	l = measure.label(im2)
        output = {'prediction': l}
        
        return output


api.add_resource(PredictSentiment, '/')


if __name__ == '__main__':
    app.run(debug=True)
