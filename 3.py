print(" Enter amount of purchases, in dollars:")

purchase = int(input())

if purchase < 10:
	print("Oops! Sorry, that did not work. Try again.") 

purchaseDiscount = purchase * .10
purchaseDiscount1 = purchase - purchaseDiscount
purchaseDiscount2 = str(purchaseDiscount1)
purchaseDiscountDecimalremoval = purchaseDiscount1 - .0

purchaseDiscountTotal = str(purchaseDiscountDecimalremoval)

if purchase >= 10:
	print("You spent over $10! Your final price is $" + purchaseDiscountTotal + "0" + " cents.")
