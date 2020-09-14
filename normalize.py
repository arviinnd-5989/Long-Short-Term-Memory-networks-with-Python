from pandas import Series
from sklearn.preprocessing import MinMaxScaler

data = [10.0,20.0,30.0,40.0,50.0,60.0,70.0,80.0,90.0,100.0]
series = Series(data)
print(series)
values = series.values
values = values.reshape((len(values),1))
print(values)
scaler = MinMaxScaler(feature_range=(0,1))
scaler=scaler.fit(values)
print('Min: %f, Max: %f'%(scaler.data_min_,scaler.data_max_))
normalized=scaler.transform(values)
print(normalized)
inversed = scaler.inverse_transform(normalized)
print(inversed)