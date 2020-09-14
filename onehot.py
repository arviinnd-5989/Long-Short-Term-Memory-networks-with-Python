from numpy import array
from numpy import argmax
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

data = ['cold','cold','warm','cold','hot','hot','warm','cold','warm','hot']
values = array(data)
print(values)
label_encoder = LabelEncoder()
integer_encoded = label_encoder.fit_transform(values)
print(integer_encoded)
onehot_encoder = OneHotEncoder(sparse=False)
integer_encoded = integer_encoded.reshape((len(integer_encoded),1))
onehot_encoded = onehot_encoder.fit_transform(integer_encoded)
print(onehot_encoded)
inverted = label_encoder.inverse_transform([argmax(onehot_encoded[0,:])])
print(inverted)