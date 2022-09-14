"""
Program counts your creditworthiness on credit amount you need to purchase a property
User type value of the property, than type how much of own contribution he have.
User must have min. 10% of own contribuiton so when he types less than program ask him to type true value.
After all, user type his earnings and program count if he have creditworthiness on credit ammount.
"""

property_value = int(input('Enter property value: '))
own_contribution = 0

while own_contribution < (property_value * 0.1):
    print('Loan to value ratio must be min 10%')
    own_contribution = int(input('Enter the ammount of your own contribution: '))

credit = property_value - own_contribution
print('CREDIT: ' + str(credit))   

earnings = int(input('Enter your earnings: '))
if credit <= (earnings * 10):
    print('Congratulations, your creditworthiness is enought to get', credit)
else:
    print('We sorry, your creditworthiness is not enought')
