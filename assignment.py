
# coding: utf-8

# In[21]:


a= int (input ("please enter the amount"))
b= float(input("please enter rate of the interest in % "))
c= int(input("enter number of years for investment"))
d=((1+(10/100))**c)
e=d*a
print ("after ",c," years your principal amount ",a," over an interest rate of ",b," % will be ",e)


# # Euclidean distance

# In[9]:


a= float(input ("enter co ordinate for x1 "))
b= float(input("enter co ordinate for x2 "))
c= float(input("enter co ordinate for y1 "))
d= float(input("enter co ordinate for y2 "))
e=(b-a)**2
f=(d-c)**2
import math
g=math.sqrt((e+f))
print (g)


# # Feet to centimetre convrter

# In[10]:


a=float(input("enter height in feet: "))
b=a*30.48
print("there are ",b," cm in ",a," ft")


# # Bmi calculator
# 

# In[ ]:


a=float(input("enter height in m2: "))
b=float(input("enter weight in kg: "))
c=(b)/a
print ("your bmi is ",c)


# # Sum of n positive numbers

# In[15]:


n=int(input("enter the value of n"))
sum=(n*(n+1))/2
print (sum)


# # Digits sum of a number

# In[27]:


n=int(input("Enter a number:"))
tot=0
while(n>0):
    dig=n%10
    tot=tot+dig
    n=n//10
print("The total sum of digits is:",tot)


# # Calculate the area of the circle
#       

# In[7]:


n=float(input("enter the radius of a circle "))
pi=3.142
area=pi*(n**2)
print("the area of a circle is ",area)


# # check number either positive, negative or zero

# In[8]:


n=int(input("enter the number"))
if (n>0):
    print("the number is positive")
elif (n<0):
    print("the number is negative")
else:
    print("the number is equal")
    


# # Divisibility check of two numbers

# In[10]:


n=int(input("enter the numerator"))
b=int(input("enter the denominator"))
if(n%b==0):
    print("the number is totally divisible by the denominator")
else:
    print("the number is not fully divisible by the denominator")
    


# # Calculate Volume of a sphere

# In[12]:


a=int(input("enter the radius of sphere "))
b=(4/3)*(3.14)*(a**3)
print("the volume of the sphere is ",b)


# # Check if number is even or odd

# In[14]:


a=int(input("enter the number"))
if(a%2==0):
    print("the number is even")
else:
    print("the number is odd")


# # Copy string n times

# In[17]:


a=input("enter any string ")
b=int(input("how many times you want to print this "))
for c in range (0,b):
    print(a)


# # Vowel tester

# In[ ]:


a=input("enter any character")
if (a=="a" or a=="e" or a=="i"or a=="o"or a=="u"):
    print("the character is vowel")
else:
    print("the character is consonent")

