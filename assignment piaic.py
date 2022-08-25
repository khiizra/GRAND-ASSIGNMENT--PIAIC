#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Assign a message to a variable and then print that message
x = "Hello world!"
print(x)


# In[2]:


#Find a quote from a famous person you admire. Print the quote and the name of its author. Your output should look something 
#like the following, including the quotation marks:

name="Oscar Wilde, said,"
quote="Experience is merely the name men gave to their mistakes."
print(name," ",quote,' ') 


# In[3]:


#Calculate Area of a Circle: Write a Python program which accepts the radius of a circle from the user and compute the area.
Radius = float(input(" Enter radius of the circle: "))

print(" Input Radius:",Radius)
print ("Area of Circle with Radius " + str(Radius) + " is : " + str(3.141 * Radius**2))


# In[4]:


#Check Number either positive, negative or zero:: Write a Python program to check if a number is positive,
num = float(input("Enter a number: "))
if num > 0:
    print("Positive Number")
elif num == 0:
    print("Zero Entered")
else:
    print("Negative number")


# In[5]:


#Vowel Tester Write a Python program to test whether a passed letter is a vowel or not
Vowel = input(" Enter a character:")
if Vowel == 'A' or Vowel == "a" or Vowel == 'E' or Vowel == 'e' or Vowel == 'I' or Vowel == 'i' or Vowel == 'O' or Vowel == 'o' or Vowel == 'U' or Vowel == 'u':
    print('Letter',Vowel,"is Vowel")
else:
    print("Letter",Vowel,"is not Vowel")


# In[6]:



#BMI Calculator Write a Python program to calculate body mass index Program
Height = float(input("Enter Height in Cm: "))
Weight = float(input("Enter Weight in Kg:: "))
Height_m = Height / 100
print("Your body mass is: ", Weight / (Height_m * Height_m) ) 


# In[7]:


#Store the names of a few of your friends in a list called names. Print each person’s name by accessing each element in the 
#list, one at a time
name = ['Khizra' , 'erum' ,  'maliha' , 'Raheel' , 'laiba' , 'komal']
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])


# In[8]:


#Start with the list you used in Question 4, but instead of just printing each person’s name, print a message to them. 
#The text of each message should be the same, but each message should be personalized with the person’s name.
for friend in name:
    print(friend,"is a nice guy")


# In[9]:


#Make a python program that conatains your nine favourite dishes in a list called foods. Print the message, 
#The first three items in the list are:
foods = ['Pizza','burger','pizza','mommos','macroni','spheghetti','corn','nuggets','pasta']
print('The first three items in the list are',foods[0:3])
print('Three items from the middle of the list are',foods[3:6])
print('The last three items in the list are',foods[6:])


# In[10]:


#Start with your program from your last Question8. Make a copy of the list of foods, and call it friend_foods. Then, 
#do the following
#Add a new dish to the original list.
#Add a different dish to the list friend_foods.
#Prove that you have two separate lists
friends_food = foods[0:9]
foods.append("chicken roll")
friends_food.append("chapotla")
print(foods)
print(friends_food)


# In[11]:


#Print the message, My favorite pizzas are: and then use a for loop to print the first list.
#Print the message
print("My favorite pizza are : ")
for items in foods:
    print(items)


# In[ ]:




