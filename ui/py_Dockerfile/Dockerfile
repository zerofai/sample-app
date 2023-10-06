# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /ui

# Copy the requirements file to the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the code to the container
COPY ui.py index.html .

# Expose the container port
EXPOSE 5000

# Set the entrypoint command
CMD [ "python", "ui.py" ]
