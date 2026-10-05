from self_study.stack.IllegalArgumentException import IllegalArgumentException
from self_study.stack.Stack import Stack
from self_study.utils.operators import operators, split_tokens, validate_expression


class Postfix:
    @staticmethod
    def process_expression(expression: str):
        # We received an empty expression, raise an exception
        if len(expression) == 0:
            raise ResourceWarning("Expression not defined")

        # We received an invalid expression, raise an exception
        if validate_expression(expression):
            raise IllegalArgumentException(expression + " <= expression validation has failed, terminating!")

        stack = Stack()
        output: list = []
        tokens = split_tokens(expression)

        for i, token in enumerate(tokens):
            if token in ("-", "+"):
                # If it's the 1st token, OR follows an operator, OR follows '('
                if i == 0 or tokens[i - 1] in operators or tokens[i - 1] == "(":
                    token = "u" + token  # Rename '-' to 'u-'

            if token == "(":
                stack.push(token)
                continue

            if token == ")":
                while not stack.is_empty() and stack.peek() != "(":
                    output.append(stack.pop())

                if stack.peek():
                    stack.pop()

                continue

            if token in operators:
                precedence, associativity = operators[token]

                while not stack.is_empty() and stack.peek() != "(" and stack.peek() in operators:
                    precedence2, _ = operators[stack.peek()]

                    is_ltr_associativity = associativity == "L" and precedence <= precedence2
                    is_rtl_associativity = associativity == "R" and precedence < precedence2

                    if is_ltr_associativity or is_rtl_associativity:
                        output.append(stack.pop())
                    else:
                        break

                stack.push(token)
                continue

            if token.isalnum():
                output.append(token)
                continue

            output.append(token)

        while not stack.is_empty():
            output.append(stack.pop())

        return " ".join(output)
