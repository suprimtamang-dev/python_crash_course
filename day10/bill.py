def bill(customer, *items, **details):
    print("Customer:", customer)
    print("Items:", items)
    print("Details:", details)

print(bill("Suprim", "Laptop", "Mouse", "Keyboard", payment="Cash", address="Kathmandu"))