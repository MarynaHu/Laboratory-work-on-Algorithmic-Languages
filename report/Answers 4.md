**Answers 4**

*1\. What is a higher-order function?* 

A higher-order function is a function that either takes one or more functions as arguments (callbacks) or returns a function as its result. They enable functional programming techniques, allowing for more abstract, reusable, and modular code, such as built-in methods like map() and filter().

*Exemple:*  
def apply(func, data):  
    return \[func(i) for i in data\]

print(apply(lambda x: x \* 2, \[1, 2, 3\]))

*2\. What is the difference between map and list comprehension?* 

The primary difference is that map() returns a lazy iterator (in Python 3), evaluating elements one by one as needed, while a list comprehension produces an eager list in memory right away.

*The main differences:*

| Feature | List Comprehension | map() Function |
| :---- | :---- | :---- |
| Return Type | A new list object | A map object |
| Memory Usage | Higher, as the entire list is built in memory at once | Lower for large datasets, as it generates values on demand |
| Readability | Generally considered more readable and direct for typical Python code	 | Can be concise when using built-in functions, but less so with lambda functions |
| Flexibility | Can easily combine transformations and filtering (if clauses) within a single expression | Primarily for transformations; filtering requires the separate filter() function or conditional logic inside the mapped function |
| Syntax | Declarative, integrated into Python's core loop structure: \[expression for item in iterable\]	 | Functional style, requires passing a function and an iterable as arguments: map(function, iterable) |

*3\. What is a decorator?* 

A decorator is a programming feature that wraps a function, method, or class to extend or modify its behavior without changing its source code.They promote code reusability, clean syntax (Single Responsibility Principle), and allow adding/removing responsibilities dynamically. Allow to cleanly add functionality—like logging, timing, or authorization—in a reusable manner.

*Exemple decorator:*  
def call\_counter(func):  
    x \= 0  
    def wrapper(\*args, \*\*kwargs):  
        nonlocal x  
        x \+= 1  
        print(f"call \#{x}")  
        return func(\*args, \*\*kwargs)  
    return wrapper

@call\_counter  
def a():  
    pass

*4\. What is the difference between a simple decorator and a decorator with arguments?* 

A simple decorator has two levels of nested functions. The outer function takes the target function as its only argument, and the inner function (wrapper) executes it.  
A decorator with arguments requires three levels of nested functions. The outermost function acts as a "factory" that takes the custom arguments, the middle function takes the target function, and the innermost function is the wrapper.

*Exemple decorator with arguments:*  
def prefix(text):  
    def decorator(func):  
        def wrapper(\*args, \*\*kwargs):  
            return text \+ ": " \+ func(\*args, \*\*kwargs)  
        return wrapper  
    return decorator

@prefix("INFO")  
def get\_data():  
 return "data"

*5\. Why is caching useful?*

Caching is an optimization technique that stores the results of expensive, time-consuming function calls in memory (usually in a dictionary). If the function is called again with the exact same arguments, it returns the stored result instantly instead of recalculating it. It trades memory space for processing speed and is crucial for optimizing recursive functions.  
