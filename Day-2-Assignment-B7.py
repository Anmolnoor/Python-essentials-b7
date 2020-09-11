#!/usr/bin/env python
# coding: utf-8

# # List and it's Default functions:

# In[1]:


lst1 = ["a","b","c"]


# In[2]:


lst2 = ["d","e","a"]


# In[13]:


#  "cmp()" Compares elements of both lists.
#As mentioned in the comments, cmp doesn't exist in Python 3. any more but we can use it as following...
def cmp(a, b):
    return (a > b) - (a < b) 


# In[14]:


cmp(lst1 , lst2)


# In[15]:


# "len()" Gives the total length of the list.


# In[16]:


len(lst1)


# In[17]:


# "max()" Returns item from the list with max value.


# In[18]:


max(lst2)


# In[20]:


# "min()" Returns item from the list with min value.


# In[21]:


min(lst1) 


# In[22]:


# "list()" Converts a tuple into list. (typecasting something like that).


# In[23]:


# Tuple 
tpl = ("A","E","F","k")


# In[31]:


list(tpl)


# In[30]:


tpl


# #  Dict - Dictionary Functions

# In[32]:


# "cmp()"  Compares elements of both dict.


# In[33]:


dit1 = {"a":"d","b":"e","c":"f"}


# In[34]:


dit2 = {"g":"j","h":"k","i":"l"}


# In[41]:


#As mentioned in the comments, cmp doesn't exist in Python 3. any more but we can use it as following...
def cmp2(a, b):
    return (a > b) - (a < b)


# In[42]:


cmp2(dit1 , dit2)


# In[43]:


# TypeError: '>' not supported between instances of 'dict' and 'dict'


# In[44]:


# "str(dict)" Produces a printable string representation of a dictionary


# In[45]:


str(dit1)


# In[46]:


# "type(variable)" Returns the type of the passed variable. If passed variable is dictionary, then it would return a dictionary type.


# In[51]:


type(tpl)


# In[52]:


type(dit1)


# In[53]:


type(lst1)


# # Sets

# In[54]:


# "add*()" Adds an element to the set


# In[55]:


st = {1,2,3,4,5,6,7,8,9}


# In[57]:


st.add(10)


# In[58]:


st


# In[59]:


# "remove()" Removes the specified element


# In[60]:


st.remove(9)


# In[61]:


st


# In[62]:


# "pop" Removes an element from the set


# In[63]:


st.pop()


# In[64]:


st


# In[65]:


# "copy()" Returns a copy of the set


# In[67]:


st.copy()


# In[69]:


# "clear()" Removes all the elements from the set


# In[70]:


st.clear()


# In[71]:


st


# # Tuple 

# In[72]:


tpl


# In[73]:


# "count()" Returns the number of times a specified value occurs in a tuple


# In[76]:


tpl.count("E")


# In[77]:


# "index()" Searches the tuple for a specified value and returns the position of where it was found


# In[78]:


tpl.index("F")


# # String

# In[79]:


# "capitalize()" Converts the first character to upper case


# In[80]:


txt = "this is the simple string for the test or perform the basic function of python on it to observe the outcomes" 


# In[83]:


print(txt.capitalize())


# In[84]:


# "casefold()" Converts string into lower case


# In[85]:


txt1 = "THIS IS THE TXT1 CAPITALIZE STRING TO CHECK OUT THAT THE CASEFOLD IS WORKING OR NOT"
print(txt1.casefold())


# In[86]:


# "count()" Returns the number of times a specified value occurs in a string


# In[88]:


txt2 = "This is a String to test the Count function of the python." 
print(txt2.count("t"))


# In[89]:


# "encode()" Returns an encoded version of the string


# In[90]:


txt3 = "This is the String to test the encode in python"
print(txt3.encode())


# In[95]:


txt3 = "This is the String to test the encode in python"
print(txt3.encode(encoding="ascii",errors="ignore"))


# In[96]:


# "strip()" Returns a trimmed version of the string


# In[98]:


txt4 = "This Is The String To Checkout The Strip In Python."
print(txt4.strip("The"))


# In[106]:


txt5 = "This Is The String To Checkout The Strip In Python."
print(txt5.strip("Strip"))


# In[ ]:




