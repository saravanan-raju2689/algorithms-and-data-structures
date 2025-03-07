class SpecialStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value):
        self.stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self):
        if not self.stack:
            return None
        value = self.stack.pop()
        if value == self.min_stack[-1]:
            self.min_stack.pop()
        return value

    def get_min(self):
        if not self.min_stack:
            return None
        return self.min_stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

# Explanation:
# This special stack supports push, pop, and retrieving the minimum element in O(1) time.
# The push operation adds an element to the stack and updates the minimum stack if necessary.
# The pop operation removes the top element and updates the minimum stack if the popped element is the current minimum.
# The get_min operation retrieves the minimum element in O(1) time.

# Time Complexity:
# - push: O(1)
# - pop: O(1)
# - get_min: O(1)
# - is_empty: O(1)
# - size: O(1)