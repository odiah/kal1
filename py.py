print("We're about to find the average of just three numbers")
print("This is my first official python code in up to three years, by the way")
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
avg = (num1+num2+num3)/3
print("The average of the three numbers is: ", avg)
step2 = [num3,num1,num2]
for lowest in step2:
    if(num1>num2) and (num1>num3):
        num1 = lowest
        if(num2>num1) and (num2>num3):
            num2 = lowest

print("\n BTW, the highest of the numbers you typed in is: ", lowest)
