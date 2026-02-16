# imports pyplot, a module used in the package matplotlib to plot various figures
from matplotlib import pyplot
# Data: numbers from 1 to 10 stored in a list x
x = list(range(1, 11))
# Calculate their squares stored in a list y
y = [i ** 2 for i in x]  
# plots the line chart, adding circular markers at each data point
pyplot.plot(x, y,marker='o')
# Adding title and labels
pyplot.title('Line Chart')
pyplot.xlabel('Number')
pyplot.ylabel('Square of Number')
# Set x-ticks to the numbers
pyplot.xticks(x)  
# Show the plot
pyplot.show()
