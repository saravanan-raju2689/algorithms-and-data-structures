class StackUsingQueues:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, item):
        self.queue1.append(item)

    def pop(self):
        if not self.queue1:
            return None
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))
        popped_item = self.queue1.pop()
        self.queue1, self.queue2 = self.queue2, self.queue1
        return popped_item