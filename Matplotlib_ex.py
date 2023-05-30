import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

##Python program that draw a line with suitable label in the x axis, y axis and a title.
X = range(1, 50)
Y = [value * 3 for value in X]
print("Values of X:")
print(*range(1,50)) 
print("Values of Y (thrice of X):")
print(Y)
plt.plot(X,Y)
plt.title('Draw a line')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()

##Python program that draw a line using given axis values with suitable label in the x axis , y axis and a title.
X1 = [1,2,3]
Y1 = [2,4,1]
print("Values of X:")
print(X1) 
print("Values of Y:")
print(Y1)
plt.plot(X1,Y1)
plt.title('Sample graph!')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()

##Python program that draw a line using given axis values with suitable label in the x axis , y axis and a title.
with open("test.txt") as f:
    data = f.read()
data = data.split('\n')
x = [row.split(' ')[0] for row in data]
y = [row.split(' ')[1] for row in data]
int_x = list(map(int, x))
print(int_x)
int_y = list(map(int, y))
print(int_y)
plt.plot(int_x,int_y)
plt.title('Sample graph!')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()

##Python program that draw line charts of the financial data of Alphabet Inc. between October 3, 2016 to October 7, 2016
df = pd.read_csv('fdata.csv', sep=';')
print(df)
df.plot()
plt.show()

##Python program that plot two or more lines on same plot with suitable legends of each line.
x1=[10,20,30]
y1=[20,40,10]
plt.plot(x1,y1,color='blue', linewidth = 3,  label = 'line1',linestyle='dotted')
x2=[10,20,30]
y2=[40,10,30]
plt.plot(x2,y2,color='red', linewidth = 5,  label = 'line2',linestyle='dashed', marker='o', markerfacecolor='blue', markersize=12)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Two or more lines on same plot with suitable legends ')
plt.axis([8, 50, 8, 50]) 
plt.grid(linestyle='-', linewidth='0.5')
plt.legend()
plt.show()

##Python program that create multiple plots
fig = plt.figure()
fig.subplots_adjust(bottom=0.020, left=0.020, top = 0.900, right=0.800)

plt.subplot(2, 1, 1)
plt.xticks(()), plt.yticks(())

plt.subplot(2, 3, 4)
plt.xticks(())
plt.yticks(())

plt.subplot(2, 3, 5)
plt.xticks(())
plt.yticks(())

plt.subplot(2, 3, 6)
plt.xticks(())
plt.yticks(())

plt.show()

##Python programming that display a bar chart of the popularity of programming Languages.
x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
x_pos = [i for i, _ in enumerate(x)]
plt.bar(x_pos, popularity, color='blue')
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
plt.xticks(x_pos, x)
## Turn on the grid
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
## Customize the minor grid
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()

##Python programming that create a pie chart of the popularity of programming Languages
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
myexplode = [0.1, 0, 0, 0,0,0.05]
plt.pie(popularity, labels = languages, explode = myexplode, shadow = True, autopct='%1.1f%%', startangle=140)
plt.axis('equal')
plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago", bbox={'facecolor':'0.8', 'pad':5})
plt.show() 

##Python program that draw a scatter graph taking a random distribution in X and Y and plotted against each other.
from pylab import randn
X3 = randn(200)
Y3 = randn(200)
plt.scatter(X3,Y3, color='r',s=70, facecolors='none')
plt.xlabel("X")
plt.ylabel("Y")
plt.show()