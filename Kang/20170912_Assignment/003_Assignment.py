from numpy import genfromtxt
import numpy as np
import matplotlib.pyplot as plt

month = list()
#income = list()
#expense = list()
engel = list()

def drawGraph(month, engel):
    plt.plot(month, engel)
    plt.xlabel('Years')
    plt.ylabel('Engel_coefficient')
    plt.show()

print('''Assingment#003_MinkyuKang
-Description-
Calculate Engel's coefficient''')


fileName = input("Please enter a file name : ")
data_ = genfromtxt(fileName, delimiter=',')

result = [['Month', 'Income', 'Expense', 'Engel']]
for i in range(1, len(data_)) :
    result.append([data_[i][0],data_[i][1],data_[i][2],data_[i][2]/data_[i][1]])
    month.append(data_[i][0])
    engel.append(data_[i][2]/data_[i][1])

drawGraph(month, engel)