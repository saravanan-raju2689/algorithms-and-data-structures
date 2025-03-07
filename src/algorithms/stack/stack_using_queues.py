class StackUsingQueues:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, item):
        # Push item onto stack
        self.queue1.append(item)

    def pop(self):
        # Pop item from stack
        if not self.queue1:
            return None
        
        # Move all elements except the last one to queue2
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))
        
        # The last element in queue1 is the top of the stack
        popped_item = self.queue1.pop(0)

        # Swap the names of the queues
        self.queue1, self.queue2 = self.queue2, self.queue1
        
        return popped_item

    def top(self):
        # Get the top item of the stack
        if not self.queue1:
            return None
        
        # Move all elements except the last one to queue2
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))
        
        # The last element in queue1 is the top of the stack
        top_item = self.queue1[0]
        
        # Move the last element to queue2 as well
        self.queue2.append(self.queue1.pop(0))

        # Swap the names of the queues
        self.queue1, self.queue2 = self.queue2, self.queue1
        
        return top_item

    def is_empty(self):
        # Check if the stack is empty
        return len(self.queue1) == 0

# Time Complexity:
# - push: O(1)
# - pop: O(n)
# - top: O(n)
# - is_empty: O(1)