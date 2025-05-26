FROM python:3.11-slim

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY streamlit_app.py .
COPY run_streamlit.py .

# Expose the Streamlit port
EXPOSE 8501

# Set environment variables
ENV API_BASE_URL="http://localhost:8000"

# Copy the entrypoint script
COPY docker_entrypoint.py .
RUN chmod +x docker_entrypoint.py

# Use the entrypoint script to start Streamlit
CMD ["python", "docker_entrypoint.py"]
