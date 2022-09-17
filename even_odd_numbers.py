"""
User enter numbers. Whenever user enter 0 program shows how many numbers
he enter, grouped by even and odd numbers 

"""


even_count = 0
odd_count = 0

while True:
    x = int(input("Enter the number: "))
    if x == 0:
        print("even:", even_count)
        print("odd:", odd_count)
        break
    elif x % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
       
        
        

   
