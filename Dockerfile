FROM python:3.9-slim-buster

# Set working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY ./requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=app.py

# Run the application
CMD ["flask", "run", "--host", "0.0.0.0"]
