# Use an official Python runtime as the base image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /env-print

# Copy the requirements file to the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the python code and html to the container
COPY env-print.py index.html .

# Expose the container port
EXPOSE 8000

# Set the entrypoint command
CMD [ "python", "env-print.py" ]
