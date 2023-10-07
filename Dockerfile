# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Add current directory code to /app in container
ADD . /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Install application dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Set environment variables
ENV APP_HOST=0.0.0.0
ENV APP_PORT=5000
ENV DB_HOST=localhost
ENV DB_PORT=5432
ENV DB_NAME=cloud_api_security_checker
ENV DB_USER=postgres
ENV DB_PASSWORD=postgres
ENV AWS_ACCESS_KEY_ID=your_aws_access_key_id
ENV AWS_SECRET_ACCESS_KEY=your_aws_secret_access_key
ENV AZURE_SUBSCRIPTION_ID=your_azure_subscription_id
ENV AZURE_CLIENT_ID=your_azure_client_id
ENV AZURE_CLIENT_SECRET=your_azure_client_secret
ENV AZURE_TENANT_ID=your_azure_tenant_id
ENV GCP_PROJECT_ID=your_gcp_project_id
ENV GCP_SERVICE_ACCOUNT_FILE=your_gcp_service_account_file_path
ENV OAUTH2_CLIENT_ID=your_oauth2_client_id
ENV OAUTH2_CLIENT_SECRET=your_oauth2_client_secret
ENV OAUTH2_REDIRECT_URI=your_oauth2_redirect_uri
ENV LOG_LEVEL=INFO

# Expose port 5000 for the app
EXPOSE 5000

# Run the application
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:5000"]
