## Lab 08 — Iteration, Context Managers, and Descriptors

In this lab, we implemented a custom object that integrates with Python through several core protocols.
We worked with a collection of students and extend it step by step so that it:  
   can be used in a for loop (iteration protocol)  
   can be used in a with statement (context manager protocol)  
   validates attribute access (descriptor)  

The goal is to understand that Python behavior is driven by protocols implemented via special methods.

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
python .\src\Lab7.py
```
Сommand to type checking
```
mypy --strict src/
```
### Short description of the implemented tasks

The program prints seven sections (A–D), each demonstrating: Iteration, Context Manager, Descriptor, Integration.  
Detailed explanations for each section and answers to theoretical questions are in the report folder in the answers 8.md file.
