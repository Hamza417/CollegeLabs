from self_study.postfix.Postfix import Postfix

if __name__ == '__main__':
    tests = [
        "3 + 4 * 2 / ( 1 - 5 ) ** 2 ** 3",  # Standard math with right-associative exponents
        "- 5 + 3",  # Unary minus at the start
        "10 * ( - 2 + 4 )",  # Unary minus after a parenthesis
        "A == B || C != D && NOT E",  # Logical and relational operators
        "5 << 1 + 2",  # Bitwise shift mixed with addition
        ""  # Should throw a ResourceWarning
    ]

    for test in tests:
        print(Postfix.process_expression(test))
