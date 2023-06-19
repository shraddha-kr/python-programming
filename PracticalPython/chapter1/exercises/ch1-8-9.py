"""
A lot of cell phones have tip calculators. Write one. Ask the user for the
price of the meal and the percent tip they want to leave. Then print both the tip
amount and the total bill with the tip included.
"""
price = eval(input("Enter the price of the meal: "))
percentTip = eval(input("Enter the % of tip: "))
tipAmt = (price * percentTip)/100
totalBill = price + tipAmt
print("Price of the meal: ", price)
print("% Tip: ", percentTip)
print("TipAmount: ", tipAmt)
print("Total Bill: ", totalBill)
