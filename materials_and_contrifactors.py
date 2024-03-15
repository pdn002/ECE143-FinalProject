#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Spill_Incidents.csv')


# In[2]:


# Remove empty cells from the cols 
data = data.dropna(subset=['Contributing Factor', 'Material Name','Material Family'])


# In[3]:


unique_values_set = set()
unique_values_set.update(data['Contributing Factor'].unique())

print(unique_values_set)


# In[4]:


# Combine Unknown,Other and Missing Code in Old Data - Must be fixed to Unknown 
data['Contributing Factor'] = data['Contributing Factor'].replace(['Other','Missing Code in Old Data - Must be fixed'], 'Unknown')


# In[7]:


data['Material Name'] = data['Material Name'].str.replace('.*fuel oil.*', 'fuel oil', regex=True)
data['Material Name'] = data['Material Name'].str.replace('.*other.*', 'other', regex=True)


# In[18]:


# Plot of Contributing Factors
cf_count = data['Contributing Factor'].value_counts()

# Plot the graph
plt.figure(figsize=(10, 6))
cf_count.plot(kind='bar', color='skyblue')
plt.title('Leading contributors of the spills')
plt.xlabel('Contributing Factors')
plt.ylabel('Number of spills')
plt.show()


# In[25]:


mn_high = data['Material Name'].value_counts()

# Filter values with count > 100
filtered_values = mn_high.head()

# Plot the graph
plt.figure(figsize=(10, 6))
filtered_values.plot(kind='bar', color='skyblue')
plt.title('Top 5 materials spilt')
plt.xlabel('Material Name')
plt.ylabel('Frequency')
plt.show()


# In[16]:


# Plot of Material Name
mf_count = data['Material Family'].value_counts()

# Plot the graph
plt.figure(figsize=(10, 6))
mf_count.plot(kind='pie', autopct='%1.1f%%', colors=['skyblue', 'lightcoral', 'lightgreen', 'orange', 'lightpink'])
plt.title('Frequency of each material family in the spills')
plt.ylabel('')
plt.show()


# In[ ]:




