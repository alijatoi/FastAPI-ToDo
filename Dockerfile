# Use a lightweight Python image
FROM python:3.10-slim

# Set the working directory inside the Docker container
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install the dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your FastAPI application code to the working directory
COPY . .

# Expose port 8000 to the outside world
EXPOSE 8000

# Command to run the FastAPI app with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
