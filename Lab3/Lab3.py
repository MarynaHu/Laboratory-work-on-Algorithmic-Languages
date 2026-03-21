#Task A — Functions as Objects
print("---Task A — Functions as Objects---\n")

def apply_twice(func, x):
    return func(func(x))

def own_function(a):
    return a**2

print(f"Using lambda: {apply_twice(lambda x: x + 1, 3)}")
print(f"Using abs: {apply_twice(abs, -15)}")
print(f"Using own function: {apply_twice(own_function, 4)}")

#Task B — Sorting with Lambda
print("\n---Task B — Sorting with Lambda---\n")

people = [
("Alice", 25),
("Bob", 20),
("Carol", 30),
("Dave", 22)
]

print(f"Sorted by age: {sorted(people, key = lambda x: x[1])}")
print(f"Sorted by name: {sorted(people, key = lambda x: x[0])}")

#Task C — Function Factory
print("\n---Task C — Function Factory---\n")

def make_multiplier(k):
    def multiplier(x):
        return k*x
    return multiplier

times3 = make_multiplier(3)
times5 = make_multiplier(5)

print (times3(10), times3(15))
print (times5(13), times5(15))

#Task D — Closure Counter
print("\n---Task D — Closure Counter---\n")

def counter():
    n = 0
    def inc():
        nonlocal n
        n += 1
        return n
    return inc

c = counter()

for i in range(5):
    print(c())

#Task E — Lambda vs def
print("\n---Task E — Lambda vs def---\n")

def def_squares(x):
    return x**2

lambda_squares = lambda x: x**2

print(f"Def: {def_squares(5)}")
print(f"Lambda: {lambda_squares(5)}")

#Task F — Functional Composition
print("\n---Task F — Functional Composition---\n")

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

result = sum(x**2 for x in filter(lambda x: x % 2 == 0, numbers))
print(result)