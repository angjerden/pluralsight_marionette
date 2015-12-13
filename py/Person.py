class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

class PersonEncoder:
    def default(self, obj):
        return obj.__dict__
