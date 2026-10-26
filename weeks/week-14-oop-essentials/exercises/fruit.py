class Fruit:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def display(self):
        print(f"Tên: {self.name}")
        print(f"Màu sắc: {self.color}")
        print(f"Giá: {self.price} VNĐ")


# Tạo object
fruit1 = Fruit("Táo", "Đỏ", 20000)
fruit2 = Fruit("Chuối", "Vàng", 15000)

# Hiển thị thông tin
fruit1.display()
print("----------")
fruit2.display()
