import requests
import pyttsx3
import os

# you can type multiline print with the triple single and double quotes.
# for making multi lines string we can use directly '''   '''' in our print block 


# Question No. 1

"""

print(
'''
Twinkle twinkle little star.
How I wonder what you are.
Up above the world so high.
Like a diamond in the sky.
Twinkle twinkle little star.
How I wonder what you are.

Twinkle twinkle little star.
How I wonder what you are.
Up above the world so high.
Like a diamond in the sky.
Twinkle twinkle little star.
How I wonder what you are.
'''
)

response = requests.get("https://api.github.com")

print("status code:",response.status_code)
# print("Content:", response.json())

engine = pyttsx3.init()
engine.say("Hi i am learning python.")
engine.runAndWait()


speak = pyttsx3.speak("I am fardeel")

"""
# Print the directories with os (Question 4)

# contents = os.listdir("/")
# # print(os.listdir(contents))
# for item in contents:
#     print(item)


# Path of the directory (you can change this to any folder path)
path = "."

# List all files and folders inside the path
contents = os.listdir(path)

print(f"Contents of directory '{path}':")
for item in contents:
    print(item)