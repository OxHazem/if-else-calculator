# MathSuite – Modular Mathematical Toolkit (Python)

MathSuite is a modular and extensible desktop-ready mathematical toolkit built in Python. It began as a beginner command-line calculator and evolved into a professionally structured application designed for scalability, maintainability, testing, and GUI integration.

The project covers arithmetic, geometry, trigonometry, algebra, and unit conversions, with a strict separation between logic and interface layers.

---

## Features

### Arithmetic

* Addition
* Subtraction
* Multiplication
* Division
* Power operations

---

### Geometry

#### Areas

* Triangle (Heron’s formula)
* Circle
* Square
* Rectangle
* Cube
* Cuboid
* Cylinder
* Sphere

#### Volumes

* Cube
* Cuboid
* Cylinder
* Sphere
* Cone
* Pyramid

#### Lateral Areas

* Cone
* Pyramid
* Cube
* Cuboid
* Cylinder

---

### Trigonometry

* sin
* cos
* tan
* sec
* csc
* cot

Implemented using Taylor series approximation.

---

### Algebra

* Quadratic equation solver

Handles:

* Linear equations
* One real root
* Two real roots
* Complex roots
* Infinite solutions
* No-solution cases

---

### Unit Conversions

#### Weight

* Milligrams
* Grams
* Kilograms
* Tons

#### Length

* Millimeters
* Centimeters
* Meters
* Kilometers

---

## Project Architecture

The project follows a clean, modular, and GUI-ready structure:

```
math_cli/
│
├── main.py
│
├── arithmetic/
│   └── basic.py
│
├── geometry/
│   ├── areas.py
│   ├── volumes.py
│   └── lateral_areas.py
│
├── trigonometry/
│   └── trig.py
│
├── algebra/
│   └── quadratic.py
│
├── conversions/
│   ├── length.py
│   └── weight.py
│
├── utils/
│   ├── validators.py
│   └── input_handler.py
│
├── GUI/
│   ├── code/
│   │   ├── main.py
│   │   ├── pages/
│   │   └── components/
│   │
│   ├── UI/
│   │   └── .ui files (Qt Designer)
│   │
│   └── style/
│       └── .qss stylesheets
│
└── README.md
```

### Architecture Principles

* Separation of concerns
* Pure logic functions (no input/output inside core modules)
* Reusable mathematical modules
* Independent GUI layer
* Scalable folder organization

The mathematical engine is completely independent from the interface layer, allowing the same logic to power both the CLI and the desktop GUI without duplication.

---

## Interfaces

### Command-Line Interface (CLI)

Run from the project root:

```bash
python main.py
```

---

### Desktop GUI (PyQt)

Run from the project root:

```bash
python -m GUI.code.main
```

The GUI version includes:

* Sidebar navigation
* Multi-page structure
* External stylesheet support
* Structured page-based design

---

## Docker Support

MathSuite can be executed inside a Docker container for environment isolation and reproducibility.

### Build Docker Image

From the project root:

```bash
docker build -t mathsuite:latest .
```

---

### Run CLI via Docker

```bash
docker run --rm -it mathsuite:latest python main.py
```

* `--rm` automatically removes the container after exit
* `-it` enables interactive terminal mode

---

### Run Desktop GUI via Docker (Linux – X11)

Allow Docker to access your display:

```bash
xhost +local:docker
```

Then run:

```bash
docker run --rm -it \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  mathsuite:latest \
  python -m GUI.code.main
```

Explanation:

* `-e DISPLAY=$DISPLAY` connects the container to the host display
* `-v /tmp/.X11-unix:/tmp/.X11-unix` shares the X11 socket
* `--rm` prevents accumulation of stopped containers

> Note: GUI execution via Docker is supported on Linux systems using X11.


### Running the GUI Docker Container on Windows and macOS

This project runs a PySide6 GUI application inside Docker.

Because Docker containers do not include a display server, the container must connect to the host operating system’s display system.

The instructions below describe the correct setup for:

* Windows 11 (WSLg – recommended)
* Windows 10 (VcXsrv)
* macOS (XQuartz)

These steps assume the provided Dockerfile is used without modification.

---

# Windows 11 (Recommended – WSLg)

This is the recommended and officially supported method.

Uses:

* Windows Subsystem for Linux
* WSLg

## Requirements

1. Windows 11
2. WSL2 installed
3. Docker Desktop configured to use the WSL2 backend

Verify WSL installation:

```powershell
wsl --status
```

If WSL is not installed:

```powershell
wsl --install
```

Restart the system after installation.

---

## Step 1 — Build the Docker Image

Open a WSL terminal and run:

```bash
docker build -t mathsuite-gui .
```

---

## Step 2 — Run the Container

```bash
docker run -it \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  mathsuite-gui
```

The application window should appear as a native Windows window.

No additional configuration is required.

---

# Windows 10 (Using VcXsrv)

For Windows 10, install:

* VcXsrv

## Step 1 — Install and Start VcXsrv

1. Install VcXsrv.
2. Launch **XLaunch**.
3. Choose:

   * Multiple windows
   * Start no client
   * Disable access control (for development only)
4. Finish the setup.

Keep VcXsrv running.

Ensure Windows Firewall allows VcXsrv when prompted.

---

## Step 2 — Build the Docker Image

In PowerShell:

```powershell
docker build -t mathsuite-gui .
```

---

## Step 3 — Run the Container

```powershell
docker run -it `
  -e DISPLAY=host.docker.internal:0.0 `
  mathsuite-gui
```

Note: Use the backtick (`) for multiline commands in PowerShell.

If the GUI does not appear:

* Confirm VcXsrv is running.
* Confirm firewall access is allowed.
* Ensure "Disable access control" was selected.

---

# macOS (Using XQuartz)

macOS requires:

* XQuartz

## Step 1 — Install and Configure XQuartz

1. Install XQuartz.
2. Open XQuartz.
3. Navigate to:

   ```
   XQuartz → Settings → Security
   ```
4. Enable:

   ```
   Allow connections from network clients
   ```
5. Restart XQuartz.

---

## Step 2 — Allow Local Connections

In macOS Terminal:

```bash
xhost + 127.0.0.1
```

---

## Step 3 — Build the Docker Image

```bash
docker build -t mathsuite-gui .
```

---

## Step 4 — Run the Container

```bash
docker run -it \
  -e DISPLAY=host.docker.internal:0 \
  mathsuite-gui
```

The GUI window should appear on macOS.

---

# Optional: Verify OpenGL Support

If your application uses OpenGL, you can test inside the container:

```bash
glxinfo | grep OpenGL
```

If needed, install `mesa-utils` in the Dockerfile:

```dockerfile
RUN apt-get update && apt-get install -y mesa-utils
```

---

# Managing the Container

Stop the container:

```bash
CTRL + C
```

Or from another terminal:

```bash
docker ps
docker stop <container_id>
```

Remove the container:

```bash
docker rm <container_id>
```

---

# Summary

| Operating System | Method  | Additional Software Required |
| ---------------- | ------- | ---------------------------- |
| Windows 11       | WSLg    | None                         |
| Windows 10       | VcXsrv  | VcXsrv                       |
| macOS            | XQuartz | XQuartz                      |

---

# Security Considerations

These configurations are intended for local development only.

* VcXsrv with disabled access control is not secure for public exposure.
* XQuartz network connections should not be exposed externally.
* Do not expose display ports to public networks without authentication.

---

If needed, a separate section can be added for:

* Native Linux support
* Cross-platform noVNC setup
* Production-ready VNC-based Docker configuration


---

## Technologies Used

* Python 3
* Python Standard Library
* PyQt
* Qt Designer
* QSS for styling
* Docker
* Modular package-based architecture

---

## Author

Omar Hazem Ahmed

This project represents the transition from beginner scripts to structured, scalable, and GUI-integrated software design, combining clean architecture principles with containerized deployment practices.

