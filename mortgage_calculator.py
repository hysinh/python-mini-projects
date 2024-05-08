"""
loan_amt = int
APR = percentage annual percentage rate (float)
rate = (APR/100)/12
"""

loan_amt = int(input("Type in your loan amount: "))
apr = float(input("type in your APR, annual percentage rate, (ex 4.2): "))
rate = round(((apr / 100) / 12), 5)

print(rate)