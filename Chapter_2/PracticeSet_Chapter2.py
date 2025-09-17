

# write a python program to print two numbers 

a = 5 
b = 7 
print("The Sum of a and b is ",a+b)


# .... to fint a remainder when a number is devided by z 

# Logically hamain aik Number chahye ho ga user se uske lye ham user se input lety hian chalo 

# number = int(input("Enter a First number:"))

# z = int(input("Enter the Z number you want to devide your number:"))

# remainder = number % z
# print(f"The remainder when {number} is divided by {z} is {remainder}")


# check the type of a variable getting it from the input

# user_input = input("Enter a random thing:")

# new_user_input = int(user_input)

# print("Random User Input value is",type(user_input))
# print("New user input is:",type(new_user_input))






#use comparison operator to find out 
# a is grater then b or not ? 

a = input("Enter the value for a:")
b = input("Enter the value for b:")

result = a > b 
print(a,">",b,result)



# Question 4 
# Find the average of two number get from the user 


#Average ka matlab hota hai:
# 👉 (Sum of values) ÷ (Number of values)


# number_1 = int(input("Enter the First Number:"))
# number_2 = int(input("Enter the Second Number:"))

# print(f"The average of {number_1} and {number_2} is: {(number_1 + number_2)/2}")




# Question 5
# calculate the square of a number given by user

sqr_number = int(input("Enter the Number you want to sqr:"))

print(sqr_number*sqr_number)

# with Exponent operator
# a ** b   →  a raised to the power b
number_for_power = int(input("Enter Number you want to Power:"))
power = int(input("Enter Number Power of a number:"))


print(number_for_power ** power)

# we can also use pow() [power function]

print(pow(sqr_number,3))
