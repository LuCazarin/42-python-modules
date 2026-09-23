# 42 - Python Modules 🐍
42 School Python Piscine &amp;amp; Modules (00 to 10). Data structures, OOP, design patterns, and clean code.

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![Code Style: flake8](https://img.shields.io/badge/code%20style-flake8-green.svg)](https://flake8.pycqa.org/)
[![Type Checking: mypy](https://img.shields.io/badge/type%20checking-mypy%20--strict-brightgreen.svg)](https://mypy.readthedocs.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Solutions for the **Python Curriculum** at **42 School**. This repository contains projects covering fundamental Python programming, object-oriented design, type safety, functional programming, and clean code principles.

---

## 🎯 Repository Standards

All modules strictly adhere to the 42 School evaluation requirements:
* **Strict Static Type Checking**: 100% compliant with `mypy --strict .` without warnings or suppressions.
* **Code Style &amp; Linting**: Fully aligned with PEP 8 standards verified via `flake8 .`.
* **Clean Architecture**: Strong focus on OOP principles, encapsulation, polymorphism, abstract base classes (`ABC`), and protocols (`Protocol` for Duck Typing).

---

## 📂 Modules Overview

| Module | Topic | Key Concepts |
| :--- | :--- | :--- |
| **[Module 00](./Module_00)** | **Python Fundamentals** | Environment setup, syntax basics, expressions, control flow, and simple functions. |
| **[Module 01](./Module_01)** | **Object-Oriented Systems** | Classes, instances, encapsulation, inheritance (`super()`), and method overriding. |
| **[Module 02](./Module_02)** | **Data Resiliency &amp; Exceptions** | Resilient pipelines, custom exceptions, `try`/`except`/`finally` blocks, and data validation. |
| **[Module 03](./Module_03)** | **Collections &amp; Data Structures** | Lists, dictionaries, sets (`set`), tuples, comprehensions, and generators. |
| **[Module 04](./Module_04)** | **File I/O &amp; Stream Management** | Context managers (`with`), file streams, and standard streams (`sys.stdin`, `sys.stdout`, `sys.stderr`). |
| **[Module 05](./Module_05)** | **Polymorphic Data Streams** | Abstract Base Classes (`ABC`), polymorphic streams, `Protocol` (Duck Typing), and export plugins. |
| **[Module 06](./Module_06)** | **Import Mysteries &amp; Packages** | Package initialization (`__init__.py`), import pathways, absolute vs relative imports, and circular dependencies. |
| **[Module 07](./Module_07)** | **Design Patterns &amp; Architecture** | Abstract factories, card architecture, capability mixins, and strategy patterns. |
| **[Module 08](./Module_08)** | **Virtual Environments &amp; Data Tools** | Virtual environments (`venv`), dependency managers (`pip`, Poetry), `.env` handling, and data analysis (`pandas`, `numpy`, `matplotlib`). |
| **[Module 09](./Module_09)** | **Pydantic Models &amp; Validation** | Pydantic v2 schemas (`BaseModel`), field constraints (`Field`), `@model_validator` decorators, and nested models. |
| **[Module 10](./Module_10)** | **Functional Programming** | Anonymous functions (`lambda`), higher-order functions (`Callable`), closures, `functools` (`reduce`, `lru_cache`), and custom decorators. |

---

## 🚀 How to Run

### 1. Prerequisites
Ensure you have Python 3.10+ installed along with `flake8` and `mypy`:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install flake8 mypy

```

### 2\. Running an Exercise &amp; Linter Verification

Navigate to any exercise folder and execute:

```
# Example: Module 05 - Exercise 2
cd Module_05/ex2
python3 data_pipeline.py

# Run Linters and Type Checkers
flake8 .
mypy --strict .

```

---

## 📜 License

This project is licensed under the [MIT License](LICENSE). EOF

---

