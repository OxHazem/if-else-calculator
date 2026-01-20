

```markdown
# MathSuite – Modular Mathematical Toolkit (Python)

MathSuite is a modular, extensible **desktop-ready mathematical toolkit** built in Python.  
It started as a beginner CLI calculator and evolved into a **professionally structured application** designed for scalability, testing, and GUI integration.

The project covers a wide range of mathematical operations including arithmetic, geometry, trigonometry, algebra, and unit conversions, with a clean separation between **logic** and **user interface**.

---

## 🚀 Features

### 🔢 Arithmetic
- Addition
- Subtraction
- Multiplication
- Division
- Power operations

### 📐 Geometry
**Areas**
- Triangle (Heron's formula)
- Circle, Square, Rectangle
- Cube, Cuboid
- Cylinder, Sphere

**Volumes**
- Cube, Cuboid
- Cylinder, Sphere
- Cone, Pyramid

**Lateral Areas**
- Cone
- Pyramid
- Cube
- Cuboid
- Cylinder

### 📐 Trigonometry
- sin, cos, tan
- sec, csc, cot  
(Implemented using Taylor series approximation)

### 🧮 Algebra
- Quadratic equation solver
- Handles:
  - Linear equations
  - One root, two roots
  - Complex roots
  - Infinite or no-solution cases

### 🔁 Unit Conversions
**Weight**
- Milligrams, Grams, Kilograms, Tons

**Length**
- Millimeters, Centimeters, Meters, Kilometers

---

## 🧱 Project Architecture

The project follows a **clean, modular structure**:

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
└── README.md

````

### Design Principles
- **Separation of concerns**
- **Pure functions** (no input/print inside logic)
- **Reusable modules**
- **GUI-ready architecture**

---

## 🖥️ Current Interface

- Command-Line Interface (CLI)
- Dictionary-based menus
- Robust input validation and error handling

---

## 🎯 Planned Enhancements (Next Versions)

- ✅ Professional **PyQt desktop GUI**
- ✅ Sidebar navigation with multiple pages
- ✅ Dark/Light mode
- ⏳ Graph plotting (quadratic & trigonometry)
- ⏳ Expression parsing (e.g. `3+4*2`)
- ⏳ Unit tests
- ⏳ Packaging as a desktop application

---

## 🛠️ Technologies Used

- Python 3
- Standard Library (`math`)
- PyQt (planned GUI)
- Modular architecture (package-based design)

---

## 📚 What I Learned

- Writing clean, reusable Python functions
- Organizing large projects into modules
- Input validation and error handling
- Mathematical modeling and numerical methods
- Designing software with future GUI integration in mind
- Transitioning from beginner scripts to professional codebases

---

## ▶️ How to Run (CLI Version)

```bash
python main.py
````

---

## 📌 Author

**Omar Hazem Ahmed**

This project represents my progression from beginner-level Python to structured, scalable software design.

---

## ⭐ Why This Project Matters

This project demonstrates:

* Growth mindset
* Clean architecture
* Strong foundations for GUI and advanced features
* Readiness for real-world software development

```
