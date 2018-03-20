import matplotlib.pyplot as plt

x=[]
y=[]

dataset = open('C:\\Users\Windows7\\Desktop\\dataset.csv', 'r')
for line in dataset:
    line = line.strip()
    X, Y = line.split(",")
    x.append(X)
    y.append(int(X)**2)

dataset.close()

plt.plot(x, y)

'''
plt.title("Exemplo")
plt.xlabel("X Label")
plt.ylabel("Y Label")
'''
plt.show()