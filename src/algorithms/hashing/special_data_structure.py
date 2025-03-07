class SpecialDataStructure:
    def __init__(self):
        self.data = {}
    
    def insert(self, key, value):
        self.data[key] = value
    
    def delete(self, key):
        if key in self.data:
            del self.data[key]
    
    def get(self, key):
        return self.data.get(key, None)
    
    def contains(self, key):
        return key in self.data
    
    def get_all(self):
        return self.data.items()