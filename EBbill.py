

charges_per_unit = {
    "I - Home": {100: 2, 200: 3, 300: 4, 400: 5, "above": 6},
    "II - Trust": {100: 3, 200: 6, 300: 9, 400: 12, "above": 15},
    "III - Industry": {100: 5, 200: 10, 300: 15, 400: 20, "above": 25}
}

# Prompt the user to input the customer details
eb_no = input("Enter the EB No.: ")
customer_name = input("Enter the customer name: ")
address1 = input("Enter address line 1: ")
address2 = input("Enter address line 2: ")
address3 = input("Enter address line 3: ")
city_town = input("Enter city/town: ")
pincode = input("Enter pincode: ")
customer_category = input("Enter customer category (I - Home, II - Trust, III - Industry): ")
sl_no = input("Enter the Sl.No.: ")
start_unit = int(input("Enter the start unit: "))
end_unit = int(input("Enter the end unit: "))

# Calculate the total units consumed
total_units = end_unit - start_unit

# Check if the customer is in the home category and has consumed less than 50 units
if customer_category == "I - Home" and total_units <= 50:
    amount = 0
else:
    # Calculate the amount based on the customer category and total units consumed
    if total_units <= 100:
        amount = total_units * charges_per_unit[customer_category][100]
    elif total_units <= 200:
        amount = 100 * charges_per_unit[customer_category][100] + (total_units - 100) * charges_per_unit[customer_category][200]
    elif total_units <= 300:
        amount = 100 * charges_per_unit[customer_category][100] + 100 * charges_per_unit[customer_category][200] + (total_units - 200) * charges_per_unit[customer_category][300]
    elif total_units <= 400:
        amount = 100 * charges_per_unit[customer_category][100] + 100 * charges_per_unit[customer_category][200] + 100 * charges_per_unit[customer_category][300] + (total_units - 300) * charges_per_unit[customer_category][400]
    else:
        amount = 100 * charges_per_unit[customer_category][100] + 100 * charges_per_unit[customer_category][200] + 100 * charges_per_unit[customer_category][300] + 100 * charges_per_unit[customer_category][400] + (total_units - 400) * charges_per_unit[customer_category]["above"]

# Print the bill details
print("-------- Bill Details --------")
print(f"EB No.: {eb_no}")
print(f"Customer Name: {customer_name}")
print(f"Address: {address1}, {address2}, {address3}")
print(f"City/Town: {city_town}")
print(f"Pincode: {pincode}")
print(f"Customer Category: {customer_category}")
print(f"Sl.No.: {sl_no}")
print(f"Start Unit: {start_unit}")
print(f"End Unit: {end_unit}")
print(f"Total Units: {total_units}")
print(f"Amount: Rs. {amount}/-")
