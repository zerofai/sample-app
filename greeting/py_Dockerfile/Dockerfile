# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /greeting

# Copy the requirements file to the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the code to the container
COPY greeting.py .

# Expose the container port
EXPOSE 5001

# Set the entrypoint command
CMD [ "python", "greeting.py" ]
