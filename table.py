class Table:
    def __init__(self):
        self.table = {}

    def insert(self, key, value):
        self.table[key] = value

    def get(self, key):
        return self.table.get(key)

    def delete(self, key):
        if key in self.table:
            del self.table[key]

    def keys(self):
        return list(self.table.keys())

    def values(self):
        return list(self.table.values())

    def items(self):
        return list(self.table.items())
