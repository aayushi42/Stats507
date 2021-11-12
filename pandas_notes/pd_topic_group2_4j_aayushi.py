
# # Problem Set 4

# ## Question 0

# Aayushi Sinha
# 
# aayushi@umich.edu
# 
# 
# ##  Timedeltas in Pandas

# ### Class pd.Timedelta
# 
# * It represents a duration of time or date. Easy to use for date or time manipulations.
# * It is a similar to the python class of datetime.timedelta.
# * It is expressed in difference units, e.g. days, hours, minutes, seconds.

# In[1]:


import pandas as pd
from datetime import datetime, timedelta

#Calculating the number of days between two dates.
present_date = datetime.now()
print ("Present Date", str(present_date))
future_date = present_date + timedelta(days = 6)
print("Future Date", str(future_date) )

print("Days left", str(present_date - future_date))


# ### Parsing 
# * Prasing through a string or an integer with units in the argument can create a timedelta object.
# * pd.to_timedelta can convert a scalar, array, list, or series from a recognized timedelta 
#   format/ value into a Timedelta type.

# In[3]:


#Parsing and to_timedelta
print (pd.Timedelta('2 days 2 hours 15 minutes 30 seconds'))
#Converting to timedelta object
pd.to_timedelta("1 days 06:05:01.00003")


# ### Operations
# 
# * You can construct timedelta64[ns] Series/Dataframes through subtraction operations and operate on the series/dataframes.
# * NaT values are supported in timedelta series.
# * min, max and the corresponding idxmin, idxmax operations are supported. Even negate can be used.

# In[5]:


# Operation Examples
s = pd.Series(pd.date_range('2012-1-1', periods=3, freq='D'))
td = pd.Series([ pd.Timedelta(days=i) for i in range(3) ])
df = pd.DataFrame(dict(A = s, B = td))
df['C']=df['A']+df['B']
df['D']=df['C']-df['B']
print(df)
