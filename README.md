# Bees

## 1) Count the total number of the bees

The goal of this task is to build a machine learning model to count the total number of honeybees. Download data from the link below: 

**Dataset:** <http://visal.cs.cityu.edu.hk/downloads/smallobjects/>
**Image folder:** honeybee

There are 118 labeled images. Next, build a solution that returns a number of honeybees per image.

Provide a summary (ideally jupyter notebook) with the results and findings that were most important for you.

The challenge is deliberately kept very general. You are free to use the approach you think is best.

### Questions to keep in mind
- How well does your model perform? How does it compare to the simplest baseline model you can think of?
- How many images are required to build an accurate model?
- What will be an ideal metric for this use-case?
- Where do you see the main challenge in building a model like the one we asked here?

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
