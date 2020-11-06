#!/usr/bin/env python
# coding: utf-8

# In[154]:


#Stacked bar chart showing percentage dstribution of covid statsics grouped on WHO Region


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#import the csv data
df=pd.read_csv("/Users/roop/Desktop/country_wise_latest.csv")


#Create the %age of individual column Recovered,Deaths and Active
recovered=(df.groupby('WHO Region')['Recovered'].sum())/(df.groupby('WHO Region')['Confirmed'].sum())*100

deaths=(df.groupby('WHO Region')['Deaths'].sum())/(df.groupby('WHO Region')['Confirmed'].sum())*100

active=(df.groupby('WHO Region')['Active'].sum())/(df.groupby('WHO Region')['Confirmed'].sum())*100

#Merge all 3 pandas series into dataframe
df=pd.concat([recovered,deaths,active],axis=1)

#Name the dataframe columns
df.columns=['Recovered','Deaths','Active']

#create a stacked bar chart
ax = df.plot.barh(stacked=True, figsize=(8, 6),color='gry')
#color_list = ['b', 'g', 'r']

# .patches is everything inside of the chart
for i,rect in enumerate(ax.patches):
    # Find where everything is located
    height = rect.get_height()
    width = rect.get_width()

    x = rect.get_x()

    y = rect.get_y()
 
    
    # The height of the bar is the data value and can be used as the label
    label_text = f'{width:.2f}%'  # f'{width:.2f}' to format decimal values
    
    # ax.text(x, y, text)
    label_x = x + width / 2
    label_y = y + height / 2
    
    # only plot labels greater than given width
  

    if width > 0:
        ax.text(label_x, label_y, label_text, ha='center', va='center', fontsize=8)
      
# move the legend
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

# add labels
ax.set_ylabel("Region", fontsize=18)
ax.set_xlabel("Percent", fontsize=18)
plt.show()


# In[191]:


#Showing the COVID trends of Confirmed and Deaths in US using Line Chart
import pandas as pd
import matplotlib.pyplot as plt

#import the csv file into dataframe
df=pd.read_csv("/Users/roop/Desktop/usa_county_wise.csv")
#Create a MonthYear column
df["MonthYear"]=pd.to_datetime(df["Date"]).dt.to_period('M')
#Create Confirmed and Death summation over the month in form of Pandas series
Confirmed=df.groupby('MonthYear')['Confirmed'].sum()
Death=df.groupby('MonthYear')['Deaths'].sum()
#create a dataframe
dfnew=pd.concat([Confirmed,Death],axis=1)
dfnew.plot(figsize=(12, 10), linewidth=2.5)
plt.ylabel("Confirmed and Deaths")
plt.title('Confirmed and Death vs Month Year')


# In[ ]:





# In[ ]:




