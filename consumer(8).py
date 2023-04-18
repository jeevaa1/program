def print_customers(customers):
    """Helper function to print the list of customers"""
    print("Customers:")
    for customer in customers:
        print(f"{customer[0]}: {customer[1]}")
    print()

def find_customer_index(customers, name):
    """Helper function to find the index of a customer by name"""
    for i, customer in enumerate(customers):
        if customer[0] == name:
            return i
    return None

# Initialize the list of customers with some data
customers = [("Alice", "1234567890"), ("Bob", "9876543210"), ("Charlie", "5555555555"), ("Dave", "9999999999"), ("Eve", "7777777777")]

while True:
    print("Select an action:")
    print("1. Check if a customer exists")
    print("2. Modify a customer name")
    print("3. Modify a customer mobile number")
    print("4. Add a new customer")
    print("5. Sort customers by name")
    print("6. Remove a customer")
    print("7. Remove all customers")
    print("8. Quit")
    action = input("Enter action number: ")

    if action == "1":
        name = input("Enter customer name: ")
        if find_customer_index(customers, name) is not None:
            print(f"{name} is in the database")
        else:
            print(f"{name} is not in the database")

    elif action == "2":
        old_name = input("Enter customer name to modify: ")
        new_name = input("Enter new customer name: ")
        index = find_customer_index(customers, old_name)
        if index is not None:
            customers[index] = (new_name, customers[index][1])
            print("Customer name modified")
            print_customers(customers)
        else:
            print(f"{old_name} not found in the database")

    elif action == "3":
        name = input("Enter customer name to modify: ")
        mobile_number = input("Enter new mobile number: ")
        index = find_customer_index(customers, name)
        if index is not None:
            customers[index] = (customers[index][0], mobile_number)
            print("Customer mobile number modified")
            print_customers(customers)
        else:
            print(f"{name} not found in the database")

    elif action == "4":
        name = input("Enter new customer name: ")
        mobile_number = input("Enter new mobile number: ")
        customers.append((name, mobile_number))
        print("New customer added")
        print_customers(customers)

    elif action == "5":
        customers.sort(key=lambda x: x[0])
        print("Customers sorted by name")
        print_customers(customers)

    elif action == "6":
        name = input("Enter customer name to remove: ")
        index = find_customer_index(customers, name)
        if index is not None:
            customers.pop(index)
            print("Customer removed")
            print_customers(customers)
        else:
            print(f"{name} not found in the database")

    elif action == "7":
        customers.clear()
        print("All customers removed")
        print_customers(customers)

    elif action == "8":
        print("Exiting...")
        break

    else:
        print("Invalid action number. Try again.")
