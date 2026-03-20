#Task A — Truthiness
print("---Task A — Truthiness---\n")

for i in (0, 1, [], [1], "", "hello", None):
    print(f"Value {i} -> True") if i else print(f"Value {i!r}: False")

#Task B — Identity vs Equality
print("\n---Task B — Identity vs Equality---\n")

print("Case 1: equal values but different objects")

a = [1,2,3]
b = [1,2,3]

print(f"a is b: {a is b}")
print(f"a == b: {a == b}")

print("\nCase 2: identical objects")

b = a

print(f"a is b: {a is b}")
print(f"a == b: {a == b}")

print("\nCase 3: behaviour with immutable values")

a = 10
b = 10

print(f"a is b: {a is b}")
print(f"a == b: {a == b}")

#Task C — Control Flow
print("\n---Task C — Control Flow---\n")

def describe_number(x):
   if x < 0: return "Negative"
   elif x == 0: return "Zero"
   elif 0 < x < 10 : return "small positive"
   else: return "large positive"

for i in (-5, 0, 6, 101):
    print(f"{i} -> {describe_number(i)}")

#Task D — Pattern Matching
print("\n---Task D — Pattern Matching---\n")

for i in (("click", 10, 15), ("keypress", "D"), ("quit",)):
    match i:
        case ("click", x, y):
            print(f"click at {x} {y}")
        case ("keypress", key):
            print(f"key pressed: {key}")
        case("quit",):
            print("quit event")
        case _ :
            print("Unknown")

#Task E — Comprehensions
print("\n---Task E — Comprehensions---\n")
sq = [i**2 for i in range(1,21)]
print(sq)

sq2 = [i**2 for i in range(2,21,2)]
print(sq2)

dicsq = {i:i**2 for i in range(1,21)}
print(dicsq)

#Task F — Generators
print("\n---Task F — Generators---\n")

def even_numbers(limit):
    for i in range(0, limit, 2):
        yield i

r = even_numbers(25)

for i in r:
    print(i, end = ", ")

print("\n---Additional requirement---\n")

total_sum = sum(x**2 for x in even_numbers(1000000))
print(total_sum)