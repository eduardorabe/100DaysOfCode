# 100 Days of Code
# DAY 2
# Created by eduardorabe
# Split Bill Calculator

# If the bill was $150.00, split between 5 people, with 12% tip. Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60 Tip: There are 2 ways to round a number. You might have to do some
# Googling to solve this.💪 HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq
# =how+to+round+number+to+2+decimal HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal
# -places-in-python

print("Welcome to the Tip Calculator.")

bill_total = float(input("What was the total bill? $"))
people = int(input("How many people to split the bill? "))
tip_percentage = float(input("What percentage tip you want to give? "))

total_per_person = format((bill_total / people) * (1 + tip_percentage / 100), '.2f')

print(f"Each person should pay: ${total_per_person}")
