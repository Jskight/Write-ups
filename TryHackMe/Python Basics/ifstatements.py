"""
    In this project, you'll create a program that calculates the total
    cost of a customers shopping basket, including shipping.

    - If a customer spends over $100, they get free shipping
    - If a customer spends < $100, the shipping cost is $1.20 per kg of the baskets weight

    Print the customers total basket cost (including shipping) to complete this exercise.

"""

customer_basket_cost = 34
customer_basket_weight = 44

# Write if statement here to calculate the total cost
shipping_cost = 0
if customer_basket_cost >= 100:
 shipping_cost = 0
else:
 shipping_cost = customer_basket_weight * 1.2
total_cost = shipping_cost + customer_basket_cost
print(total_cost)