class Stock:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity


    def get_attributes(self):
        ob_att = [self.name,self.quantity]
        return ob_att


    def __str__(self):
        return f"{self.name}: {self.quantity}"
