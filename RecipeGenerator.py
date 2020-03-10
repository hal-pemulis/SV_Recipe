#!/usr/bin/env python
# coding: utf-8

# # Recipe Generator

# In[1]:


import pandas as pd
import random
import matplotlib.pyplot as plt
import json
from pprint import pprint


# In[2]:


filepath = "Resources/recipes_raw/recipes_raw_nosource_fn.json"

with open(filepath) as jsonfile:
    json_data = json.load(jsonfile)


# In[ ]:

# In[3]:


recipe = input("What would you like to cook today?\n")


# In[5]:


keys = []

for x in json_data:
    try:

        if recipe.lower() in json_data[x]['title'].lower():
            keys.append(x)
    except:
        1 == 1


# In[6]:


rand_num = random.randint(0,len(keys))
                   
print(f"{json_data[keys[rand_num]]['title']}\n")
print('Ingredients:')
for ingredient in json_data[keys[rand_num]]['ingredients']:
      print(f"• {ingredient}")
print('\nDirections:')
print(f"{json_data[keys[rand_num]]['instructions']}\n\n")

