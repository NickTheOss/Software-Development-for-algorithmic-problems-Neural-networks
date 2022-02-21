import keras
import numpy as np
import pandas as pd
import sys
from keras import layers, optimizers, losses, metrics
from keras.models import load_model

model = load_model('WindDenseNN.h5') 

if (sys.argv[-2] == "-i"):  #parsing file via command line
        filename = sys.argv[-1] 
else:
        print('Wrong Input') 
        sys.exit()

# It doesn't matter about this warning message: UserWarning: No training configuration found in save file: the model was *not* compiled. Compile it manually.
model.summary()  #test
# It doesn't matter about this warning message: UserWarning: No training configuration found in save file: the model was *not* compiled. Compile it manually.


weights = model.layers[0].get_weights()   
#print(type(weights), len(weights), len(weights[0]), len(weights[1]))

#print(weights)

model = keras.Sequential()   # create neural network
model.add(layers.Dense(64, activation='relu', input_shape=(128,))) 
model.compile(optimizer=optimizers.RMSprop(0.01), loss=losses.categorical_crossentropy, metrics=[metrics.categorical_accuracy])  
model.layers[0].set_weights(weights)  
model.summary()  #test

l1 = [str(x) for x in range(1,130)] 
df = pd.read_csv(filename,names=l1) 
#print(df.head()) #test

labels = list(df['1'])  

df = df.drop(df.columns[[0]], axis=1) # drop dates

print(df.head())

result = model.predict(df, batch_size=32)


l = []
for x in labels:
	l.append(x[1:19]) # keep only the timestamp.
#print(l[0], l[1], l[2])

t = pd.DataFrame(result)

t.insert(loc=0, column='Timestamp', value=l)


t.to_csv('new_representation.csv', header=False, index=False)

