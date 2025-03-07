class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        # Push item onto stack1
        self.stack1.append(item)

    def dequeue(self):
        # If stack2 is empty, move elements from stack1 to stack2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        # If stack2 is still empty, raise an error
        if not self.stack2:
            raise IndexError("dequeue from empty queue")
        # Pop the top item from stack2
        return self.stack2.pop()

# Time Complexity:
# Enqueue: O(1)
# Dequeue: O(n) in the worst case when transferring elements from stack1 to stack2.