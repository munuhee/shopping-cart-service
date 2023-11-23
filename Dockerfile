# Use a Python base image
FROM python:3.9

# Set the working directory within the container
WORKDIR /app

# Copy the application code into the container
COPY . /app

# Install necessary dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the port your Flask app runs on
EXPOSE 5000

# Define environment variables (if needed)
# ENV FLASK_ENV=development
# ENV FLASK_APP=run.py

# Command to run the application
CMD ["python", "run.py"]
