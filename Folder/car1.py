Here is the equivalent Python code:
```
class Car(object):
    def __init__(self, brand=None, model=None):
        self.brand = brand if brand else "Unknown"
        self.model = model if model else "Unknown"
    
    @property
    def brand(self):
        return self._brand
    
    @brand.setter
    def brand(self, value):
        self._brand = value
    
    @property
    def model(self):
        return self._model
    
    @model.setter
    def model(self, value):
        self._model = value
```
Note that in Python, we use `def` to define a function instead of the `sub` keyword used in Perl. We also use `@property` decorator to define getters and setters for attributes. In addition, we use the `if` statement to assign default values for optional arguments.