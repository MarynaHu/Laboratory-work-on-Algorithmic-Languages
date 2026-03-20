**Answers 2**

**1)Task A — Truthiness**  
*Why does Python treat empty containers as False?*

Python treats empty containers as False for the sake of conciseness and readability of the code.

**2)Task B — Identity vs Equality**  
*When should \`is\` be used instead of \`==\`?*

\`is\` should be used instead of \`==\` in several cases:  
1\. when you are interested in identity (whether it points to the same object in memory), not value (whether the variables contain the same data)  
2\. For comparison with None

**3)Task C — Control Flow**  
There are no questions

**4)Task D — Pattern Matching**  
*Why is match convenient for analysing structured data?*

1\. Eliminates the need for long, hard-to-read if-elif-else chains with multiple index checks.  
2.Simultaneously checks the structure and extracts the data into variables in a single step  
3\.  It easily matches complex nested structures (lists inside dictionaries, etc.) and allows for type checking directly inside the pattern.

**5)Task E — Comprehensions**  
There are no questions

**6)Task F — Generators**

*1\. What is the difference between a list comprehension and a generator expression?*

A list comprehension computes all values immediately and stores the entire list in memory. A generator expression computes values one at a time on the fly, making it much more memory-efficient for large datasets.

*2\. Why are generators considered lazy?*

Generators are considered "lazy" because they do not compute or store their entire dataset in memory upfront. Instead, they pause execution and generate values one-by-one only on demand (using the yield keyword), which saves significant memory and computational resources

*3\. What happens when a generator finishes execution?*

Once a generator has yielded all its values, it becomes "exhausted." If you try to request another value from it, it raises a StopIteration exception.