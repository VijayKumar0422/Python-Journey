class car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Brand ", self.brand)
        print("Model ", self.model)


car1 = car("Toyota ", "Fortuner")
car1.display()
