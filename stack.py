"""
MIT License

Copyright (c) 2019 Michael Schmidt

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


class Stack:
    """
    A Stack
    """

    def __init__(self):
        self.__stack = []

    def __len__(self):
        return len(self.__stack)

    @property
    def top(self):
        """
        top of Stack
        """

        if not self.__stack:
            return None

        return self.__stack[-1]

    @top.setter
    def top(self, top):
        """
        POP and then PUSH the stack
        """
        if not self.__stack:
            raise ValueError("Ca'nt assign to an emtpy stack")

        self.__stack[-1] = top

    def pop(self, n=1):
        """
        POP operation
        """
        if n < len(self.__stack):
            for _ in range(n):
                self.__stack = self.__stack[:-1]
        elif n == len(self.__stack):
            self.__stack = []
        else:
            raise ValueError('n > stack.size')

    def push(self, value=None):
        """
        PUSH operation
        """
        self.__stack.append(value)

    def empty(self):
        """
        EMPTY query
        """
        return bool(len(self.__stack))

    @property
    def size(self):
        """
        SIZE of Stack
        """
        return len(self.__stack)

    def clear(self):
        """
        clear the Stack
        """
        self.__stack = []
