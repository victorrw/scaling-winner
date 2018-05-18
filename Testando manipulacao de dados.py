#import scipy as sp
import matplotlib.pyplot as plt
x = []
y = []
data = open('result.txt','r')
print(data)
plt.title('TÍTULO LINDO') #adicionando o título
plt.xlabel('Data/Hora',fontsize=12)
plt.ylabel('Preço',fontsize=14)
plt.xticks(rotation=30,fontsize=8)
plt.grid()
plt.autoscale(tight=True)
for line in data:
        X, Y = line.split(',')
        x.append(X)
        y.append(Y)
data.close()
plt.plot(x,y)
plt.show()
