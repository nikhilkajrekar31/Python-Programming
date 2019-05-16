# Name: Nikhil Kajrekar
# UTA ID: 1001552488

quantity = int(input("Enter number of packages purchased: "))
amount = quantity*99
if quantity >= 10 and quantity <= 19:
    discount = amount*0.1
    total_amount = amount - discount
    print("Discount Amount: $",discount)
    print("Total Amount after Discount: $",total_amount)
elif quantity >= 20 and quantity <= 49:
    discount = amount*0.2
    total_amount = amount - discount
    print("Discount Amount: $",discount)
    print("Total Amount after Discount: $",total_amount)
elif quantity >= 50 and quantity <= 99:
    discount = amount*0.3
    total_amount = amount - discount
    print("Discount Amount: $",discount)
    print("Total Amount after Discount: $",total_amount)
else:
    discount = amount * 0.4
    total_amount = amount - discount
    print("Discount Amount: $", discount)
    print("Total Amount after Discount: $", total_amount)

