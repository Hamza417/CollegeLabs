"""
Write statements that demonstrate the use of various operators and their precedence.
"""

# Arithmetic Operators
a = 10
b = 5
print("Arithmetic Operators:")
print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Floor Division: {a} // {b} = {a // b}")
print(f"Modulus: {a} % {b} = {a % b}")
print(f"Exponentiation: {a} ** {b} = {a ** b}")

# Comparison Operators
print("\nComparison Operators:")
print(f"{a} == {b}: {a == b}")
print(f"{a} != {b}: {a != b}")
print(f"{a} > {b}: {a > b}")
print(f"{a} < {b}: {a < b}")
print(f"{a} >= {b}: {a >= b}")
print(f"{a} <= {b}: {a <= b}")

# Logical Operators
print("\nLogical Operators:")
x = True
y = False
print(f"{x} and {y}: {x and y}")
print(f"{x} or {y}: {x or y}")
print(f"not {x}: {not x}")

# Bitwise Operators
print("\nBitwise Operators:")
c = 6  # 110 in binary
d = 3  # 011 in binary
print(f"{c} & {d}: {c & d} (Bitwise AND)")
print(f"{c} | {d}: {c | d} (Bitwise OR)")
print(f"{c} ^ {d}: {c ^ d} (Bitwise XOR)")
print(f"~{c}: {~c} (Bitwise NOT)")
print(f"{c} << 1: {c << 1} (Left Shift)")
print(f"{c} >> 1: {c >> 1} (Right Shift)")

# Make a long chain using multiple operators to demonstrate precedence
print("\nOperator Precedence:")
# PRECEDENCE BREAKDOWN:
# 1. Math & Shifts : (-2**2 * 3 + 1 << 2) -> -44
# 2. Bitwise Logic : (-44 & 15 ^ 7 | 2) -> 3
# 3. Comparisons   : (3 == 2 in [True, 1]) -> (3 == 2) and (2 in ...) -> False
# 4. Booleans      : False and (not False) or 99 -> False or 99 -> 99
# 5. Ternary       : 99 if (5 > 2) else 0 -> 99
result = -2 ** 2 * 3 + 1 << 2 & 15 ^ 7 | 2 == 2 in [True, 1] and not False or 99 if 5 > 2 else 0
print(f"Result of complex expression: {result}")