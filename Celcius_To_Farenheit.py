#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import tensorflow as tf


# In[2]:


df=pd.read_csv("Celsius+to+Fahrenheit.csv")
df.head()


# In[3]:


df.info()


# In[4]:


df.describe()


# In[5]:


sns.scatterplot(df['Celsius'], df['Fahrenheit'])


# In[6]:


X_train=df['Celsius']
y_train=df['Fahrenheit']


# In[7]:


model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(units=10, input_shape=[1]))
model.add(tf.keras.layers.Dense(units=5))
model.add(tf.keras.layers.Dense(units=2))
model.add(tf.keras.layers.Dense(units=1))
model.summary()


# In[13]:


model.compile(optimizer=tf.keras.optimizers.Adam(0.5),loss='mean_squared_error')
# model.compile(optimizer='Adam',loss='mean_squared_error')


# In[14]:


epoch_hist=model.fit(X_train,y_train,epochs=300)


# In[15]:


plt.plot(epoch_hist.history['loss'])
plt.title('Model Loss Progress During Training')
plt.xlabel('Epoch')
plt.ylabel('Training Loss')
plt.legend(['Training Loss'])


# In[16]:


model.get_weights()


# In[17]:


Temp_C = 1
Temp_F = model.predict([Temp_C])
print('Temperature in degF Using Trained ANN =', Temp_F)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




