FROM python:3.12

# Create virtual environment
ENV VIRTUAL_ENV=/opt/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install system packages for libxml2, libxslt, and build dependencies
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
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Download the language detection model
RUN pip install fasttext
# Create models directory before downloading the file
RUN mkdir -p /models && \
    wget https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.ftz -O /models/lid.176.ftz



# Copy app code
COPY . .

# Run FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
