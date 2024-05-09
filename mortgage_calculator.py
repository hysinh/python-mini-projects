import math

"""
loan_amt = int
APR = percentage annual percentage rate (float)
rate = (APR/100)/12
"""


def get_mortgage_data():
    print("inside the get_mortgage_data function")

print("Compare Mortgage payments and Interest savings")
get_mortgage_data()

loan_amt = int(input("Type in your loan amount: "))
apr = float(input("type in your APR, annual percentage rate, (ex 4.2): "))
rate = round(((apr / 100) / 12), 5)
loan_length = int(input("Type in your loan length in years: "))
months = loan_length * 12
monthly_interest = round((loan_amt * rate), 3)
monthly_payment = ((apr / 100 / 12) * loan_amt) / (1 - (math.pow((1 + (apr / 100 / 12)), (-loan_length * 12))))
print(rate)
print(f"Your Monthly Interest payment: ${monthly_interest}")
print(f"Your monthly payment: ${round(monthly_payment, 2)}")