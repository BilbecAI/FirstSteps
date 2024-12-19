import matplotlib.pyplot as plt
import pandas as pd
#1
df=pd.read_csv('przykladowe_dane.csv')
print(df)
p3=df.head(3)
print(p3)
info=df.info()
#2
print(df)
suma=df[('Sprzedaż')].sum()
print(suma)
srednia=df[('Zysk')].mean()
print(srednia)
#3
suma=df.groupby('Produkt')['Sprzedaż'].sum()
print(suma)
srednia=df.groupby('Produkt')['Koszt'].mean()
print(srednia)
#4
sort100=df[df['Zysk']>100]
print(sort100)
sortA=df[df['Produkt']=='A']
print(sortA)
#5
plt.figure("Wykres 1: Sprzedaż według Produktu")
df.groupby('Produkt')['Sprzedaż'].sum().plot(kind='bar', title='Sprzedaż według Produktu')
plt.show()
plt.figure("Wykres 2: Zysk w czasie")
wykreslin=df.plot(x='Data', y='Zysk', kind='line', title='Zysk w czasie')
plt.show()