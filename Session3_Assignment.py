
# coding: utf-8

# In[1]:


#Write a Python Program to implement your own myreduce() function which works exactly
#like Python's built-in function reduce()

def multiply(x,y): return x*y
x = 5
y = 10

import functools
tot = functools.reduce(multiply, range(5, 10))
print ('reduce('+str(x)+','+str(y)+')=' ,tot)

def myreduce(a,b):
    tot = 1
    for i in range(a,b):
        tot = tot * i
        print (i,tot)
    print ('myreduce('+str(a)+','+str(b)+')=' ,tot)

myreduce(x,y)


# In[ ]:


#Write a Python program to implement your own myfilter() function which works exactly like
#Python's built-in function filter()


# In[2]:


age = [5, 12, 17, 18, 24, 32]
adults = filter(lambda x: x > 18 , age)
print("filter function = ")
for x in adults:
  print(x)

def myfilter(a):
    l = []
    for i in a:
        if( i > 18):
            l.append(i)        
    print ('myfilter function = ')
    for x in l:
      print(x)

myfilter(age)


# In[ ]:


# Implement List comprehensions to produce the following lists.
#Write List comprehensions to produce the following Lists
#['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]


# In[3]:


letters = []

for letter in 'ACADGILD':
    letters.append(letter)

print(letters)


# In[ ]:


#['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']


# In[4]:


letters = []

for letter in 'xyz':
    letters.append(letter)
    letters.append(letter+letter)
    letters.append(letter+letter+letter)
    letters.append(letter+letter+letter+letter)
    
print(letters)


# In[ ]:


#['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']


# In[5]:


letters = []

for letter in 'xyz':
    letters.append(letter)
for letter in 'xyz':    
    letters.append(letter+letter)
for letter in 'xyz': 
    letters.append(letter+letter+letter)
for letter in 'xyz': 
    letters.append(letter+letter+letter+letter)
    
print(letters)


# In[ ]:


#[[2], [3], [4], [3], [4], [5], [4], [5], [6]]


# In[6]:


y = 1
l4 =[]
for x in range(1,4):
    l1 = [x+y for x in range(1,2)]    
    l4.append(l1)
    y = y+1

z=2
for x in range(1,4):
    l2 = [x+z for x in range(1,2)]    
    l4.append(l2)
    z = z+1

w=3
for x in range(1,4):
    l3 = [x+w for x in range(1,2)]    
    l4.append(l3)
    w = w+1
print(l4)


# In[ ]:


#[[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]


# In[7]:


y = 1
l2 =[]
for x in range(1,5):
    l1 = [x+y for x in range(1,5)]    
    l2.append(l1)
    y = y+1

print(l2)


# In[ ]:


#[(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]


# In[8]:


list1 = [ 1,2,3 ]
list2 = [ 1,2,3 ]
merged_list = [ (y,x) for x in list1 for y in list2 ]
print (merged_list)


# In[ ]:


#3. Implement a function longestWord() that takes a list of words and returns the longest one.


# In[9]:


def longestWord(word_list): 
    count = 0    
    for i in word_list: 
        if len(i) > count: 
            count = len(i)
            word = i
    return ("The Longest String is " + word)

words = ['acad','acadgild','gild']

longestWord(words)

