# Update Data using transfer from old data

import json
from datetime import datetime

# Load the old data 
with open('data.json', 'r') as f:
    old_data = json.load(f)

# Create a new list to hold the update data
update_data = []

# Initialize variables
total_revenue = 0
quantity_of_hats = 0
customer_id = ""

# Create a dictionary to store reveue for each vendor
vendor_revenue = {}


# Looping over the desired fields from the old data
for item in old_data:
    update_item = {}
    update_item['id'] = item['id']
    update_item['vendor'] = item['vendor']
    update_item['date'] = item['date']
    update_item['customerId'] = item['customer']['id']
    update_item['details'] = []

    # Change the form to "details" from "order" in old_data 
    for key, value in item['order'].items():
        details_item = {}
        details_item['item'] = key
        details_item['quantity'] = value['quantity']
        details_item['price'] = value['price']
        details_item['revenue'] = value['quantity'] * value['price']

        # Populate 'item,'quantity','price', and 'revenue' into details
        update_item['details'].append(details_item)

        # total revenue for each vendor
        if update_item['vendor'] in vendor_revenue:
            vendor_revenue[update_item['vendor']] += details_item['revenue']
        else:
            vendor_revenue[update_item['vendor']] = details_item['revenue']


        # Calculate total revenue of all items
        total_revenue += details_item['revenue']


        # Calculate quantity of hats
        if details_item['item'] == "hat":
            quantity_of_hats += details_item['quantity']

        #Parse the date string and extract the month information
        str_date = datetime.strptime(update_item['date'],'%m/%d/%Y')
        if str_date.month == 10 and details_item['item'] == "ice":
            count = 0
            if details_item['quantity'] > count:
                count = details_item['quantity']
                customer_id = update_item['customerId']

        

    # Finalize all feilds to transfer into update data
    update_data.append(update_item)



# Ventera Developer Challenge

# Create the update data as json data
with open("update.json", "w") as outfile:
    json.dump(update_data, outfile, indent = 1)

# 1. Total revenue (sum of quantity times price of all items)
print(f"The total revenue of all items is ${total_revenue}.")

# 1. Vendor with the most revenue
max_vendor = max(vendor_revenue, key=vendor_revenue.get)
print(f"The vendor who made with most revenue is '{max_vendor}'.\nThe revenue is ${vendor_revenue[max_vendor]}.")

# 1. Quantity of hats sold (items where the key is exactly 'hat')
print(f"The quantity of hats sold is {quantity_of_hats}.")

# 1. ID of the customer that bought the most ice in October
print(f"ID of the customer that bought the most ice in Oct is '{customer_id}'.")


print