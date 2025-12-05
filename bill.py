product=input("Enter product name: ")
price=float(input("Enter price of the product: "))
quantity=int(input("Enter quantity purchased: "))
flag=int(input("Are you a member? (1 for Yes / 0 for No):"))

print("\n--- Shopping Bill --- ")
print("Product Name\t: ", product)
print("Price \t\t: ", price)
print("Quantity \t: ", quantity)
print("Member \t\t: ",bool(flag))
total= price * quantity
print("Total Amount \t: ", total)

if flag==1:
    final=total*0.9
else:
    final=total

print("Final amount \t: ", final)

print("\n--- Data Types ---")
print("Type of product name \t: ", type(product))
print("Type of price\t\t: ", type(price))
print("Type of quantity\t: ", type(quantity))
print("Type of member flag\t: ", type(bool(flag)))
print("Type of total amount\t: ", type(total))