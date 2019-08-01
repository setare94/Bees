from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import pickle
import numpy as np
import werkzeug
#from model import NLPModel
from skimage import io, filters,measure

app = Flask(__name__)
api = Api(app)

#model = NLPModel()

clf_path = 'final_prediction.pickle'
with open(clf_path, 'rb') as f:
    model.clf = pickle.load(f)

#vec_path = 'lib/models/TFIDFVectorizer.pkl'
#with open(vec_path, 'rb') as f:
#    model.vectorizer = pickle.load(f)

# argument parsing
parser = reqparse.RequestParser()
parse.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')
#audioFile.save("your_file_name.jpg")



class PredictSentiment(Resource):
    def get(self):
        # use parser and find the user's query
        args = parser.parse_args()
        user_image = args['file']

        # vectorize the user's query and make a prediction
        #uq_vectorized = model.vectorizer_transform(np.array([user_query]))
	vector=np.reshape(user_image,(-1,240,320,3))
        prediction = model.predict(vector)
#        pred_proba = model.predict_proba(uq_vectorized)

        # Output either 'Negative' or 'Positive' along with the score
#        if prediction == 0:
#            pred_text = 'Negative'
#        else:
#            pred_text = 'Positive'
            
        # round the predict proba value and set to new variable
#        confidence = round(pred_proba[0], 3)
	pred=np.reshape(preds,(x, y))
	val = filters.threshold_otsu(pred)
	im2=pred>val
	l = measure.label(im2)

        # create JSON object
        output = {'prediction': l}
        
        return output


# Setup the Api resource routing here
# Route the URL to the resource
api.add_resource(PredictSentiment, '/')


if __name__ == '__main__':
    app.run(debug=True)
