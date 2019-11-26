#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests


# In[2]:


r = requests.get('https://reqres.in/api/users',verify=False)
if r.status_code != 200:
    print("Error GET /tasks/ {}".format(resp.status_code))


# In[3]:


names = []
for resp in r.json()['data']:
    p = [resp["first_name"],resp["last_name"]]
    names.append(' '.join(p))
    print('{0}: {1}'.format(resp["id"],resp["first_name"]+" "+resp["last_name"]))


# In[4]:


names


# In[ ]:




