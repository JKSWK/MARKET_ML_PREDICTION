#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
import glob
import os


# In[8]:


#sv_files = glob.glob("NIKKEI_d.csv","DAX_d.csv","WIG20_d.csv","DJI_d.csv","SP500_d.csv","JAPAN10B_d.csv","GERMANY10B_d.csv",
#                    "POLAND10B_d.csv","USA10B_d.csv","USA30B_d.csv","WHEAT_d.csv","COPPER_d.csv","PALLADIUM_d.csv",
#                   "IRON_d.csv","GOLD_d.csv","NATGAS_d.csv","OILBRENT_d.csv","USDJPY_d.csv","EURUSD_d.csv",
#                   "GBPUSD_d.csv","USDCHF_d.csv","EURJPY_d.csv","GLOBAL_INDUSTRY_d.csv","GLOBAL_ENERGY_d.csv",
#                    "GLOBAL_FINANCE_d.csv","GLOBAL_HEALTHCARE_d.csv","GLOBAL_TECH_d.csv",
#                    "SPTECH_d.csv","SPENERGY_d.csv","SPVIX_d.csv")


# In[17]:


csv_files = glob.glob("*.csv")


# In[18]:


csv_files


# In[104]:


merged_df = pd.DataFrame()


# In[105]:


merged_df = pd.read_csv(csv_files[0], usecols=["Data","Zamkniecie"]).drop(columns = "Zamkniecie")
for file in csv_files[0:]:
    df = pd.read_csv(file, usecols=["Data", "Zamkniecie"])
    filename = os.path.splitext(os.path.basename(file))[0]
    df = df.rename(columns={"Zamkniecie":filename})
    merged_df = merged_df.merge(df, how="left", on="Data")


# In[106]:


merged_df


# In[107]:


merged_df.sample(20)


# In[108]:


merged_df.isna().sum()


# In[109]:


merged_df.dropna()


# In[110]:


merged_df.to_csv('merged_data.csv', index=False)



# In[ ]:





# In[ ]:





# In[84]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




