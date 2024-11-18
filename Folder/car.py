Here is the Python code equivalent of the Perl code:
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
Note that in Python, we use the `:` keyword instead of `use strict; use warnings;` to indicate a block of code. Also, in Python we use the `__init__` function as a constructor and we don't need to use the `bless $self, $class` statement like in Perl. Finally, in Python we can define class methods using the `@property` decorator to make them behave like attributes, which is not possible with Perl.