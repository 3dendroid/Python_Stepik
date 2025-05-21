# объявление функции


def get_shipping_cost(quantity):
    if quantity == 1:
        return 1000
    if quantity > 1:
        return 1000 + (120 * quantity - 120)
        # return 1000 + (quantity - 1)
    return quantity


# считываем данные
n = int(input())

# вызываем функцию
print(get_shipping_cost(n))
