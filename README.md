# Bees

## 1) Count the total number of the bees
model.ipynb


The goal of this project is to predict the number of moving objects from the input video.
This autoencoder CNN network is trained to count the number of small moving objects in the input video. The input type is RGB videos, and the output is the total number of moving objects. 
The algorithm consists of two main steps: 1) image segmentation, which is performed by a deep neural network, and 2) object counting.

The proposed model is based on Autoencoder CNN networks that try to predict images to show the location of the bees in the image.
The inputs are color images tha provided by the images of the bees from the dataset.
The output of the system is the image that predicted by system and it is show the location of the bees. (this model could be easily generalized for video for show the segmented part real time.)

after training the system, a simple trick help to find the number of the bees, with regard to predicted images from system and black and white version of that, easily we can found the number of white holes in the images that indicate the bees. in the model.ipynb at the end result are shown by images.


## 2) Publication of an API using containers

This file included the app.py that uses flask and flask restful to make API. and then dockerize it on the server.

