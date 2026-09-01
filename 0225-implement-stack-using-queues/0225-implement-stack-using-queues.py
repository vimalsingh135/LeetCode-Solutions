
from queue import Queue

class MyStack:

    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x: int) -> None:
        self.q1.put(x)

    def pop(self) -> int:
        if self.q1.empty():
            print("the stack is empty")
            return -1
        while self.q1.qsize() > 1:
            self.q2.put(self.q1.get())
        popped_element = self.q1.get()
        self.q1, self.q2 = self.q2, self.q1
        return popped_element

    def top(self) -> int:
        if self.q1.empty():
            print("the stack is empty")
            return -1
        while self.q1.qsize() > 1:
            self.q2.put(self.q1.get())
        top_element = self.q1.get()
        self.q2.put(top_element)  # need to put it back, since we're only peeking
        self.q1, self.q2 = self.q2, self.q1
        return top_element

    def empty(self) -> bool:
        return self.q1.empty()