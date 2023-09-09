product_name = "rower"
price = 300
amount = 2

warehouses = {}

warehouses[product_name] = {
    "price": price,
    "amount": amount
}

warehouses["boat"] = {
    "price": price,
    "amount": amount
}

print(warehouses)

print(warehouses["boat"])
print(warehouses["boat"]["price"])