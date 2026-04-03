from typing import Callable, TypeVar

#Task A — Basic Type Hints
print("---Task A — Basic Type Hints---\n")

def add(a: int, b: int) -> int:
   return a + b

def square_list(data: list[int]) -> list[int]:
    return [x * x for x in data]

print(f"Example showing that function add works correctly: {add(10, 15)}")
print(f"Example showing that function square_list works correctly: {square_list(list(range(5)))}")

#Task B — Typed Collections
print("\n---Task B — Typed Collections---\n")

def filter_even(data: list[int]) -> list[int]:
    return [x for x in data if x % 2 == 0]

print(f"A small usage example function filter_even with list 0-10: {filter_even(list(range(10)))}")

#Task C — Optiona
print("\n-----Task C — Optiona-----\n")

def find(data: list[int], x: int) -> int | None:
    for i in data:
        if i == x: return i 
    return None

print (f"Example for the case where a value 5 is found in list 0-10: {find(list(range(10)), 5)}")
print (f"Example for the case where a value 42 is not found in list 0-10: {find(list(range(10)), 42)}")

#Task D — Function Type
print("\n-----Task D — Function Type-----\n")

def apply(func: Callable[[int], int], x: int) -> int:
   return func(x)

print("Input data to apply(func, x: int) -> int:\n func = lambda x: x * 2 \n data = 5 \n")
print(f"Entrance: \n {apply((lambda x: x * 2), 5)} \n")

print("Input data to apply(func, x: int) -> int:\n func = abs \n data = -5 \n")
print(f"Entrance: \n {apply(abs, -5)} ")

#Task E — Generics
print("\n-----Task E — Generics-----\n")
T = TypeVar("T")

def first(items: list[T]) -> T:
   return items[0]

print(f"Return the first element in int list: {first([1, 2, 3])}")
print(f"Return the first element in str list: {first(["a", "b", "Allons-y"])}")
print(f"Return the first element in float list: {first([3.14, 2.71, 0.3])}")

#Task F — Function Returning Function
print("\n---Task F — Function Returning Function---\n")

def make_multiplier(k: int) -> Callable[[int], int]:
   return lambda x: x * k

make_multiplier_5 = make_multiplier(5)
print(f"Example showing that the returned function works correctly: {make_multiplier_5(10)}")

#Task G — Pipeline
print("\n-----Task G — Pipeline-----\n")

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
result = sum(x**2 for x in filter(lambda x: x % 2 == 0, numbers))
print(f"""The final result of keeping only even numbers, squaring them, 
      and computing the sum using list({numbers}) is {result}""")