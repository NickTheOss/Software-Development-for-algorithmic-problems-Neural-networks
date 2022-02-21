import keras
import numpy as np
import pandas as pd
import math
import sys
from keras import layers, optimizers, losses, metrics
from keras.models import load_model

model = load_model('WindDenseNN.h5') #load network



# It doesn't matter about this warning message: UserWarning: No training configuration found in save file: the model was *not* compiled. Compile it manually.
model.summary()
if (sys.argv[-2] == "-i"):  #parsing file via command line
        filename = sys.argv[-1]  
else:
        print('Wrong Input')
        sys.exit()   
l1 = [x for x in range(1,130)]   #make column list
df = pd.read_csv(filename,names=l1) # otherwise first line will be the column name in dataframe 
df = df.drop(df.columns[[0]], axis=1)   #drop first date column
result = model.predict(df)   #keras
l2 = [x for x in range(1,9)]     
actual = pd.read_csv('actual.csv',names=l2)  
actual = actual.drop(actual.columns[[0]], axis=1) 
actual = actual.to_numpy() 
diff_MAE = 0
diff_MSE = 0
n = len(actual)
print(result)  
for row in range (n):  
        for col in range(len(actual[0])):   
          
            diff_MAE = diff_MAE + math.fabs(actual[row][col]-result[row][col])  #mae
            diff_MSE = diff_MSE + math.pow(actual[row][col]-result[row][col],2) #mse
mae = diff_MAE/n
mse = diff_MSE/n
mape = mae*100/n

t = pd.DataFrame(result)  #print results
with open('predicted.csv','w') as f:   #export to csv
    print('MAE: ',mae,'MAPE: ',mape," % ",'MSE: ',mse,'\n',t,file=f)
    
