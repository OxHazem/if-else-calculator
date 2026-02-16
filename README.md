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

