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

# PRECEDENCE BREAKDOWN:
# 1. Powers (R-to-L) : 1 ** 3 -> 1, then 2 ** 1 -> 2
# 2. Bitwise NOT     : ~2 -> -3  (unary ~ is lower than **)
# 3. Mult / Div / Mod: (-3 * 5 // 2 % 7) -> (-15 // 2 % 7) -> (-8 % 7) -> 6
# 4. Bit Shifts      : (6 << 2 >> 1) -> (24 >> 1) -> 12
# 5. Bitwise Logic   : (12 & 14 ^ 3 | 5) -> (12 ^ 3 | 5) -> (15 | 5) -> 15
# 6. Comparisons     : (15 in {5, 6} == True) -> (15 in {5, 6}) and ({5, 6} == True) -> False
# 7. Booleans        : False and (not 0) or "fallback" -> False and True or "fallback" -> "fallback"
# 8. Ternary         : "fallback" if (3 < 5) else None -> "fallback"
result = ~2 ** 1 ** 3 * 5 // 2 % 7 << 2 >> 1 & 14 ^ 3 | 5 in {5, 6} == True and not 0 or "fallback" if 3 < 5 else None
print(f"Result of complex expression: {result}")

# Step 1: Right-to-Left Exponentiation (** binds tighter than unary ~)
step1 = 2 ** (1 ** 3)
print(f"Step 1 (Powers):              {step1}")  # 2

# Step 2: Unary Bitwise NOT (~x = -(x + 1))
step2 = ~step1
print(f"Step 2 (Bitwise NOT):        {step2}")  # -3

# Step 3: Multiplicative (*, //, % evaluated Left-to-Right)
step3a = step2 * 5  # -15
step3b = step3a // 2  # -8 (rounds toward negative infinity)
step3 = step3b % 7  #  6 (Python keeps divisor's positive sign)
print(f"Step 3 (Mult / Floor / Mod):  {step3}")  # 6

# Step 4: Bitwise Shifts (<<, >> evaluated Left-to-Right)
step4a = step3 << 2  # 24
step4 = step4a >> 1  # 12
print(f"Step 4 (Bit Shifts):         {step4}")  # 12

# Step 5: Bitwise Logic Hierarchy (& > ^ > |)
step5a = step4 & 14  # 12 & 14 = 12
step5b = step5a ^ 3  # 12 ^ 3  = 15
step5 = step5b | 5  # 15 | 5  = 15
print(f"Step 5 (Bitwise &, ^, |):    {step5}")  # 15

# Step 6: Chained Comparison (15 in {5, 6} == True)
# Expands to: (15 in {5, 6}) and ({5, 6} == True)
part_a = step5 in {5, 6}  # False
part_b = {5, 6} == True  # False
step6 = part_a and part_b  # Short-circuits on part_a
print(f"Step 6 (Chained Comparison): {step6}")  # False

# Step 7: Boolean Logic Hierarchy (not > and > or)
bool_not = not 0  # True
bool_and = step6 and bool_not  # False and True -> False
step7 = bool_and or "fallback"  # False or "fallback" -> "fallback"
print(f"Step 7 (Booleans):           {step7}")  # 'fallback'

# Step 8: Ternary / Conditional Expression (if - else)
condition = 3 < 5  # True
final_result = step7 if condition else None
print(f"Step 8 (Final Ternary):       {final_result}")  # 'fallback'