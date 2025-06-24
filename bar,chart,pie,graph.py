
import matplotlib.pyplot as plt
#linechart
a = [1,4,5,7,8]
b = [3,7,4,2,9]

plt.plot(a,b,marker='+',)
plt.grid()
#scatter
plt.scatter(a,b,marker ='+')
plt.grid()

#bar
plt.bar(a,b,color='pink',width = 0.99)
plt.grid()
g=[4,3,2,7,8,2,2,2,2,4,3,7,7,7,7,5,8]
#pie
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]
colors = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen']
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=10)
plt.title('Pie Chart Example')
plt.show()
