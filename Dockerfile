
# Use the official Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the required files to the container's working directory
COPY requirements.txt .
COPY app.py .
COPY templates templates
COPY static static
COPY diabetes_model.pkl .

# Install dependencies
RUN apt-get update &&\
    apt-get install -y gcc &&\
    # Install pip dependencies
    pip install --no-cache --dirr requirements.txt

# Expose the port where the Flask app will run
EXPOSE 5000

# Set the environment variable for Flask to run in production mode
ENV FLASK_ENV=production

# Start the Flask app when the container starts
CMD ["python", "app.py"]
