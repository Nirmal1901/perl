Here is the Python code that corresponds to the given Perl code:
```
class Car:
    def __init__(self, brand="Unknown", model="Unknown"):
        self.brand = brand
        self.model = model
    
    def set_brand(self, brand):
        self.brand = brand
    
    def get_brand(self):
        return self.brand
    
    def set_model(self, model):
        self.model = model
    
    def get_model(self):
        return self.model
```
Note that in Python, we use the `def` keyword to define methods instead of the `sub` keyword used in Perl. Additionally, we use the `__init__` method to initialize the class with default values for the attributes.