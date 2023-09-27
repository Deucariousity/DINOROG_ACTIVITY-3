while True:
    print("Welcome!, Dear Customer")
    print("Our Product Sales is 6% discount!")

    name = input("Please Enter your name:")
    print("Hello!", name)

    purchase_amount = float(input("Enter Purchase Amount:"))
    tax = 0.06
    sale_tax = purchase_amount * tax
    
    print("Your Sales Tax is", round(sale_tax, 2))
    print("Thank you!")

    another = input("Proceed to next customer?(yes/no):")
    if another != 'yes':
        break



