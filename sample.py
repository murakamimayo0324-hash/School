def calculate_average(numbers):
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)


def find_max(numbers):
    max_value = numbers[0]
    for n in numbers:
        if n > max_value:
            max_value = n
    return max_value


def filter_even(numbers):
    result = []
    for n in numbers:
        if n % 2 == 0:
            result.append(n)
    return result


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price, quantity=1):
        self.items.append({"name": name, "price": price, "quantity": quantity})

    def total_price(self):
        total = 0
        for item in self.items:
            total += item["price"] * item["quantity"]
        return total

    def remove_item(self, name):
        for item in self.items:
            if item["name"] == name:
                self.items.remove(item)


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6]
    print("Average:", calculate_average(nums))
    print("Max:", find_max(nums))
    print("Even numbers:", filter_even(nums))

    cart = ShoppingCart()
    cart.add_item("apple", 100, 3)
    cart.add_item("banana", 50, 2)
    print("Total price:", cart.total_price())
