#!/usr/bin/env python
# coding: utf-8

# In[2]:


"""Use the dictionary, port1 = {21: "FTP", 22:"SSH", 23: "telnet", 80: "http"}, and make a new dictionary in which keys become 
values and values become keys, as shown: Port2 = {“FTP":21, "SSH":22, “telnet":23,"http": 80}"""

port1={21:"FTP",22:"SSH",23:"telnet",80:"http"}
print(port1)
port2 = {value:key for key, value in dict.items(port1)}
print(port2)Q


# In[3]:


"""Take a list of tuple as shown below. [(1,2), (3,4), (5,6),(4,5)] Make a new list which contains sum of number of tuples."""


list1=[(1,2),(3,4),(5,6),(4,5)]
res=[]
for each in range(0,len(list1)):
    a,b=list1[each]
    res.append(a+b)
print(res)


# In[4]:


"""Take a list as shown below [(1,2,3), [1,2], ['a','hit','less']] The List contains tuple and lists. 
Make the elements of inner lists and tuples to outer list"""


list1=[(1,2,3),[1,2],['a','hit','less']]
list2=[]
list2=[i for each in list1 for i in each]
print(list2)

