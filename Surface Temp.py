import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('Temp.xlsx')

years = ['1960s','1970s','1980s','1990s','2000s','2010s','2020-2022']
mylist = []

def hesapla(a):
  b = 11
  c = 21
  mylist.append(np.mean(data.iloc[a][2:11]))
  for d in range(0,5):
    b += 10
    c += 10
    mylist.append(np.mean(data.iloc[a][b:c]))
  mylist.append(np.mean(data.iloc[a][61:64]))

plt.style.use("classic")
plt.figure(figsize=(9, 5))
plt.title("Surface Temperatures of The Biggest 3 Country in South America ")
plt.xlabel('Decades')
plt.ylabel('Degree')
plt.xticks(rotation=45)
plt.grid(True, color='black')

hesapla(8)
plt.plot(years, mylist, label="Argentina", marker='o', c = 'blue', linewidth = 7)
arg = mylist
mylist = []
hesapla(20)
plt.plot(years, mylist, label="Brazil", marker='o', c = 'green', linewidth = 7)
brazil = mylist
mylist = []
hesapla(129)
plt.plot(years, mylist, label="Peru", marker='o', c = 'red', linewidth = 7)
peru = mylist
plt.legend(loc = 'upper left')
plt.show()

plt.style.use("classic")
plt.figure(figsize=(9, 5))
plt.title("Surface Temperatures of The Biggest 3 Country in North America ")
plt.xlabel('Decades')
plt.ylabel('Degree')
plt.xticks(rotation=45)
plt.grid(True, color='black')

mylist = []
hesapla(28)
canada = mylist
plt.plot(years, mylist, label="Canada", marker='o', c = 'blue', linewidth = 7)
mylist = []
hesapla(169)
usa = mylist
plt.plot(years, mylist, label="USA", marker='o', c = 'red', linewidth = 7)
mylist = []
hesapla(107)
mexico = mylist
plt.plot(years, mylist, label="Mexico", marker='o', c = 'green', linewidth = 7)
plt.legend(loc = 'upper left')
plt.show()

mylist = []
dizi = np.array([[canada], [usa], [mexico]])
x = -1
for eachx in years:
  x += 1
  sutun_1 = dizi[:,:,x]
  ortalama_1 = np.mean(sutun_1)
  mylist.append(ortalama_1)

plt.style.use("classic")
plt.figure(figsize=(9, 5))
plt.title("Average of Surface Temperatures of North America's 3 Largest Countries ")
plt.xlabel('Decades')
plt.ylabel('Degree')
plt.xticks(rotation=45)
plt.grid(True, color='black')
plt.margins(x=0.01)
plt.stem(years, mylist)
plt.show()

mylist = []
dizi = np.array([[arg], [brazil], [peru]])
x = -1
for eachx in years:
  x += 1
  sutun_2 = dizi[:,:,x]
  ortalama_2 = np.mean(sutun_2)
  mylist.append(ortalama_2)

plt.style.use("classic")
plt.figure(figsize=(9, 5))
plt.title("Average of Surface Temperatures of South America's 3 Largest Countries ")
plt.xlabel('Decades')
plt.ylabel('Degree')
plt.xticks(rotation=45)
plt.grid(True, color='black')
plt.margins(x=0.01)
plt.stem(years, mylist)
plt.show()
