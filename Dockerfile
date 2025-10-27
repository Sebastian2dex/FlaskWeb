FROM python:3.10-slim

# Select the working directory
WORKDIR /app

# Copy the project files to the docker container
COPY . /app

# Flask installation in this casw
RUN pip install --no-cache-dir -r requirements.txt

# Runs of port 8080 (same as the app's running port)
EXPOSE 8080

# Run the app
CMD ["python", "app.py"]