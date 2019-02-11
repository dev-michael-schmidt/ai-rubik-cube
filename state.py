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

import copy

class State:

    def __init__(self, state=None):
        if isinstance(state, State):
            self.__cost = state.__cost + 1
        else:
            self.__cost = 0

        self.__parent = None
        if isinstance(state, State):
            self.__parent = state
            self.__state = copy.copy(state.__state)
        else:
            self.__state = copy.copy(state)

    def __call__(self, *args, **kwargs):
        return self.__state.__call__(*args, **kwargs)

    def __lt__(self, other):
        if isinstance(other, State):
            return self.__cost < other.__cost

    def __le__(self, other):
        if isinstance(other, State):
            return self.__cost <= other.__cost
          # return comparison
    def __eq__(self, other):
        if isinstance(other, State):
            return self.__cost == other.__cost

    def __ne__(self, other):
        if isinstance(other, State):
            return self.__cost != other.__cost

    def __gt__(self, other):
        if isinstance(other, State):
            return self.__cost > other.__cost

    def __ge__(self, other):
        if isinstance(other, State):
            return self.__cost >= other.__cost

    def get(self):
        return self.__state

    @property
    def cost(self):
        return self.__cost

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, state):
        self.__state = state
