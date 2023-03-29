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
max_ice_quantity = 0
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


        # Calculate total revenue of all items
        total_revenue += details_item['revenue']


        # Calculate quantity of hats
        if details_item['item'] == "hat":
            quantity_of_hats += details_item['quantity']


        # Total revenue for each vendor
        if update_item['vendor'] in vendor_revenue:
            vendor_revenue[update_item['vendor']] += details_item['revenue']
        else:
            vendor_revenue[update_item['vendor']] = details_item['revenue']


        # Parse the date string and extract the month information
        str_date = datetime.strptime(update_item['date'],'%m/%d/%Y')
        if str_date.month == 10 and details_item['item'] == "ice":
            if details_item['quantity'] > max_ice_quantity:
                max_ice_quantity = details_item['quantity']
                customer_id = update_item['customerId']

        
    # Finalize all feilds to transfer into update data
    update_data.append(update_item)



# Ventera Developer Challenge

# Create the update data as json data
with open("update.json", "w") as outfile:
    json.dump(update_data, outfile, indent = 1)

# 1. Total revenue (sum of quantity times price of all items)
print(f"The total revenue of all items is ${total_revenue}.")

# 2. Vendor with the most revenue
max_vendor = max(vendor_revenue, key=vendor_revenue.get)
print(f"The vendor who made with most revenue is '{max_vendor}'. The revenue is ${vendor_revenue[max_vendor]}.")

# 3. Quantity of hats sold (items where the key is exactly 'hat')
print(f"The quantity of hats sold is {quantity_of_hats}.")

# 4. ID of the customer that bought the most ice in October
print(f"ID of the customer that bought the most ice in Oct is '{customer_id}'.")


#    ---------------
#   | sample output |
#    ---------------

# The total revenue of all items is $7536.
# The vendor who made with most revenue is 'partyco'. The revenue is $2969.
# The quantity of hats sold is 115.
# ID of the customer that bought the most ice in Oct is 'd7aa81e3-2991-474b-87b8-85ce12a7d3ea'.


#        -----------------------------------------------------------
# ****** | See the update.json file is created after implementation | *******
#        -----------------------------------------------------------
# [
#  {
#   "id": 1,
#   "vendor": "acme",
#   "date": "03/03/2017",
#   "customerId": "8baa6dea-cc70-4748-9b27-b174e70e4b66",
#   "details": [   
#    {
#     "item": "hat",
#     "quantity": 14,
#     "price": 8,
#     "revenue": 112
#    },
#    {
#     "item": "cake",
#     "quantity": 9,
#     "price": 3,
#     "revenue": 27
#    },
#    {
#     "item": "ice",
#     "quantity": 10,
#     "price": 5,
#     "revenue": 50
#    },
#    {
#     "item": "candy",
#     "quantity": 6,
#     "price": 8,
#     "revenue": 48
#    }
#   ]
#  },
#  {
#   "id": 2,
#   "vendor": "acme",
#   "date": "08/23/2017",
#   "customerId": "d2584a20-7490-499a-83be-d7cea4a0e260",
#   "details": [
#    {
#     "item": "cake",
#     "quantity": 8,
#     "price": 1,
#     "revenue": 8
#    },
#    {
#     "item": "punch",
#     "quantity": 19,
#     "price": 7,
#     "revenue": 133
#    },
#    {
#     "item": "bouncy house",
#     "quantity": 4,
#     "price": 9,
#     "revenue": 36
#    }
#   ]
#  },
#  {
# ...............
