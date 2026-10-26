class Fruit:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def display(self):
        print(f"Ten: {self.name}")
        print(f"Mau sac: {self.color}")
        print(f"G ia: {self.price} VND")


# Tao object
fruit1 = Fruit("Tao", "Do", 20000)
fruit2 = Fruit("Chuoi", "Vang", 15000)

# Hien thi thong tin
fruit1.display()
print("----------")
fruit2.display()
