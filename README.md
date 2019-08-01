# Bees

## 1) Count the total number of the bees
The goal of this project is to cunt the number of the bees from the input images.

It is done in two main part:
The First one is system training, and second one is cunting the number of bees, with regard to the prdicted images from the system.

The proposed model is based on Autoencoder CNN networks that try to predict images to show the location of the bees in the image.
The inputs are color images tha provided by the images of the bees from the dataset.
The output of the system is the image that predicted by system and it is show the location of the bees. (this model could be easily generalized for video for show the segmented part real time.)

after training the system, a simple trick help to find the number of the bees, with regard to predicted images from system and black and white version of that, easily we can found the number of white holes in the images that indicate the bees. in the model.ipynb
at the end result are shown by images.


## 2) Publication of an API using containers

This file included the app.py that uses flask and flask restful to make API. and then dockerize it on the server.

