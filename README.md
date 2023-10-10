# Greeting HKWeather

A very simple python and GO based microservices contain 4 component:

<img width="1030" alt="Screenshot 2023-10-10 at 09 36 13" src="https://github.com/zerofai/greeting_hkweather_image/assets/20843048/89fe4c44-9450-4847-ad7c-bed568c1cb9c">



# UI
A web UI with 2 button written in python
Code and Dockerfile inside ./ui/py_Dockerfile

# Greeting
A service that will return random greeting phrase and current time written in python
Code and Dockerfile inside ./greeting/py_Dockerfile

# Weather
A service that will reach out to HKO to get current werather info of Hong Kong written in go
Code and Dockerfile inside ./weather/go_Dockerfile
Existing Python version can find in ./weather/py_Dockerfile

# Image
A service that will connect to S3 and get a random image to show, written in python
Code and Dockerfile that tested with minio is inside ./image/py_Dockerfile_minio

# To Test locally 
```
export GREETING_HOSTNAME=127.0.0.1:5001
export WEATHER_HOSTNAME=127.0.0.1:5002
export IMAGE_HOSTNAME=127.0.0.1:5003
```

# To Build the image on M1 for x64
```
docker build --platform linux/amd64 -t imagename .
```

Image has been build and pushed to DockerHub, for image name please refer to below yaml

# Deployment on k8s 
A sample k8s deployment has been create and the yaml is inside ./deployment/greeting_hkweather.yaml
