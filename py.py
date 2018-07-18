print("We're about to find the average of just three numbers")
print("This is my first official python code in up to three years, by the way")
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
avg = (num1+num2+num3)/3
print("The average of the three numbers is: ", avg)
numlist = [num3,num1,num2]
hold_large_num = 0
for num in numlist:
    if(num>hold_large_num):
        hold_large_num = num
        
print("\n BTW, the highest of the numbers you typed in is: ", hold_large_num)

#pardon my lack of use of comoments, really
