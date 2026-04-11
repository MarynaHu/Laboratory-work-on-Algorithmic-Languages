## Lab 06: Python Object Model and Basic Object Behavior

In this lab, we implemented our own Python class and gradually transformed it into a well-functional object that integrates with the language.
The goal of this lab is to practice:  

► working with classes and objects  
► understanding how attributes are stored  
► implementing basic dunder methods  
► controlling object behavior in Python  
► writing type-safe code with mypy --strict  

### Python version used
Python 3.14+

### Instructions on how to run the code
Activating a virtual environment via terminal:  
```
python -m venv .venv  
.venv\Scripts\activate  
pip install -r requirements.txt
```
Сommand to run the program:  
```
python .\src\Lab6.py
```
Сommand to type checking
```
mypy --strict src/
```
### Short description of the implemented tasks

The program prints seven sections (A–G), each demonstrating: Define the Student class, Inspect internal structure, Implement `__str__`, Implement `__repr__`, Implement equality (`__eq__`), Implement ordering (`__lt__`), Sorting.  
Detailed explanations for each section and answers to theoretical questions are in the report folder in the answers 6.md file.
