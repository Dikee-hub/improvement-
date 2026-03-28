# Calculator API

A modular, production-ready calculator API built with Python and Flask, featuring basic arithmetic, advanced mathematics, statistics, and equation solving capabilities.

## Features

### 1. Basic Operations
- Addition, Subtraction, Multiplication, Division
- Input validation and error handling
- Division by zero protection

### 2. Advanced Mathematics
- Trigonometric functions (sin, cos, tan)
- Logarithmic functions (log, ln)
- Square root calculations
- Power operations

### 3. Statistics
- Mean (average)
- Median
- Standard Deviation
- Variance
- Sum calculations

### 4. Equation Solving
- Linear equations (ax + b = 0)
- Quadratic equations (ax² + bx + c = 0)
- Symbolic equation solver

## Setup & Installation

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/Dikee-hub/improvement-.git
   cd improvement-
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python app.py
   ```

The API will be available at `http://localhost:5000`

## API Documentation

### Basic Operations

#### Addition
```bash
curl -X POST http://localhost:5000/api/basic/add -H "Content-Type: application/json" -d '{"a": 5, "b": 3}'
```

#### Division
```bash
curl -X POST http://localhost:5000/api/basic/divide -H "Content-Type: application/json" -d '{"a": 6, "b": 3}'
```

### Advanced Math

#### Sine
```bash
curl -X POST http://localhost:5000/api/advanced/sin -H "Content-Type: application/json" -d '{"angle": 90}'
```

#### Square Root
```bash
curl -X POST http://localhost:5000/api/advanced/sqrt -H "Content-Type: application/json" -d '{"value": 16}'
```

### Statistics

#### Mean
```bash
curl -X POST http://localhost:5000/api/stats/mean -H "Content-Type: application/json" -d '{"numbers": [1, 2, 3, 4, 5]}'
```

### Equation Solving

#### Linear Equation
```bash
curl -X POST http://localhost:5000/api/solve/linear -H "Content-Type: application/json" -d '{"a": 2, "b": -4}'
```

#### Quadratic Equation
```bash
curl -X POST http://localhost:5000/api/solve/quadratic -H "Content-Type: application/json" -d '{"a": 1, "b": -5, "c": 6}'
```

## Project Structure

```
improvement-/
├── app.py                  # Flask API server
├── basic_operations.py     # Basic arithmetic functions
├── advanced_math.py        # Advanced math functions
├── statistics_calc.py      # Statistical calculations
├── solver.py               # Equation solver
├── requirements.txt        # Project dependencies
└── README.md              # This file
```

## Error Handling

The API provides meaningful error messages for invalid inputs

## License

This project is licensed under the MIT License