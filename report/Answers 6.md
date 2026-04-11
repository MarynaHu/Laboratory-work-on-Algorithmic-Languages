**Answers 6**

*1\. What is stored in obj.\_\_dict\_\_?* 

In Python, obj.\_\_dict\_\_ is a dictionary that stores all of an object's instance attributes. Every time you assign a value to self.attribute, it gets recorded in this internal dictionary.   
Keys: The names of the attributes as strings.  
Values: The current data assigned to those attributes.

*An example of using \_\_dict\_\_ can be seen in the code in task B.*

*2\. What is the difference between a class and an object?* 

A class is a blueprint, template, or set of instructions used to create objects, defining their data structure and behavior without occupying memory. An object is a specific, real-world instance of that class that exists in memory, holding actual data.

*Analogy:* A class is a blueprint for a house, and an object is a real house built from the blueprint.

*The main differences:*

| Feature | Class | Object |
| :---- | :---- | :---- |
| Definition | A logical structure that serves as a template for creating entities. | A concrete instance created based on a class template. |
| Purpose | Determines what attributes and methods future objects will have. | Stores real data and performs actions described in the class. |
| Memory | Does not take up memory for data storage). | Takes up space in computer memory while the program is running. |
| Existence | It exists in the code in only one instance (as a type description). | Based on a single class, you can create an infinite number of unique objects. |

*3\. What does \_\_init\_\_ do?* 

The \_\_init\_\_ method is a special method that is automatically called when a new object (instance) of a class is created. Its main role is initialization, that is, setting the initial state of the object by assigning values ​​to its properties (attributes).

*Example \_\_init\_\_:*  
def \_\_init\_\_(self, name:str, group:str, average\_grade: float):  
        self.name \= name  
        self.group \= group  
        self.average\_grade \= average\_grade

*4\. Who calls \_\_str\_\_, and when?* 

The \_\_str\_\_ method is a special "dunder" (double underscore) method in Python that is used to compute an "informal" or user-friendly string representation of an object. Python's internal machinery calls \_\_str\_\_ automatically when an object needs to be converted into a string for human consumption.It is called whenever a human-readable representation is required rather than a developer-focused one. Specifically: User Interface/CLI Output, Logging, Web Frameworks.

*Examples   \_\_str\_\_:*  
def \_\_str\_\_(self) \-\> str:  
        return f"Student: {self.name}  ({self.group}; {self.average\_grade})"

*5\. What is the difference between \== and is?* 

The difference between \== and is primarily concerns how they compare objects.   
The main difference:  
\==: compares values ​​or data stored in objects. Returns True if the contents of the objects are equivalent.  
is: compares the addresses of objects in memory. Returns True only if both variables refer to the same object in memory.

*The main differences:*

| Feature | \== | is |
| :---- | :---- | :---- |
| What it checks | Checks if the values ​​(contents) of the objects are the same. | Checks if the variables point to the same object in memory. |
| Verification mechanism | Calls the \_\_eq\_\_ method | Compares object identifiers (memory addresses). |
| Typical use | When you need to compare data (numbers, strings, lists). | For comparison with singletons (as None) |

*6\. Why do we use other: object in \_\_eq\_\_ and \_\_lt\_\_?* 

Using other: object is a defensive programming practice that ensures type safety and prevents crashes:

*Polymorphism:* It allows the method to accept any object type for comparison.

*Safe Handling:* By accepting an object, we can use isinstance(other, Student) inside the method. If someone tries to compare a Student to a string or a number, the program won't crash; it will simply return False (for \_\_eq\_\_) or raise a meaningful TypeError (for \_\_lt\_\_).  
