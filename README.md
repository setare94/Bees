# Small Object Detection

## 1) Data Set
you can download dataset from here :
http://visal.cs.cityu.edu.hk/downloads/smallobjects/

## 2) Count the total number of the bees
model.ipynb


The goal of this project is to predict the number of moving objects from the input video.
This autoencoder CNN network is trained to count the number of small moving objects in the input video. The input type is RGB videos, and the output is the total number of moving objects. 
The algorithm consists of two main steps: 1) image segmentation, which is performed by a deep neural network, and 2) object counting.



## 3) Publication of an API using containers

This file included the app.py that uses flask and flask restful to make API. and then dockerize it on the server.

