## LAB05: Type Hints, Generics, Mypy

The goal of this lab is to practice using type hints and to understand how static typing improves code reliability 
and clarity. Demonstrate understanding of:  
► basic type annotations for functions   
► typed collections   
► generics using TypeVar  
► function types   
► functions returning functions   
► static type checking with mypy  
► strict type checking discipline (mypy --strict)   
 

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
python .\src\Lab5.py
```
Сommand to type checking
```
mypy --strict src/
```
### Short description of the implemented tasks

The program prints seven sections (A–G), each demonstrating: Basic Type Hints, Typed Collections, Optional, Function Type, Generics, Function Returning Function, Pipeline.  
Detailed explanations for each section and answers to theoretical questions are in the report folder in the answers 5.md file.
