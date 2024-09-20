# Brennen Bates  9/20/24
# Write a program that calculates the total amount of a meal purchased at a restaurant.
# The program should ask the user to enter the charge for the food and then calculate the amounts
# with an 18 percent tip and a 7 percent sales tax. Display each of these amounts and the total price.

meal_cost = float(input('Charge for the food:'))
tip_amt = meal_cost*0.18
tax_amt = meal_cost*0.07
final_total = meal_cost+tip_amt+tax_amt

print('The cost of the meal was ${:.2f}.\nAn 18% tip is ${:.2f}.\nA 7% tax on the sale is ${:.2f}.\nThe final total is ${:.2f}.'
      .format(meal_cost,tip_amt,tax_amt,final_total))