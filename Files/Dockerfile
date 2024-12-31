FROM python:3.10-alpine3.16

# Install necessary dependencies: Docker, Git, and Curl
RUN apk update && \
    apk add --no-cache docker git curl

# Set the working directory to /code
WORKDIR /code

# Copy the requirements file into the container
COPY requirements.txt /code/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r /code/requirements.txt

# Copy the Python script into the Docker container
COPY app.py /code/app.py

# Set the default command to run the Python script
ENTRYPOINT ["python", "/code/app.py"]
