# 🐍 Ideoversity Python Course

Welcome to the **Ideoversity Python Course** repository! This repository contains a curated collection of Python practice files, moving systematically from basic concepts up to intermediate level topics like functions, loops, conditions, and operations.

Each file is fully commented, self-contained, and serves as an excellent reference for learning Python programming.

---

## 📂 Project Directory Structure

Here is a breakdown of the files in this repository:

| File Name | Primary Topics | Description |
| :--- | :--- | :--- |
| **`#1 Hello World.py`** | Basics, Prints, Operations | Introduction to print statement, basic arithmetic operations, variables, type checking, string replication, and concatenation. |
| **`#2 Variable and Datatype.py`** | Variables, Datatypes, Collections, Formulas | Exploring Python datatypes, string length, collections (Lists, Tuples, Dictionaries), percentage/area formulas, and a basic calculator. |
| **`#3 Conditional Statements And Loop.py`** | Control Flow, Loops, Typecasting | `if-else` logic, `for` loops, `while` loops, nested loops (patterns), `break`/`continue`, password verification, and guessing games. |
| **`#4 Oprators in python.py`** | Operators, Logical Conditions | Arithmetic, Comparison, Assignment, Compound Assignment, and Logical (`and`, `or`, `not`) operators, with practical scenarios like a leap year checker. |
| **`#5 Function.py`** | Functions, Scopes, Arguments, Return | Writing reusable code blocks. Parameters, default arguments, return statements, and apps like BMI, Age, and Triangle Area calculators, plus prime checking. |
| **`#6 Array.py`** | Lists, List Methods, Membership | Understanding lists (arrays) in Python. Indexing, modifications (`append`, `insert`, `remove`, `pop`), checking membership (`in`), and calculating sum. |
| **`#7 OOP.Ipynb`** | OOP, Classes, Objects, Inheritance | Object-Oriented Programming (OOP) concepts, defining parent/child classes, methods, attributes, and inheritance. |
| **`08-a-PyPi.ipynb.ipynb`** | PyPI Packages, Time, Text-to-Speech | Installing and utilizing third-party libraries: `pyjokes` for generating jokes, `spepy` for offline text-to-speech, and `moment` for datetime formatting. |
| **`09-a-chatbot-vs-aiagent-Langgraph.ipynb`** | Gemini SDK, Chatbots, Agents, LangGraph | Developing AI Chatbots and Agents using the new `google-genai` SDK and LangGraph. |
| **`speak.vbs`** | VBScript, Text-to-Speech (SAPI) | A simple standalone Windows VBScript file that plays text-to-speech utilizing `sapi.spvoice`. |

---

## 📝 Detailed Overview of Topics Covered

### 1️⃣ Hello World & Basic Arithmetic
* **Printing Output**: Using `print()` to write text to console.
* **Basic Math**: Addition (`+`), subtraction (`-`), multiplication (`*`), division (`/`), exponentiation (`**`), and modulus (`%`).
* **Variables & Type Checking**: Storing values in variables and checking their types using `type()`.
* **String Operations**: String replication (`"ha" * 5`) and concatenation (`+`).

### 2️⃣ Variables, Datatypes & Collections
* **Standard Datatypes**: 
  * `int` (e.g., age, salary)
  * `float` (e.g., price, percentage)
  * `complex` (e.g., complex numbers like `5 + 6j`)
  * `str` (e.g., names, strings)
* **String Operations**: Checking string length using `len()`, string indexing (accessing characters by position), and iterating through characters using a `for` loop.
* **Python Collections**:
  * **Lists**: Declaring and printing nested and simple lists.
  * **Tuples**: Working with ordered, immutable collections.
  * **Dictionaries**: Key-value pairs representing mapped data (e.g. user details).
* **Applied Math & Calculator**:
  * **Percentage Calculation**: Formula-based percentage calculator.
  * **Triangle Area Calculation**: Base and height area calculator.
  * **Basic Arithmetic Calculator**: Displaying values of mathematical operations for user values.

### 3️⃣ Control Flow & Loop Iterations
* **Conditional Statements**: `if`, `elif`, and `else` branches. Used for checking voting eligibility and fee discount grades.
* **For Loops**: Range-based loops `range(start, stop, step)` to generate sequences, even numbers, and print patterns.
* **While Loops**: Running a block of code until a condition is met (e.g., verifying user passwords or calculating mathematical sums).
* **Loop Control**: Using `break` to exit loops prematurely and `continue` to skip specific iterations.
* **Nested Loops**: Generating right-angled triangle star (`*`) patterns.

### 4️⃣ Operators in Python
* **Comparison Operators**: Evaluates operands and returns boolean (`>`, `<`, `==`, `!=`, `>=`, `<=`).
* **Compound Assignment**: Modifying variables in-place (`+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`).
* **Logical Operators**: Combining conditions using `and`, `or`, and `not`.
* **Real-world Practice Code**: 
  * Checking if a year is a Leap Year.
  * Checking eligibility criteria using combined conditions.
  * Building boolean switches using `not`.

### 5️⃣ Python Functions (Reusability)
* **Defining & Calling**: Defining reusable logic with the `def` keyword.
* **Arguments & Parameters**: Passing variables into functions dynamically.
* **Default Arguments**: Providing default values (e.g., `greeting="Hello"`).
* **Return Statement**: Retrieving output from a function for further calculation.
* **Real-world Applications Included**:
  * **BMI (Body Mass Index) Calculator**: Categorizes weight levels based on weight and height inputs.
  * **Age Calculator**: Calculates age dynamically using year of birth.
  * **Triangle Area Function**: Calculates area using base and height inputs.
  * **Prime Number Checker**: Function returning boolean if a number is prime.
  * **Percentage Calculator**: Function returning the calculated percentage.

### 6️⃣ Arrays & Lists (Python Lists)
* **List Basics & Indexing**: Creating lists, accessing elements using 0-based index.
* **Strings as Arrays**: Accessing string characters by their index position.
* **List Manipulation Methods**:
  * `append(value)`: Add elements to the end of a list.
  * `insert(index, value)`: Insert elements at specific positions.
  * `remove(value)`: Remove the first occurrence of a specific value.
  * `pop(index)`: Remove and return an element at a given index (or the last element if no index is provided).
* **Accumulating Values in Loops**: Collecting multiple user inputs into a list and calculating sum using `sum()`.
* **Membership Testing (`in` / `not in`)**: Checking if an element exists in a list to check category membership (e.g. checking students and employees lists).

### 7️⃣ Object-Oriented Programming (OOP)
* **Classes & Objects**: Defining blueprints using `class` and instantiating them.
* **Inheritance**: Creating child classes (`Child`) that inherit properties and methods from parent classes (`Parent`).
* **Attributes & Methods**: Storing state inside `self` and defining object actions.

### 8️⃣ Working with PyPI Packages
* **Package Management**: Using `%pip install <package>` within Jupyter Notebooks to extend functionality.
* **Random Jokes**: Integrating the `pyjokes` library to retrieve developer jokes.
* **Text-to-Speech**: Utilizing the `spepy` library to convert text strings to voice output offline.
* **Date & Time Formatting**: Using `moment` to parse, format, and display timestamps.

### 9️⃣ AI Chatbots & Agents (Gemini & LangGraph)
* **Google GenAI SDK**: Integrating the new `google-genai` SDK to initialize and communicate with Gemini models.
* **Content Generation**: Generating text dynamically using `client.models.generate_content`.
* **Chatbots vs Agents**: Structuring conversation loops and building multi-turn logic with LangGraph.

---

## 🚀 How to Run the Files Locally

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/HammadSadique786/Ideoversity_Python_Course.git
   cd Ideoversity_Python_Course
   ```

2. **Run Python files or Jupyter Notebooks**:
   * For standard Python scripts:
     ```bash
     python "#1 Hello World.py"
     ```
   * For notebooks (`.ipynb`), make sure your Jupyter kernel is set to the `.venv` virtual environment and run them via VS Code or Jupyter Lab.

---
Happy Coding! 🚀
