inventory_toppings = ['pepperoni', 'sausage', 'cheese', 'peppers']
requested_toppings = []
request1 = raw_input('Please give me a topping: ')
if request1 in inventory_toppings:
  requested_toppings.append(request1)
  print "We have {0}!".format(request1)
else:
  print "Sorry, we don't have {0}.".format(request1)

request2 = raw_input('Please give me one more topping: ')
if request2 in inventory_toppings:
  requested_toppings.append(request2)
  print "We have {0}!".format(request2)
else:
  print "Sorry, we don't have {0}.".format(request2)

print "Here are your toppings:"
print requested_toppings

