# Step 1: Build the ItemToPurchase class:

class ItemToPurchase:
    item_name = "none"
    item_price = 0
    item_quantity = 0

    def __init__(self,name,price,quantity):
        self.item_name = name
        self.item_price = price
        self.item_quantity = quantity

    def print_item_cost(self):
        print('{} {:.0f} @ ${:.2f} = ${:.2f}'
              .format(self.item_name,self.item_quantity,self.item_price, self.item_price*self.item_quantity))
        
# Step 2: In the main section of your code, prompt the user for two items and create two objects of the ItemToPurchase class.

item_1_name = input('Enter the item name:')
item_1_price = float(input("Enter the item price:"))
item_1_quantity = int(input("Enter the item quantity:"))

item_2_name = input('Enter the item name:')
item_2_price = float(input("Enter the item price:"))
item_2_quantity = int(input("Enter the item quantity:"))

item_1 = ItemToPurchase(item_1_name,item_1_price,item_1_quantity)
item_2 = ItemToPurchase(item_2_name,item_2_price,item_2_quantity)


# Step 3: Add the costs of the two items together and output the total cost.

print('     TOTAL COST')
item_1.print_item_cost()
item_2.print_item_cost()
print('     Total: ${:.2f}'
      .format(item_1.item_quantity * item_1.item_price + item_2.item_quantity * item_2.item_price))