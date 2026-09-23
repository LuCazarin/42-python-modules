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
| **[Module 00](./Module_00)** | **Python Basics** | Environment setup, syntax basics, basic control flow, and functions. |
| **[Module 01](./Module_01)** | **Object-Oriented Programming** | Classes, instances, encapsulation, inheritance (`super()`), and method overriding. |
| **[Module 02](./Module_02)** | **Advanced OOP &amp; Error Handling** | Static/Class methods, custom exceptions, decorators, and data validation. |
| **[Module 03](./Module_03)** | **Data Structures** | Lists, dictionaries, sets (`set`), comprehensions, and data transformations. |
| **[Module 04](./Module_04)** | **File I/O &amp; Generators** | Context managers (`with`), file streams, custom generators, and exception handling. |
| **[Module 05](./Module_05)** | **Data Processing &amp; Architecture** | Abstract Base Classes (`ABC`), polymorphic stream processing, and `Protocol` export plugins. |

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

This project is licensed under the [MIT License](LICENSE).

```

---

### 💻 2. Comandos de Terminal para Subir no GitHub (PC da 42)

Como você está no terminal da 42 (`/home/luafranc/python`), execute a sequência de comandos abaixo:

#### **Passo A: Garantir que você está no diretório correto**
```bash
cd /home/luafranc/python

```

#### **Passo B: Criar o arquivo** **.gitignore**

Para evitar subir caches do Python ou pastas temporárias:

```
cat &lt;&lt; 'EOF' &gt; .gitignore
.venv/
env/
venv/
__pycache__/
*.pyc
.mypy_cache/
.pytest_cache/
.DS_Store
.vscode/
