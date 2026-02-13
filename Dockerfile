FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy all files
COPY . ./

# Upgrade pip and install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port
EXPOSE 8080

# Run the app
CMD ["python", "app.py"]
