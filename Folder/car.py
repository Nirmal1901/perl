Here is the equivalent Python code:
```
class Car:
    def __init__(self, brand='Unknown', model='Unknown'):
        self.brand = brand
        self.model = model
    
    @staticmethod
    def set_brand(self, brand):
        self.brand = brand
    
    @staticmethod
    def get_brand(self):
        return self.brand
    
    @staticmethod
    def set_model(self, model):
        self.model = model
    
    @staticmethod
    def get_model(self):
        return self.model
```
Note that in Python, we use the `def` keyword to define methods instead of using the `sub` keyword like in Perl. We also use the `@staticmethod` decorator to indicate that a method does not require an instance of the class to be called.