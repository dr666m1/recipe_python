from keras.models import Sequential
from keras.layers import Dense, Activation
model=Sequential()
model.add(Dense(output_dim=32, input_dim=784))
