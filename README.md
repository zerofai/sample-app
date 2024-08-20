# Sample-APp

This repo contains few very simple python and GO based microservices:

<img width="1030" alt="greeting_hkweather_image" src="https://github.com/zerofai/greeting_hkweather_image/assets/20843048/5dfe4963-8e8f-4961-aeef-35fe627996cd">


# UI
**Welcome to my Microservices Playground! 🎮🚀**

This repo contains a variety of microservices, providing a fun and engaging way to learn about containerization and orchestration using Kubernetes.

In the UI:

- With `/greeting`, you can get a random greeting message.
- The `/weather` endpoint gives weather forecasts for the day.
- To get an image, hit the `/image` endpoint.
- And with `/namegen`, you can generate a random name!

The code is simple and straightforward, showcasing how different microservices can be stitched together using environment variables for easy configuration.

**So what are you waiting for? 😏 Let the learning begin!**

*Fun Fact: This app was dockerized by the author, so no need to worry about deployment or environment setup.*


Code and Dockerfile inside ./ui/py_Dockerfile

# Greeting
This Python Flask application serves as a simple greeting API that returns a randomized greeting along with the current time in GMT+8.  A docker image can be download to run this app.
 
To use this API, make a GET request to its root endpoint ("/v1/greeting"). The application will respond with a JSON object containing a randomly chosen greeting and the current time (formatted as HH:MM:SS) in GMT+8. If an unknown route is accessed, it will return a JSON error message stating that the user should use the correct endpoint.

Code and Dockerfile inside ./greeting/py_Dockerfile

# Weather
This Golang application serves as a simple weather API that returns the latest weather data in JSON format from the Hong Kong Observatory. A docker image can be download to run this app.
 
To use this API, make a GET request to its root endpoint ("/v1/flw"). The application will respond with the current weather information fetched from the data.weather.gov.hk API. If an unknown route is accessed, it will return a JSON error message stating that the user should use the correct endpoint.

Code and Dockerfile inside ./weather/go_Dockerfile
Existing Python version can find in ./weather/py_Dockerfile

# Image
This Python Flask application serves as a simple image API that returns a randomized image from an Amazon S3 bucket. A docker image can be download to run this app.
 
To use this API, make a GET request to its root endpoint ("/v1/image"). The application will respond with a randomly chosen image in JPEG format. If an unknown route is accessed, it will return a JSON error message stating that the user should use the correct endpoint.

Code and Dockerfile that tested with minio is inside ./image/py_Dockerfile_minio

# Namegen
This Golang application serves as a simple name API that returns a randomized full name from a MySQL database. A docker image can be download to run this app.
 
To use this API, make a GET request to its root endpoint ("/v1/name"). The application will respond with a randomly chosen full name in string format. If an unknown route is accessed, it will return a JSON error message stating that the user should use the correct endpoint.

Code and Dockerfile that tested with minio is inside ./image/py_Dockerfile_minio


# To Test locally 
```
export GREETING_HOSTNAME=127.0.0.1:5001
export WEATHER_HOSTNAME=127.0.0.1:5002
export IMAGE_HOSTNAME=127.0.0.1:5003
export NAMEGEN_HOSTNAME=127.0.0.1:5004
```

# To Build the image on M1 for x64
```
docker build . --platform linux/amd64 -t imagename 
```

Image has been build and pushed to DockerHub, for image name please refer to below yaml

# Deployment on k8s 
A sample k8s deployment has been create and the yaml is inside ./deployment/greeting_hkweather.yaml

# To Build python on M1 for x64, require x86_64 python on mac
```
pyinstaller --target-arch x86_64 --onefile target.py
```
