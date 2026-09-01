print("\n========== Arithmetic Operators ==========")

x = 250
y = 75

print(x + y)  # Output: 325
print(x - y)  # Output: 175
print(x * y)  # Output: 18750
print(x / y)  # Output: 3.3333333333333335
print(x // y)  # Output: 3
print(x % y)  # Output: 25
print(x ** y)  # Output: 250 raised to the power of 75

print("\n========== Assignment Operators ==========")

y += 25
print(y)  # Output: 100
y -= 50
print(y)  # Output: 50
y *= 2
print(y)  # Output: 100
y /= 4
print(y)  # Output: 25.0
y //= 5
print(y)  # Output: 5.0
y %= 3
print(y)  # Output: 2.0
y **= 3
print(y)  # Output: 8.0

print("\n========== Ternary Operators ==========")

# ternary operator
a = 10
b = 20
max_value = a if a > b else b
print(max_value)  # Output: 20

print("\n========== Comparison Operators ==========")

# comparison operators
a = 10; b = 20
print(a == b)  # Output: False
a = 20; b = 20
print(a != b)  # Output: False
a = 15; b = 10
print(a > b)  # Output: True
a = 10; b = 15
print(a < b)  # Output: True
a = 10; b = 10
print(a >= b)  # Output: True
a = 5; b = 10
print(a <= b)  # Output: True

print("\n========== Logical Operators ==========")

# Logical operators
x = 5
print(1 < x < 10)  # Output: True
# noinspection PyChainedComparisons
print(1 < x and x < 10)  # Output: True

print(x < 1 or x < 10)  # Output: True

print(not(x < 1 or x < 10))  # Output: False

print("\n========== Nested Ternary Operator ==========")

# Nested ternary operator
a = 10
b = 20
result = "a is greater" if a > b else "b is greater" if b > a else "a and b are equal"
print(result)  # Output: b is greater

print("\n========== Identity Operators ==========")

# Identity operators
x = ["Apple", "Banana", "Cherry"]
y = ["Apple", "Banana", "Cherry"]
z = x
print(x is z)  # Output: True
print(x is y)  # Output: False
print(x is not y)  # Output: True
print(x is not z)  # Output: False
print(x == y)  # Output: True
print(x == z)  # Output: True

print("\n========== Membership Operators ==========")

# Membership operators
x = ["Apple", "Banana", "Cherry"]
print("Banana" in x)  # Output: True
print("Mango" not in x)  # Output: True
print("Banana" not in x)  # Output: False
print("Mango" in x)  # Output: False

text = "Hello, I am a student of MANUU, and MANUU is in Gachibowli."
name = "Hamza"

if name in text:
    print(f"{name} is present in the text.")
else:
    print(f"{name} is not present in the text.")

print("MANUU is present in the text."
      if "MANUU" in text
      else "MANUU is not present in the text.")  # Output: MANUU is present in the text.

print("\n========== Bitwise Operators ==========")

print(6 & 3)  # Output: 2
print(6 | 3)  # Output: 7
print(6 ^ 4)  # Output: 2
print(~3)  # Output: -4
print(6 << 1)  # Output: 12
print(6 >> 1)  # Output: 3

print(3 << 2)  # Output: 12
print(7 >> 2)  # Output: 1
