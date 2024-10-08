# Class from previous portfolio assignment
class ItemToPurchase:
    item_name = "none"
    item_price = 0.0
    item_quantity = 0
    item_description = ""

    def __init__(self,name,price,quantity,description):
        self.item_name = name
        self.item_price = price
        self.item_quantity = quantity
        self.item_description = description

    def print_item_cost(self):
        print('{} {:.0f} @ ${:.2f} = ${:.2f}'
              .format(self.item_name,self.item_quantity,self.item_price, self.item_price*self.item_quantity))
        

# Step 4: Build the ShoppingCart class with the following data attributes and 
# related methods.  Note: Some can be method stubs (empty methods) initially, to
# be completed in later steps

class ShoppingCart:

    def __init__(self, customer_name = "none", current_date = "January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []
    
    def add_item(self,ItemToPurchase):
        self.cart_items.append(ItemToPurchase)

    def remove_item(self,ItemToRemove):
        if ItemToRemove not in self.cart_items:
            print(f'{ItemToRemove} was not found in cart.')
        
        else: 
            self.cart_items.remove(ItemToRemove)
            print(f'{ItemToRemove} removed from cart.')

    def modify_item(self,ItemToPurchase):
        if ItemToPurchase not in self.cart_items:
            print(f'{ItemToPurchase} not found in cart, nothing to modify.')

        for item in self.cart_items:
            if ItemToPurchase.item_name == item.item_name:
                # Check if parameter has default values for description, price and quantity.  If not, modify item in cart.
                if item.item_description != "" and item.item_price > 0.0 and item.item_quantity > 0:
                    self.cart_items[item] = ItemToPurchase

    def get_num_items_in_cart(self):
        num_items = 0
        for item in self.cart_items:
            num_items += item.item_quantity
        return num_items
    
    def get_cost_of_cart(self):
        cost = 0
        for item in self.cart_items:
            cost += item.item_quantity * item.item_price
        return cost
    
    def print_total(self):
        print("{}'s Shopping Cart - {}"
              .format(self.customer_name,self.current_date))
        if len(self.cart_items) == 0:
            print('SHOPPING CART IS EMPTY')
        
        else: 
            print(f'Number of Items: {self.get_num_items_in_cart()}')

            for item in self.cart_items:
                print('{} {} @ ${} = ${}'
                      .format(item.item_name,item.item_quantity,item.item_price,item.item_price*item.item_quantity))

            print(f'Total: ${self.get_cost_of_cart()}')    
            
        
    def print_descriptions(self):
        print("{}'s Shopping Cart - {}"
              .format(self.customer_name,self.current_date))
        
        if len(self.cart_items) == 0:
            print('SHOPPING CART IS EMPTY')
        else: 
            print('Item Descriptions')

            for item in self.cart_items:
                print(f'{item.item_name}: {item.item_description}') 
            

# Part 4 - 
# Input Section

# customer_name = input('What is your name?:')
# date = input('What is the date?:')

customer_name = "Brennen"
date = "October 6, 2024"

item_1 = ItemToPurchase('Nike Romaleos',189,2,'Volt color, Weightlifting shoes')
item_2 = ItemToPurchase('Chocolate Chips',3,5,'Semi-sweet')
item_3 = ItemToPurchase('Powerbeats 2 Headphones',128,1,'Bluetooth headphones')

myCart = ShoppingCart(customer_name,date)
myCart.add_item(item_1)
myCart.add_item(item_2)
myCart.add_item(item_3)
# myCart.print_total()
# myCart.print_descriptions()

# Step 5 -
# In the main section of your code, implement the print_menu() function. print_menu() has a ShoppingCart parameter and outputs a menu of options to manipulate the shopping cart. 
# Each option is represented by a single character. Build and output the menu within the function.

def print_menu(ShoppingCart):
    key = ""
    while key != 'q':
        print('MENU')
        print('a - Add item to cart')
        print('r - Remove item from cart')
        print('c - Change item quantity')
        print("i - Output items' descriptions")
        print('o - Output shopping cart')
        print('q - Quit')
        key = input('Choose an option: ')
# Step 6 - Implement Output shopping cart menu option. Implement Output item's description menu option.
        if key == 'o':
            print('OUTPUT SHOPPING CART')
            ShoppingCart.print_total()
        
        if key == 'i':
            print("OUTPUT ITEMS' DESCRIPTIONS")
            ShoppingCart.print_descriptions()

# Call print_menu on myCart to start the while loop
print_menu(myCart)