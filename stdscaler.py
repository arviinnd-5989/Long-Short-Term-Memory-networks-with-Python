from pandas import Series
from sklearn.preprocessing import StandardScaler
from math import sqrt
data = [1.0,5.5,9.0,2.6,8.8,3.0,4.1,7.9,6.3]
series=Series(data)
print(series)
values=series.values
values=values.reshape((len(values),1))
scaler = StandardScaler()
scaler=scaler.fit(values)
print('Mean: %f, StandardDeviation: %f'%(scaler.mean_,sqrt(scaler.var_)))
standardized = scaler.transform(values)
print(standardized)
inversed=scaler.inverse_transform(standardized)
print(inversed)