FROM python:3.11-slim

WORKDIR /app

# Install CPU-only torch first (avoids pulling the large CUDA build)
RUN pip install --no-cache-dir \
    torch==2.9.0 \
    torchvision==0.24.0 \
    --index-url https://download.pytorch.org/whl/cpu

# Install remaining dependencies
RUN pip install --no-cache-dir flask==3.1.2 Pillow==10.0.1

# Copy app files
COPY app.py .
COPY plastic_classifier.pth .
COPY templates/ templates/

EXPOSE 5000

CMD ["python", "app.py"]
