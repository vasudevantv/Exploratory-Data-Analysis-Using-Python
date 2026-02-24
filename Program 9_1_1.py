# Imports the pandas module, used for data manipulation and analysis
import pandas

# imports pyplot, a module used in the package matplotlib to plot various figures
from matplotlib import pyplot

# Load Titanic dataset into a data frame
titanic_data = pandas.read_csv('titanic.csv')

# Plotting the distribution of passenger ages using a histogram
titanic_data['Age'].plot(kind='hist', color='skyblue', edgecolor="black", bins=30)
# sets the title 
pyplot.title('Distribution of Passenger Ages')
# sets the x-axis label
pyplot.xlabel('Age')
# sets the y-axis label
pyplot.ylabel('Number of Passengers')
# shows the histogram
pyplot.show()
