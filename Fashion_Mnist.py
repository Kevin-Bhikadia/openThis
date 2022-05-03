#!/usr/bin/env python
# coding: utf-8

# In[63]:


import pandas as pd
import numpy as np
import seaborn as sns
import tensorflow as tf
import matplotlib.pyplot as plt


# In[64]:


train_df=pd.read_csv("fashion-mnist_train.csv")
test_df=pd.read_csv("fashion-mnist_test.csv")


# In[65]:


train_df.head()


# In[66]:


train_df.shape


# In[67]:


test_df.shape


# In[68]:


train=np.array(train_df, dtype='float32')


# In[69]:


test=np.array(test_df, dtype='float32')


# In[70]:


X_train=train[:,1:]/255
y_train=train[:,0]

X_test=test[:,1:]/255
y_test=test[:,0]


# In[71]:


X_train.shape


# In[72]:


X_train=X_train.reshape(X_train.shape[0],*(28,28,1))
X_test=X_test.reshape(X_test.shape[0],*(28,28,1))


# In[73]:


from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense


# In[74]:


model = Sequential()
model.add(Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)))
model.add(MaxPooling2D(2,2))
model.add(Conv2D(64, (3,3), activation='relu'))
model.add(MaxPooling2D((2,2)))
model.add(Conv2D(64, (3,3), activation='relu'))
model.add(MaxPooling2D(2,2))
model.add(Flatten())
model.add(Dense(64, activation='relu'))
model.add(Dense(10, activation='softmax'))
model.summary()


# In[75]:


model.compile(loss='sparse_categorical_crossentropy', optimizer='Adam', metrics=['accuracy'])


# In[76]:


history=model.fit(X_train,y_train,batch_size=512,epochs=20,verbose=1)


# In[ ]:




