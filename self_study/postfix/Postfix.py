from self_study.stack.Stack import Stack
from self_study.utils.operators import operators


class Postfix:
    def __init__(self):
        self.stack = Stack()
        self.output: list = []

    def postfix(self, expression=""):
        self.output = []
        chars = expression.split()

        for character in chars:
            if character == "(":
                self.stack.push(character)
                continue

            if character == ")":
                while not self.stack.is_empty() and self.stack.peek() != "(":
                    self.output.append(self.stack.pop())

                if self.stack.peek():
                    self.stack.pop()

                continue

            if character in operators:
                precedence, associativity = operators[character]

                while not self.stack.is_empty() and self.stack.peek() != "(" and self.stack.peek() in operators:
                    precedence2, associativity2 = operators[self.stack.peek()]

                    if (associativity == "L" and precedence <= precedence2) or (
                            associativity == "R" and precedence < precedence2):
                        self.output.append(self.stack.pop())
                    else:
                        break

                self.stack.push(character)
                continue

            if character.isalnum():
                self.output.append(character)
                continue

            self.output.append(character)

        while not self.stack.is_empty():
            self.output.append(self.stack.pop())

        return " ".join(self.output)
