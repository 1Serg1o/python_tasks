'''
Program counts the amount of monthly installments broken down into:
entier_installment and sepperately shows intrests
'''

credit_amount = int(input("Enter credit ammount "))
percentage = int(input("Enter bank percentage: "))
loan_period = int(input("Eter loan period: "))

percentage = percentage / 100
capital_installment = credit_amount / loan_period
month_percentage = percentage / 12

for nr_m in range(loan_period):
    intrest_installment = credit_amount * month_percentage
    entier_installment = intrest_installment + capital_installment
    print(str(nr_m + 1) + ". " + str(entier_installment) + " Intrest:  ", intrest_installment)
    credit_amount = credit_amount - capital_installment
