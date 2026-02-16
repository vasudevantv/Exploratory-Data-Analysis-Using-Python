# import pandas module used for data manipulation and analysis
import pandas
# imports pyplot, a module used in the package matplotlib to plot various figures
from matplotlib import pyplot
# load the Titanic dataset
titanic_data = pandas.read_csv('titanic.csv')
# plots the histogram of fare attribute
# edge colour is set as black
# number of bins is set as 30 ( By default bins = 10 )
titanic_data['Fare'].plot(kind='hist', edgecolor="black", bins=30)
# sets the title 
pyplot.title("Histogram - Titanic Data Set")
# sets the x-axis label
pyplot.xlabel('Fare')
# shows the histogram
pyplot.show()
