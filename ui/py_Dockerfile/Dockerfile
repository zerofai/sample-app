# Use an official Python runtime as the base image
FROM cgr.dev/chainguard/python:latest

# Set the working directory in the container
WORKDIR /ui

# Copy the requirements file to the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the python code and html to the container
COPY ui.py index.html .

# Copy the static folder and its contents to the container
COPY static static

# Expose the container port
EXPOSE 5000

# Set the entrypoint command
CMD [ "python", "ui.py" ]
