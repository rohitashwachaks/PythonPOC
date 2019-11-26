#!/usr/bin/env python
# coding: utf-8

# In[1]:


import datetime


# In[25]:


inp = '2019-03-16 15:00:00'
#inp = input("enter time (YYYY-MM-DD HH:MM:SS): ")
inp_date,inp_time = map(str, inp.split(" "))
inp_date_year, inp_date_month, inp_date_date = map(int,inp_date.split("-"))
inp_time_hour, inp_time_minute, inp_time_second = map(int,inp_time.split(":"))

inp_date_year, inp_date_month, inp_date_date,inp_time_hour, inp_time_minute, inp_time_second


# In[26]:


hour_angle = ((30*inp_time_hour)%360) + (0.5*inp_time_minute)
# 24 hrs = 720 degree -> 1 hr = 30 degree. modulo 360 to find angle of hour hand from 12'oclock
# 60 mins = 1 hr = 30 degree -> 1 min = 1/60hr = 0.5 degree
minute_angle = (6*inp_time_minute)
# 60 mins = 360 degree -> 1 min = 6 degree.
hour_angle,minute_angle


# In[27]:


angle_diff = hour_angle-minute_angle
ans = int(min(abs(angle_diff),360-abs(angle_diff)))
ans


# In[ ]:




