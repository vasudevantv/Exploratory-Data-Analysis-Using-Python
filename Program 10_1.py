# Imports the pandas module, used for data manipulation and analysis
import pandas
# imports pyplot, a module used in the package matplotlib to plot various figures
from matplotlib import pyplot
# Load Titanic dataset into a data frame
titanic_data = pandas.read_csv('titanic.csv')
# Plotting the distribution of fares 
titanic_data.boxplot(column='Fare', by='Pclass')
# sets the title 
pyplot.title('Fare Distribution Across Passenger Classes')
# sets the x-axis label
pyplot.xlabel('Passenger Class')
# sets the y-axis label
pyplot.ylabel('Fare')
# sets x-axis ticks along with labels
pyplot.xticks([1, 2, 3],['1st Class', '2nd Class', '3rd Class'])
# shows the plot
pyplot.show()

