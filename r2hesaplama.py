import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import r2_score

veriler=pd.read_csv('maaslar.csv')

#verilerin bölünmesi
x=veriler.iloc[:,1:2]
y=veriler.iloc[:,2:]

#dataframeleri numpy arraylere dönüştürme
X = x.values
Y = y.values

#linear regression
from sklearn.linear_model import LinearRegression
lin_reg=LinearRegression()
lin_reg.fit(x,y)

plt.scatter(x,y)
plt.plot(x,lin_reg.predict(x))

#polynomial regression(2.dereceden)
from sklearn.preprocessing import PolynomialFeatures
poly_reg=PolynomialFeatures(degree=2)
x_poly=poly_reg.fit_transform(x)
print(x_poly)

lin_reg2=LinearRegression()
lin_reg2.fit(x_poly,y)
plt.scatter(x,y,color='red')
plt.plot(x,lin_reg2.predict(poly_reg.fit_transform(x)),color='blue')
plt.show()

#polynomial regression(4.dereceden)
poly_reg=PolynomialFeatures(degree=4)
x_poly=poly_reg.fit_transform(x)
print(x_poly)

lin_reg2=LinearRegression()
lin_reg2.fit(x_poly,y)
plt.scatter(x,y,color='red')
plt.plot(x,lin_reg2.predict(poly_reg.fit_transform(x)),color='blue')
plt.show()

print('Polynomial Regression R2 değeri')
print(r2_score(Y,lin_reg2.predict(poly_reg.fit_transform(X))))


#random forest regression
#n_estimators -> karar ağacı sayısı
from sklearn.ensemble import RandomForestRegressor
rf_reg=RandomForestRegressor(n_estimators=10,random_state=0)
rf_reg.fit(X,Y.ravel())

print(rf_reg.predict([[6.6]]))

plt.scatter(X,Y,color='red')
plt.plot(X,rf_reg.predict(X),color='blue')


print('Random Forest R2 değeri')
print(r2_score(Y,rf_reg.predict(X)))




