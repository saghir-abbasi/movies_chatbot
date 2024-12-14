# # Use an official Python runtime as the base image
# FROM python:3.12-slim

# # Set the working directory inside the container
# WORKDIR /app

# # Copy the project files into the container
# COPY . /app

# # Install dependencies
# RUN pip install --no-cache-dir -r requirements.txt

# # Expose the port your application runs on
# EXPOSE 8501

# # Set the environment variable for the API key (Optional if set externally)
# # ENV GEMINI_API_KEY=your-api-key

# # Command to run the application
# # Command to run the Streamlit app
# CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]


# ///////
# Use the official Python image
FROM python:3.12-slim

# Install dependencies
RUN apt-get update && apt-get install -y curl git && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Install Python dependencies
COPY . /app/
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]