print("*"*54)
for element in ["Coding Temple, Inc.","283 Franklin St.","Boston, MA"]:
    print(" "*17,end="")
    print(element)

print("="*54)

product_name  = ["Product Name","Books","Computer","Monitor"]
product_price = ["Product Price","$49.95","$579.99","$124.89"]
product = zip(product_name, product_price)

for prod in product:
    print(" "*6,end="")
    print("{0:15s}".format(prod[0]), "{0:15s}".format(prod[1]))


print("="*54)
print(" "*21,end="")
print("{0:15s}".format("Total"))


from decimal import Decimal
sum = Decimal(0)
for i in range(1,len(product_price)):
    a = product_price[i];
    sum = sum + Decimal(a[1::])

print(" "*21,end="")
print("{0:15s}".format("$" + str(sum)))

print("="*54)
print()
print(" "*6,end="")
print("Thanks for shopping with us today!")
print()
print("*"*54)
