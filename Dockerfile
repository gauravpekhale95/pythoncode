# installing the latest version of Python
FROM python:3.12-slim
# Set the working directory
WORKDIR /app

ARG Env
# Copy the requirements file into the container : # Copy all files from the current directory to the container
COPY . . 

RUN echo "Environment: $Env"
# Install the required packages
RUN pip install --no-cache-dir -r req.txt

# Expose the port the app runs on
EXPOSE 8000

# run the application using uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

