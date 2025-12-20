# Use lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy reqirements first (better caching)
Copy requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY api/ api/
COPY src/ src/
COPY models/ models/

# Expose API port
EXPOSE 8000

# Start FastAPI server
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
