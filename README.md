# Bees

## 1) Count the total number of the bees

This proposed model is based on Autoencoder CNN networks that try to predict images that show the location of the bees is the image.
The inputs are color images tha provided by the images of the bees from the dataset.



## 2) Publication of an API using containers

Now that you have a model, build a simple application that serves predictions as a web service.
This task consists of writing a simple REST API with a single prediction endpoint. For a given image, this endpoint should return a total number of bees as JSON. Ideally, use Docker to containerize your API.

Example usage of your Docker application:

`docker build -t <your-rest-api-docker-image> .`
`docker run -t <your-rest-api-docker-image> -d`
`curl http://<DOCKER-IP>:<DOCKER-PORT>/predict?image_url=http://domain.com/image.jpeg`

## How to complete the challenge

Create a new git repository for your solution.
Organize your work within that repository. When you get to a stopping point, archive it and send it to us. Do not forget to document your code, using a README.md and code documentation, where applicable.

# Evaluation
Your challenge results will be evaluated based on the following criteria:

- model accuracy;
- code cleanliness;
- level of creativity/ingenuity of your solution.

# Questions?
Feel free to [email us](mailto:herbert@hasty.ai) with any questions you might have about the challenge.
