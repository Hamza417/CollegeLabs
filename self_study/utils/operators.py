# Format: 'operator': (precedence_level, 'associativity')
# Higher number = evaluated first

operators = {
    # Logical Operators
    'OR': (1, 'L'),
    '||': (1, 'L'),
    'AND': (2, 'L'),
    '&&': (2, 'L'),

    # Bitwise Operators
    '|': (3, 'L'),
    # Note: If building a math calculator, we might want to use '^' for exponents.
    # If building a programming language parser, '^' is usually Bitwise XOR (at level 4).
    '^': (4, 'L'),  # Bitwise XOR
    '&': (5, 'L'),
    '<<': (6, 'L'),  # Left shift
    '>>': (6, 'L'),  # Right shift

    # Equality & Relational
    '==': (7, 'L'),
    '!=': (7, 'L'),
    '<': (8, 'L'),
    '<=': (8, 'L'),
    '>': (8, 'L'),
    '>=': (8, 'L'),

    # Additive (Math)
    '+': (9, 'L'),
    '-': (9, 'L'),

    # Multiplicative (Math)
    '*': (10, 'L'),
    '/': (10, 'L'),
    '//': (10, 'L'),  # Integer division
    '%': (10, 'L'),  # Modulo / Remainder

    # Exponentiation (Math)
    # Right-associative (e.g., 2^3^2 is evaluated as 2^(3^2))
    '**': (11, 'R'),
    # '^': (11, 'R'), # Uncomment this if using '^' for math exponents instead of XOR

    # Unary Operators
    # Right-associative. Evaluated before almost everything else.
    'NOT': (12, 'R'),
    '!': (12, 'R'),
    'u-': (12, 'R'),  # Unary minus (e.g., negative numbers like -5)
    'u+': (12, 'R')  # Unary plus
}
