**Answers 7**

*1\. What is duck typing?*   
   Duck typing is a dynamic typing concept that determines the type or suitability of an object not by its descendant class, but by the presence of certain methods or attributes. That is, a function can accept any object, as long as it can perform the desired action.   
   The name comes from the phrase: "If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck."

**Limitations / Failure cases:**

* Runtime Errors: If the object lacks a required method, the program will crash with an AttributeError error directly during code execution, not at the compilation or writing stage.  
* Lack of developer hints unless typing is used.

*2\. How does Protocol differ from ABC?* 

  Both tools are used to create interfaces, but they work fundamentally differently.  
  ABC uses nominal typing. To conform to an interface, a class must explicitly inherit from ABC.  
  Protocol uses structural typing. This is the static equivalent of duck typing. A class does not need to inherit from anyone. A static analyzer (like mypy) simply checks whether the structure of the class matches the Protocol.

*The main differences:*

| Feature | Protocol | ABC (Abstract Base Class) |
| :---- | :---- | :---- |
| Subtyping | Structural ("Duck Typing") | Nominal (Explicit inheritance) |
| Relationship	 | "Has a" (shape) | "Is a" (hierarchy) |
| Checking | Mostly Static (Type Checkers) | Runtime (and Static) |
| Inheritance | Not necessary	 | Required |
| Code Reuse | No (mostly interface) | Yes (can have base methods) |
| Best For | Loosely coupled code/3rd party | Strict hierarchy/shared logic |
| Limitations / Failure cases | By default, it is checked only statically. At runtime, it will not prevent passing an invalid object.  (The exception is using @runtime\_checkable, but that only checks for the existence of the method, not its arguments.) | Requires a rigid hierarchy. You can't easily force a class from a third-party library to conform to your ABC because you can't change its code to add inheritance. |

*3\. Does Protocol require inheritance? Why or why not?*

No, Protocol does not require inheritance.  
After all, Protocol was created specifically to describe an interface for "duck typing", where the form of the object is important, not its lineage. This allows you to write flexible code and create interfaces for classes that already exist or are imported from third-party libraries, without having to rewrite them.

**Limitations / Failure cases**:

* Accidental compliance: Since there is no inheritance, an object may accidentally conform to a protocol simply because of matching method names, even though logically it does something completely different.

*4\. What problem does ABC solve?*  

ABC (Abstract Base Classes) solves the problem of guaranteed implementation of an interface. It creates a strict contract. If the inheriting class does not implement all the methods marked with @abstractmethod, Python will not physically allow the creation of an object of that class.

**Limitations / Failure cases:**

* Instantiation Error: The main "failure case" is TypeError: Can't instantiate abstract class with abstract method. If the developer forgot to write the serialize() method, the program will crash immediately when trying to create the object student \= StudentABC().  
* Tight Coupling: Code becomes less flexible because classes are tightly coupled to their abstract parents.

*5\. What does @dataclass generate automatically?*

The @dataclass decorator automatically generates several special "dunder" methods to handle the template code of classes that primarily store data. 

By default, the following methods are added: \_\_init\_\_(), \_\_repr\_\_(), \_\_eq\_\_()

You can also trigger the generation of additional methods by passing parameters to the decorator.

**Limitations / Failure cases:**

* Mutable Default Arguments: If you try to give a field a mutable default value (e.g. items: list \= \[\]), Python will throw a ValueError. This is to avoid the error of all instances of a class sharing the same list. You should use *field(default\_factory=list)*.  
* Complex or non-standard initialization logic requires additional effort (using the \_\_post\_init\_\_ method).

*6\. What changes when using slots?* 

When you use slots=True (or manually define \_\_slots\_\_), Python stops using the dynamic dictionary \_\_dict\_\_ to store the attributes of an object. Instead, it allocates a fixed amount of memory only for the attributes you explicitly specify.  
This saves a lot of RAM and makes accessing attributes a little faster.

**Limitations / Failure cases:**

* Restricted Structure: The object loses its dynamic nature. Attempting to add a new attribute at runtime will result in an AttributeError.  
* Multiple Inheritance: Using slots makes multiple inheritance very difficult. If multiple parent classes have their own non-empty slots, you will get TypeError: multiple bases have instance lay-out conflict.

*7\. Why does Protocol work with different implementations (regular class, dataclass, slots)?*

Protocol works with different implementations because it enforces structural subtyping (static "duck typing"), not inheritance. It checks if a class has the required methods/attributes at type-checking time, regardless of whether they are defined via \_\_dict\_\_, \_\_slots\_\_, or generated by @dataclass, enabling compatibility across varying implementation strategies. 

*Protocol works with different implementations:*

* Structural Compatibility (Duck Typing): Protocol focuses on whether a class has the required methods (speak(), etc.), not how they are implemented or which class they inherit from.  
* Dataclasses: They generate methods (\_\_init\_\_, \_\_repr\_\_) at runtime. Because Protocol is often checked by static analyzers (like mypy) or at runtime, it only cares that the methods exist.  
* slots: Slots optimize memory by avoiding \_\_dict\_\_. Protocol checks for the existence of the attribute, which is still possible, even if it is stored in a fixed-size array. 

This means a Protocol for a Callable can be satisfied by a regular class method, a dataclass field, or a slot-based class method without any of them needing to inherit from the protocol itself.

**Limitations / Failure cases:**

If a dataclass or slot class changes the method name for some reason (e.g. to to\_json()) or changes the argument/return types, Protocol will reject that class during mypy validation, no matter how beautifully written the internal code of the class is.