# Bees

## 1) Count the total number of the bees
the goal of this project is to cunt the number of the bees in input images.
I did it in two main part:
The First one is system training, and second one is cunt yhe number with regard to the prdicted images from the system.

The proposed model is based on Autoencoder CNN networks that try to predict images that show the location of the bees is the image.
The inputs are color images tha provided by the images of the bees from the dataset.
The output of the system is the image tha predicted by system and it is show the location of the bees.
after training the system, a simple trick help to find the number ofthe bees, with regard to predicted images from system and black and white version of that, easily we can found the number of white holes in the images that indicate the bees. 


## 2) Publication of an API using containers

This file included the app.py that uses flask and flask restful to make API. and then dockerize it on the server.


