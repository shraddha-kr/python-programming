import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    totalMealCost = 0

    totalTip = meal_cost * (tip_percent/100)
    totalTax = meal_cost * (tax_percent/100)
    totalMealCost =  meal_cost + totalTax + totalTip 

    totalMealCost = round(totalMealCost)

    # Output
    print(totalMealCost)


if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)




'''
# Inputs
mealCost = float(input())
tipPercent = int(input())
taxPercent = int(input())

totalMealCost = 0

totalTip = mealCost * (tipPercent/100)
totalTax = mealCost * (taxPercent/100)
totalMealCost =  mealCost + totalTax + totalTip 

totalMealCost = round(totalMealCost)

# Output
print(totalMealCost)
'''
