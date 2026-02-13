Here is the updated version with the GUI folder added clearly inside the project architecture section, written in a clean and natural way.

---

# MathSuite – Modular Mathematical Toolkit (Python)

MathSuite is a modular and extensible desktop-ready mathematical toolkit built in Python. It began as a beginner command-line calculator and gradually evolved into a professionally structured application designed for scalability, maintainability, testing, and GUI integration.

The project covers arithmetic, geometry, trigonometry, algebra, and unit conversions, with a clear separation between logic and user interface layers.

---

## Features

### Arithmetic

* Addition
* Subtraction
* Multiplication
* Division
* Power operations

### Geometry

**Areas**

* Triangle (Heron’s formula)
* Circle
* Square
* Rectangle
* Cube
* Cuboid
* Cylinder
* Sphere

**Volumes**

* Cube
* Cuboid
* Cylinder
* Sphere
* Cone
* Pyramid

**Lateral Areas**

* Cone
* Pyramid
* Cube
* Cuboid
* Cylinder

### Trigonometry

* sin
* cos
* tan
* sec
* csc
* cot

Implemented using Taylor series approximation.

### Algebra

* Quadratic equation solver

Handles:

* Linear equations
* One real root
* Two real roots
* Complex roots
* Infinite solutions
* No-solution cases

### Unit Conversions

**Weight**

* Milligrams
* Grams
* Kilograms
* Tons

**Length**

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

The mathematical engine is completely independent from the interface layer, which allows the same logic to power both the CLI and the PyQt desktop GUI without duplication.

---

## Interfaces

### Command-Line Interface (CLI)

Run from the project root:

```
python main.py
```

### Desktop GUI (PyQt)

Run from the project root:

```
python -m GUI.code.main
```

The GUI version includes:

* Sidebar navigation
* Multi-page structure
* External stylesheet support
* Structured page-based design

---

## Technologies Used

* Python 3
* Python Standard Library
* PyQt
* Qt Designer
* QSS for styling
* Modular package-based architecture

---

## Author

Omar Hazem Ahmed

This project represents the transition from beginner scripts to structured, scalable, and GUI-integrated software design.
