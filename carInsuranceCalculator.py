user_age = int(input('Enter age: '))

if user_age < 25:
  insurance_price = 4800
else:
  insurance_price = 2200

print('Annual price: ${}'.format(insurance_price))
