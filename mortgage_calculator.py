"""
loan_amt = int
APR = percentage annual percentage rate (float)
rate = (APR/100)/12
"""

loan_amt = int(input("Type in your loan amount: "))
apr = float(input("type in your APR, annual percentage rate, (ex 4.2): "))
rate = round(((apr / 100) / 12), 5)
loan_length = int(input("Type in your loan length in years: "))
months = loan_length * 12
monthly_interest = round((loan_amt * rate), 3)
print(rate)
print(f"Your Monthly Interest payment: ${monthly_interest}")