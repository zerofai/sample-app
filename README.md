# Greeting HKWeather

A very simple python based microservices contain 3 component:

![image](https://github.com/zerofai/greeting_hkweather/assets/20843048/f3799bea-74aa-4cf5-b1f2-bdf9a83cdc1d)


# UI
A web UI with 2 button
Code and Dockerfile inside ./ui/Dockerfile

# Greeting
A service that will return random greeting phrase and current time
Code and Dockerfile inside ./greeting/Dockerfile

# Weather
A service that will reach out to HKO to get current werather info of Hong Kong
Code and Dockerfile inside ./weather/Dockerfile

# Image
A service that will connect to S3 and get a random image to show
Code and Dockerfile inside ./image/Dockerfile

# To Test locally 
```
export GREETING_HOSTNAME=127.0.0.1:5001
export WEATHER_HOSTNAME=127.0.0.1:5002
```

# To Build the image on M1 for x64
```
docker build --platform linux/amd64 -t imagename .
```

Image has been build and pushed to DockerHub, for image name please refer to below yaml

# Deployment on k8s 
A sample k8s deployment has been create and the yaml is inside ./deployment/greeting_hkweather.yaml
