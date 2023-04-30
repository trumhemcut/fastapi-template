# Use the latest stable Python version
FROM python:3.9-slim-buster

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code into the container
COPY . .

# Expose the port on which the GRPC server will listen
EXPOSE 50051

# Start the server
CMD ["python", "app/server.py"]
