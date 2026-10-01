from self_study.stack.Stack import Stack
from self_study.utils.operators import operators


class Postfix:
    @staticmethod
    def process_expression(expression: str):
        if len(expression) == 0:
            raise ResourceWarning("Expression not defined")

        stack = Stack()
        output: list = []
        chars = expression.split()

        for i, character in enumerate(chars):
            if character in ("-", "+"):
                # If it's the 1st token, OR follows an operator, OR follows '('
                if i == 0 or chars[i - 1] in operators or chars[i - 1] == "(":
                    character = "u" + character  # Rename '-' to 'u-'

            if character == "(":
                stack.push(character)
                continue

            if character == ")":
                while not stack.is_empty() and stack.peek() != "(":
                    output.append(stack.pop())

                if stack.peek():
                    stack.pop()

                continue

            if character in operators:
                precedence, associativity = operators[character]

                while not stack.is_empty() and stack.peek() != "(" and stack.peek() in operators:
                    precedence2, associativity2 = operators[stack.peek()]

                    if (associativity == "L" and precedence <= precedence2) or (
                            associativity == "R" and precedence < precedence2):
                        output.append(stack.pop())
                    else:
                        break

                stack.push(character)
                continue

            if character.isalnum():
                output.append(character)
                continue

            output.append(character)

        while not stack.is_empty():
            output.append(stack.pop())

        return " ".join(output)
