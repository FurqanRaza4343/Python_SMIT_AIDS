number_of_products = int(input("How many products?: "))

subtotal = 0
product_names = []
product_prices = []
product_quantities = []
product_total = []



for i in range(number_of_products):
  print("\nProduct", i + 1)
  name = input('Name: ')
  price = int(input('Price: '))
  quantity = int(input('Quantity: '))
  
  total = price * quantity
  subtotal += total
  
  product_names.append(name)
  product_prices.append(price)
  product_quantities.append(quantity)
  product_total.append(total)


if subtotal >= 10000:
  discount = subtotal * (10/100)
  final_bill = subtotal - discount
elif (subtotal >= 5000) and (subtotal < 10000):
  discount = subtotal * (5/100)
  final_bill = subtotal - discount
else:
  discount = 0
  final_bill = subtotal

print('\n============================================\n'
        '             SUPERMARKET BILL'
        '\n============================================\n')


for i in range(number_of_products):
  print(product_names[i], '    ',
        product_quantities[i],
        'x',
        product_prices[i],
        '=',
        product_total[i])

print('\nSubtotal:', subtotal,
      '\nDiscount:', int(discount),
      '\nFinal Bill:', int(final_bill))
print('\n         Thank you for shopping!'
      '\n============================================') 