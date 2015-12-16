print(" Enter amount of purchases, in dollars:")

purchase = float(input())
purchase1 = str(purchase)
if purchase < 1000:
        print("Oops! Sorry, that did not work. Try again.")

purchaseDiscount = purchase1 * .10
purchaseDiscount1 = purchase1 - purchaseDiscount
purchaseDiscount2 = str(purchaseDiscount1)

if purchase >= 1000:
	print("You spent over $10! Your final price is " + purchaseDiscount1 +  " cents.")
