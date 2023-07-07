# Dockerfile for the task service
FROM python:3.9-slim-buster

WORKDIR /app

# Copy the necessary files
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "main.py" ]
