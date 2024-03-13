#!/usr/bin/env python
# coding: utf-8

# # To get Latitude and Longitude from Place Name

# In[1]:


import requests
import json
import pandas as pd


# # Enter Place Name Here:
# Use ',' to enter multiple Places

# In[ ]:


villlist=input('Enter the Place Name ')
villlist = villlist.split(',')


# # Enter the Place Name gurdaspur,mukerian,hoshiarpur
# To Get Places names from PUNJAB.xlsx File

# In[ ]:


lat=[]
long=[]
place=[]
district=[]

#Places to test the code
#villlist= ['Barnala','zira','Hoshiarpur','Kapurthala','Ludhiana','Mansa','Moga','Tarn Taran']

for vill in villlist:
    vill1=vill.replace(" ","+")
    url="https://nominatim.openstreetmap.org/search?q="+vill1+"&format=json&polygon=1&addressdetails=1"
    d=requests.get(url)
    data=d.json()
    place.append(vill)
    
    if(len(data)==0):
        
        lat1='NA'
        long1='NA'
        dist1='NA'
        lat.append(lat1)
        long.append(long1)
        district.append(dist1)
        
    else:
        for sr in data:
            try:
                x1=sr['address']['state_district']
                x2=sr['address']['state']
                x3=sr['address']['country_code']
                #print(x3,x2,x1)
                x=1
            except:
                x=0
            
            if(x==1):
                lat1=0
                long1=0
                dist1='NA'
                if((sr['address']['country_code']=='in')&(sr['address']['state']=='Punjab')):
                    
                    lat1=(sr['lat'])
                    long1=(sr['lon'])
                    dist1=(sr['address']['state_district'])
                    #print(villlist.index(vill),"  ",vill)
                    break    
            else:
                lat1=0
                long1=0
                dist1='NA'
                
        lat.append(lat1)
        long.append(long1)
        district.append(dist1)
        
    print(villlist.index(vill)+1," ",vill," is in ",district[-1]," and has Cordinates",lat[-1], long[-1])


# # To Create Dataframe and Import in Excel Format

# In[ ]:


LLData= pd.DataFrame()
LLData['Place']=place
LLData['Latitude']=lat
LLData['Longitude']=long
LLData['District']=district
LLData.head()
#LLData.to_excel('Place_LL.xlsx',index=False)
LLData.to_excel('D:\S.T.U.D.Y\Place.xlsx',index=False)


# In[ ]:





# In[ ]:




