# Use an official Python runtime as the base image
FROM cgr.dev/chainguard/python:latest

# Set the working directory in the container
WORKDIR /weather

# Copy the requirements file to the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the code to the container
COPY weather.py .

# Expose the container port
EXPOSE 5002

# Set the entrypoint command
CMD [ "python", "weather.py" ]
