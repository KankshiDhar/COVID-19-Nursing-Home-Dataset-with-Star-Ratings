#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importing libraries for Exploratory Analysis of Dataset
import pandas as pd
import os


# In[63]:


#Importing the file for star rating
star_rating=pd.read_csv(r'C:\Users\kanks\OneDrive\Desktop\Star Rating.csv', encoding = 'utf_8')


# In[3]:


#Information on Star rating dataframe
star_rating.info()


# In[4]:


#Finding null values in Star Rating dataframe
print(star_rating.isnull().sum())


# In[64]:


#Importing the csv file for the Nursing home dataset
nursing_home=pd.read_csv(r'C:\Users\kanks\OneDrive\Desktop\Nursing_Home.csv', encoding = 'utf_8')


# In[6]:


#Finding Nursing home dataframe attribute information 
nursing_home.info()


# In[7]:


#Finding null values in Nursing Home Dataframe
print(nursing_home.isnull().sum())


# In[73]:


#Performing a left join using 'Federal Provider Number' as key for both datasets to combine & analyze values
combined=pd.merge(nursing_home, star_rating, left_on="Federal Provider Number", right_on="Federal Provider Number", how="left")


# In[66]:


combined.dtypes


# In[11]:


#Test Command to check joined values for a Federal Provider Number
combined.loc[combined['Federal Provider Number'] == '335797']


# In[35]:


get_ipython().system('pip install scikit-learn')


# In[12]:


#Importing libraries for Data Analysis
import sklearn as skl
import numpy as np
import seaborn as sns #visualisation
import matplotlib.pyplot as plt #visualisation


# In[40]:


#Print values for Combined
combined.head()


# In[41]:


#Finding null & non-nul values of Combined dataset
combined.info()


# In[42]:


#Find null values in Combined Dataframe
print(combined.isnull().sum())


# In[43]:


# Checking the data types
combined.dtypes.head(20)


# In[50]:


# Total number of rows and columns
combined.shape


# In[ ]:


#r= np.corrcoef(combined['Overall Rating'], combined['Number of All Beds'])


# In[47]:


sns.boxplot(x= combined['Overall Rating'])


# In[126]:


sns.boxplot(x= combined['Total Resident Confirmed COVID-19 Cases Per 1,000 Residents'])


# In[107]:


# Plotting a scatter plot of Overall Rating with Number of Available Beds
fig, ax = plt.subplots(figsize=(10,6))
ax.scatter(combined['Number of All Beds'], combined['Overall Rating'])
ax.set_xlabel('Number of Beds')
ax.set_ylabel('Overall Rating')
plt.show()


# In[21]:


from scipy import stats


# In[67]:


list(combined.columns.values)


# In[127]:


#Finding Correlation Coefficients to see Relations between attributes
x=combined
Correlation = x.corr()
Correlation


# In[129]:


Correlation.to_csv('C:/Users/kanks/OneDrive/Desktop/Correlation.csv')


# In[109]:


#Group by state, average for rating, sum observations in each
Grouped_state = x.groupby(['Provider State_x']).mean()
Grouped_state.head()


# In[110]:


#Highest & Lowest Overall Rating by State in Ascending order
y=Grouped_state.sort_values(by=['Overall Rating'])
y['Overall Rating']


# In[111]:


#Highest & Lowest Quality Measure Rating by State in Ascending order
Q =Grouped_state.sort_values(by=['QM Rating'])
Q['QM Rating']


# In[113]:


#Highest & Lowest Residents Total all Deaths by State in Ascending order
R =Grouped_state.sort_values(by=['Residents Total All Deaths'])
R['Residents Total All Deaths']


# In[114]:


#Highest & Lowest Residents Total COVID-19 Deaths by State in Ascending order
D =Grouped_state.sort_values(by=['Residents Total COVID-19 Deaths'])
D['Residents Total COVID-19 Deaths']


# In[123]:


#Highest & Lowest Total Resident Confirmed COVID-19 Cases Per 1,000 Residents by State in Ascending order
a =Grouped_state.sort_values(by=['Total Resident Confirmed COVID-19 Cases Per 1,000 Residents'])
a['Total Resident Confirmed COVID-19 Cases Per 1,000 Residents']


# In[124]:


#Highest & Lowest Total Resident COVID-19 Deaths Per 1,000 Residents by State in Ascending order
b =Grouped_state.sort_values(by=['Total Resident COVID-19 Deaths Per 1,000 Residents'])
b['Total Resident COVID-19 Deaths Per 1,000 Residents']


# In[125]:


#Highest & Lowest Health Inspection Rating by State in Ascending order
c =Grouped_state.sort_values(by=['Health Inspection Rating'])
c['Health Inspection Rating']


# In[ ]:




