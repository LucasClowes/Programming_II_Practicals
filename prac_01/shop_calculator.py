number_of_items = int(input("Number of Items: "))
while number_of_items < 0:
    print("invalid number of items!")
    number_of_items = int(input("Number of Items: "))

total_cost = 0
for i in range(number_of_items):
    total_cost += float(input("Price of item: $"))
if total_cost > 100:
    discount_cost = total_cost - (total_cost * 0.1)
    print("Total price for {} items is ${}".format(number_of_items, discount_cost))
else:
    print("Total price for {} items is ${}".format(number_of_items, total_cost))
