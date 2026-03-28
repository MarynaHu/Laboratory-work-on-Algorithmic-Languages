#Task A — Higher-Order Function
print("---Task A — Higher-Order Function---\n")

def apply(func, data):
    return [func(i) for i in data]

test_func = (lambda x: x * 2)
test_data = [1, 2, 3]

print(f"Input data to apply(func, data):\n func = lambda x: x * 2 \n data = {test_data} \n")
print(f"Entrance: \n {apply(test_func, test_data)} ")

#Task B — map
print("\n-----Task B — map-----\n")

nums = [1,2,3]

print(f"Initial list: {nums}")
print(f"Squaring all numbers in a list: {list(map(lambda x: x**2, nums))}")
print(f"Converting numbers to strings: {list(map(str, nums))}")

#Task C — filter
print("\n-----Task C — filter-----\n")
nums = [5, 10, 15, 20]

print(f"Initial list: {nums}")
print(f"Keeping only even numbers: {list(filter(lambda x: x % 2 == 0, nums))}")
print(f"Keeping numbers greater than 10 : {list(filter(lambda x: x > 10, nums))}")

#Task D — map/filter vs comprehension
print("\n---Task D — map/filter vs comprehension---\n")

nums = list(range(5))
result_1 = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, nums)))
result_2 = [i**2 for i in nums if i % 2 == 0]

print(f"Initial list: {nums}")
print(f"Using map + filter: {result_1}")
print(f"Using list comprehension: {result_2}")

#Task E — Simple Decorator
print("\n---Task E — Simple Decorator---\n")

def call_counter(func):
    x = 0
    def wrapper(*args, **kwargs):
        nonlocal x
        x += 1
        print(f"call #{x}")
        return func(*args, **kwargs)
    return wrapper

@call_counter
def a():
    pass

print("Calls to the a() function:")
print([a() for i in range(5)])

#Task F — Decorator with Arguments
print("\n---Task F — Decorator with Arguments---\n")

def prefix(text):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return text + ": " + func(*args, **kwargs)
        return wrapper
    return decorator

@prefix("INFO")
def get_data():
 return "data"

print("Function output with the addition of the given text \"INFO\": ")
print(get_data())

#Task G — Caching Decorator
print("\n---Task G — Caching Decorator---\n")

def cache(func):
    cached = {}
    def wrapper(n):
        if n in cached:
            return cached[n]
        res = func(n)
        cached[n] = res
        return res
    return wrapper

def staircase_counting(n):
        print("Operation", n)
        if n < 0: return 0
        if n == 0 or n == 1: return 1
        return (staircase_counting(n-1) + 
                staircase_counting(n-2) + 
                staircase_counting(n-3))

print("Staircase counting without caching: ")
print(staircase_counting(5))
print()

staircase_counting = cache(staircase_counting)

print("Staircase counting with caching: ")
print(staircase_counting(5))