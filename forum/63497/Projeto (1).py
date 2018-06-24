


import numpy as np


# In[2]:


import pandas as pd


# In[5]:

# # Usando Keras Redes Neurais

# In[ ]:


#previsores = base.iloc[:, 1:4].values


# In[3]:


test =pd.read_csv('/Radhe1/CEFET/MineraçãoDados_CEFET/Projeto/The UNSW-NB15 data set description/UNSW_NB15_testing-set.csv')


# In[4]:


train = pd.read_csv('/Radhe1/CEFET/MineraçãoDados_CEFET/Projeto/The UNSW-NB15 data set description/UNSW_NB15_training-set.csv')


# In[5]:


previsores_train = train.iloc[:,train.columns.isin(('sload','dload',
                                                   'spkts','dpkts','swin','dwin','smean','dmean',
'sjit','djit','sinpkt','dinpkt','tcprtt','synack','ackdat','ct_srv_src','ct_srv_dst','ct_dst_ltm',
 'ct_src_ltm','ct_src_dport_ltm','ct_dst_sport_ltm','ct_dst_src_ltm')) ].values


# In[6]:


classe_train = train.iloc[:, -1].values


# In[48]:


previsores_train


# In[46]:


previsores_train.shape


# In[7]:


previsores_test = test.iloc[:,test.columns.isin(('sload','dload',
                                                   'spkts','dpkts','swin','dwin','smean','dmean',
'sjit','djit','sinpkt','dinpkt','tcprtt','synack','ackdat','ct_srv_src','ct_srv_dst','ct_dst_ltm',
 'ct_src_ltm','ct_src_dport_ltm','ct_dst_sport_ltm','ct_dst_src_ltm')) ].values


# In[ ]:


#df.loc[:, df.columns.isin(list('BCD'))]


# In[ ]:


#https://stackoverflow.com/questions/13021654/get-column-index-from-column-name-in-python-pandas


# In[8]:


classe_test = test.iloc[:, -1].values


# In[47]:


classe_test


# In[ ]:


train.columns


# In[ ]:


test.columns


# In[ ]:


train.columns.get_loc('sload')


# In[ ]:





# In[ ]:





# In[50]:


X_train2,y_train2 = previsores_train,classe_train

X_test2,y_test2 = previsores_test,classe_test


# In[40]:





# In[11]:


import keras


# In[12]:


from keras.models import Sequential


# In[13]:


from keras.layers import Dense


# In[14]:


classificador_rede_neural = Sequential()


# # Camadas Ocultas e de Saída

# camadas ocultas = (entradas + saídas)/2 #estimando o numero de neurônios em camada oculta
# 
# temos:len(train.columns) - 1   atributos previsores
# 
# 1 classe

# In[51]:


features = previsores_train.shape[1] #num de atributos previsores


# In[58]:


print('numero de features', features)


# In[32]:


camadas_ocultas = round((features +1)/2 )


# In[33]:


print(camadas_ocultas)


# In[ ]:


#input_dim é o número de atributos


# In[72]:


classificador_rede_neural.add(Dense(units=camadas_ocultas, activation='relu',input_dim = features ))#primeira camada


# In[65]:


classificador_rede_neural.add(Dense(units=camadas_ocultas, activation='relu' ))#segunda camada


# In[66]:


classificador_rede_neural.add(Dense(units=1, activation='sigmoid' ))#camada de saída. a saída é binária, logo units=1


# In[ ]:


#sigmoid pq a saida é binaria: gera uma probabilidade


# In[67]:


classificador_rede_neural.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])


# In[ ]:


#classificador_rede_neural.fit(X_train2.values,y_train2.values,batch_size=10,epochs =100)#é treino: trocar


# In[38]:


X_train2.shape


# In[39]:


y_train2.shape


# In[69]:


#classificador_rede_neural.fit(X_train2,y_train2,batch_size=10, epochs=10000)#é treino: trocar


# In[73]:


classificador_rede_neural.fit(X_train2,y_train2)#é treino: trocar

