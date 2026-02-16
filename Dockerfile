FROM python:3.12-slim


# Install system dependencies for GUI apps
# Install system dependencies for PySide6 (Qt6)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1 \
    libegl1 \
    libx11-6 \
    libxext6 \
    libxrender1 \
    libsm6 \
    libxkbcommon-x11-0 \
    libxcb1 \
    libxcb-cursor0 \
    libxcb-render0 \
    libxcb-shape0 \
    libxcb-xfixes0 \
    libxcb-randr0 \
    libxcb-keysyms1 \
    libxcb-image0 \
    libxcb-icccm4 \
    libxcb-util1 \
    libdbus-1-3 \
    libglib2.0-0 \
    libfontconfig1 \
    libfreetype6 \
    fonts-dejavu-core \
    && rm -rf /var/lib/apt/lists/*



WORKDIR /app 

COPY requirments.txt .

RUN pip install --no-cache-dir -r requirments.txt

COPY . . 

CMD ["python", "main.py"]

