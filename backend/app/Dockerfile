# Use Python 3.12 slim image
FROM python:3.12-slim

# Set environment variables
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install system packages
RUN apt-get update && apt-get install -y \
    build-essential \
    libxml2-dev \
    libxslt1-dev \
    libz-dev \
    libjpeg-dev \
    libpng-dev \
    libpoppler-cpp-dev \
    tesseract-ocr \
    pkg-config \
    git \
    curl \
    wget \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Create working directory
WORKDIR /app

# Create Python virtual environment
RUN python -m venv $VIRTUAL_ENV

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip \
   && pip install --no-cache-dir -r requirements.txt

# Copy your application code
COPY . .

# Expose your FastAPI port
EXPOSE 8001

# Run the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
