import logging

from self_study.stack.StackOverflow import StackOverflow
from self_study.stack.StackUnderflow import StackUnderflow


class Stack:
    def __init__(self, size=100):
        """
        Initialize the stack

        :param size: specify the max stack size, if no size is
            specified, then 100 stack size will be used.
        """
        self.stack_size = size
        self.stack = []

    def is_empty(self):
        """
        Check if the stack is empty.

        :return: True if stack is empty else False.
        """
        if len(self.stack) == 0:
            return True
        else:
            logging.debug(
                "Stack is not empty, size: %d",
                len(self.stack)
            )

            return False

    def is_full(self):
        """
        Check if the stack is full.

        :return: True is the stack is full else False.
        """
        if len(self.stack) == self.stack_size:
            return True
        else:
            logging.debug(
                "%d indexes remaining in the stack",
                self.stack_size - len(self.stack)
            )

            return False

    def push(self, value):
        """
        Push a value on to the stack.

        :param value: value to be added at the top of the stack
        :raises: StackOverflow if stack is full already.
        """
        if self.is_full():
            raise StackOverflow("Stack is full")

        self.stack.append(value)
        logging.info(
            "value %s has been inserted into the stack",
            value
        )

    def pop(self):
        """
        Pops the top value from the stack.
        :return: the popped value.
        :raises: StackUnderflow if the stack is not full.
        """
        if self.is_empty():
            raise StackUnderflow("stack is already empty")

        value = self.stack[-1]
        self.stack.pop()
        logging.info("top item %s has removed", value)
        return value

    def peek(self):
        """
        Peeks the top value of the stack.
        :return: the peeked value.
        """
        if self.is_empty():
            logging.info("stack is empty")
            return None
        else:
            return self.stack[-1]

    def display(self):
        """
        Displays the whole stack.
        """
        print(self.stack)
