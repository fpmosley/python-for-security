class Car:
    def __init__(self, color, num_of_windows, price):
        self.color = color
        self.num_of_windows = num_of_windows
        self.price = price


car1 = Car("Red", 4, 100000)
car2 = Car("Blue", 2, 300500)
print(car1.color)
print(car2.price)
