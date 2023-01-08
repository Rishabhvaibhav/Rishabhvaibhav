#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# # Load CSV DATA

# In[2]:


import pandas as pd
airline_data = pd.read_csv('flights.csv')


# # Print Shape and Column

# In[3]:


print(airline_data.shape)
print(airline_data.columns)


# In[4]:


"""
Analysis:
* Flight airtime will depends on the distance between the source and destination airports.	
* Field ““sched_dep_time“ & “dep_time” will be completey depends on the “hour”  field.
* Hour and dep_time, scheduled_dep_time are highly correlated.
* Distance and air_time are highly correlated
* Arr_delay and dep_delay are also highly correlated
* dep_delay is highly correlated with arr_delay 
* distance is highly correlated with air_time 
* hour is highly correlated with dep_time 
* sched_dep_time is highly correlated with hour.

"""


# # Print Airline Data

# In[5]:


airline_data.head()


# # Data Information

# In[6]:


airline_data.info()


# # Calling Describe

# In[7]:


airline_data.describe()


# In[8]:


Airline_data = airline_data
print(Airline_data)


# In[9]:


#Find-out and fill the the missing values .
missing_values = Airline_data.isnull()


# In[10]:


#identify missing values
print(missing_values)


# In[11]:


#count the missing values
missing_values_count = Airline_data.isnull().sum()
print(missing_values_count)


# In[12]:


#fill the missing values to One 
Airline_data = Airline_data.fillna(1)
print(Airline_data)


# In[13]:


#To check the missing value is fill or not 
missing_values_count_check = Airline_data.isnull().sum()
print(missing_values_count_check)


# In[14]:


#Drop 'tailnumber' and 'year' fields as there will be not used for the Explotary data analysis.
Airline_data = airline_data.drop(columns=['TAIL_NUMBER','YEAR'])
Airline_data


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # Airline with highest and lowest mean speed

# In[15]:


print(airline_data.columns)


# In[16]:


# USe this Function because Speed = Distance / time
Airline_data['FLIGHT_SPEED'] = Airline_data['DISTANCE']/Airline_data['AIR_TIME']


# In[17]:


#print the flight speed data 
Airline_data['FLIGHT_SPEED']


# In[18]:


# use aggregate() function to get the average value of the columns in the dataframe
Mean_speed_Airline = Airline_data.groupby('AIRLINE').agg({'FLIGHT_SPEED':[np.mean]})
print(f'The Mean Speed of Airline : \n \n {Mean_speed_Airline}')


# In[19]:


Mean_speed_Airline[:14].plot(kind="bar",figsize=(12,5),color = ("orange"))
plt.xlabel("Airline",fontsize=(20))
plt.ylabel("Mean",fontsize=(20))
plt.title("Graph of Mean Speed Airline",fontsize=(20));


# In[20]:


# to find the highest mean speed of airline  i used idxmax 
# and the str() function converts the specified value into a string.

highest_airline_mean_speed = str(Mean_speed_Airline.idxmax())
print(f'The Highest Airline mean Speed is : \n \n{highest_airline_mean_speed}')


# In[21]:


# to find the Lowest mean speed of airline  i used idxmin 
Lowest_airline_mean_speed = str(Mean_speed_Airline.idxmin())
print(f'The Lowest Airline mean Speed is : \n \n{Lowest_airline_mean_speed}')


# # Airports most and least busy 

# In[22]:


print(airline_data.columns)


# In[23]:


# use aggregate() function to get the average value of the columns in the dataframe
#sorts a data frame in Ascending or Descending .
# Ascending = false means it is in Descreasing order that means the busiest airline is above
Most_Busiest_Airline= Airline_data.groupby(['DESTINATION_AIRPORT']).agg({'ARRIVAL_DELAY':[np.mean,np.size]}).sort_values(by=[('ARRIVAL_DELAY','mean')], ascending=False)
Most_Busiest_Airline.head()


# In[24]:


Most_Busiest_Airline[0:5].plot(kind="bar" , figsize=(8,3),color = ("Green"))
plt.xlabel("Destination Airport",fontsize=(10))
plt.ylabel("Mean",fontsize=(10),)


# In[25]:


print(f'the Most Busiest Airline is : \n \n {Most_Busiest_Airline.head(1)}')


# In[26]:


# Ascending = True means it is in Ascending order that means the least busy airline is above 
Least_busy_Airline  = Airline_data.groupby(['DESTINATION_AIRPORT']).agg({'ARRIVAL_DELAY':[np.mean,np.size]}).sort_values(by=[('ARRIVAL_DELAY','mean')], ascending=True)
Least_busy_Airline.head()


# In[27]:


Least_busy_Airline[0:5].plot(kind="bar" , figsize=(8,3),color = ("Blue"))
plt.xlabel("Destination Airport",fontsize=(10))
plt.ylabel("Mean",fontsize=(10),)


# In[28]:


print(f'the Least Busy Airline is : \n \n {Least_busy_Airline.head(1)}')


# # Months During which airports are most and least busy

# In[29]:


print(airline_data.columns)


# In[30]:


Airline_During_Month = Airline_data.groupby(['MONTH']).agg({'DEPARTURE_DELAY':[np.mean],'ARRIVAL_DELAY':[np.mean,np.size]})
Airline_During_Month


# In[31]:


# plot of Airline during Month 
Airline_During_Month['DEPARTURE_DELAY'][0:12].plot(figsize=(8,3),color = ("Red"))
plt.xlabel("MONTH",fontsize=(10))
plt.ylabel("DEPARTURE_DELAY",fontsize=(10),)


# In[32]:


Airline_During_Month['total_delay'] = Airline_During_Month[('DEPARTURE_DELAY','mean')] + Airline_During_Month[('ARRIVAL_DELAY','mean')]


# In[33]:


#Months During airports are most busy
# Ascending = False means it is in Descending order that means the bugiest airline is above 
Airline_During_Month.sort_values(by='total_delay', ascending=False)


# In[34]:


#Months During airports are  leastbusy
# Ascending = True means it is in Ascending order that means the least busy airline is above 
Airline_During_Month.sort_values(by='total_delay', ascending=True)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




