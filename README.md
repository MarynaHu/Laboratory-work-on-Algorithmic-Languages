## Lab 07 — Behavior, Protocols, ABC, Dataclasses, Slots

In this lab, we explored different ways to define and implement behavior in Python.
We worked with a single concept — an object that can be serialized — and implement it using different 
approaches:
 duck typing (regular class) 
 Protocol (structural typing) 
 dataclass 
 slots 
 Abstract Base Classes (ABC)

The goal is to understand how Python defines “type” through behavior rather than inheritance.

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

The program prints seven sections (A–D), each demonstrating: Regular class (duck typing), Dataclass implementation, Slots, ABC version.  
Detailed explanations for each section and answers to theoretical questions are in the report folder in the answers 7.md file.
