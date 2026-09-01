a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")


# print("a is greater than b" if a > b else "a is not greater than b")

# On non-empty string
print(bool("MANUU"))  # Output: True

# On empty string
print(bool(""))  # Output: False

# On whitespace string
print(bool("   "))  # Output: True

# On non-zero number
print(bool(42))  # Output: True

# On zero number
print(bool(0))  # Output: False

list = ["Apple", "Banana", "Cherry"]

# On non-empty list
print(bool(list))  # Output: True

# On empty list
print(bool([]))  # Output: False

# On non-empty tuple
tuple = (1, 2, 3)
print(bool(tuple))  # Output: True

# On empty tuple
tuple = ()
print(bool(tuple))  # Output: False

# On non-empty dictionary
dict = {"name": "Hamza", "age": 72}
print(bool(dict))  # Output: True

# On empty dictionary
dict = {}
print(bool(dict))  # Output: False