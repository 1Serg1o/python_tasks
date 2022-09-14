'''
User have to guess the hiden number, every time he type wrong number program suggest if number is too much or not enought
'''

hiden_number = 47

print("GUESS THE HIDEN NUMBER")

while True:
    x = int(input("Enter your number: "))
    if x > hiden_number:
        print("Too much")
    elif x < hiden_number:
        print("Not enought")
    else:
        print("BRAVO, you have guess the number")
        break


    
    
   


