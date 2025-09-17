

# input is a buil it function by we can take data form the user 

user_1 = input("Enter Your Name:")
user_2 = int(input("Enter Your Age:")) # when user will enter this will be stirng and i have to type cast it. 

print("Your name is:",user_1,"and your age is:", user_2)
print(user_1+user_2) #this is throw an error we can't add str + int directly to print it seperately we have to add a "," between

user_3 = int(input("Enter your Number:"))
print(type(user_1))
print(type(user_2))
print(type(user_3))