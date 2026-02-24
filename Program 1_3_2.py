# import pandas module used for data manipulation and analysis
import pandas
# imports pyplot, a module used in the package matplotlib to plot various figures
from matplotlib import pyplot
# Load the Titanic dataset
titanic_data = pandas.read_csv('titanic.csv')
# Count the number of passengers by Pclass sorted by Pclass order
pclass_counts = titanic_data['Pclass'].value_counts().reindex([1,2,3])
# plots the bar chart with different colours for each Pclass
pclass_counts.plot(kind='bar', color=['lightblue', 'lightgreen', 'salmon'])
# sets the title 
pyplot.title('Bar Chart - Titanic Data Set')
# sets the x-axis label
pyplot.xlabel('Passenger Class')
# sets the y-axis label
pyplot.ylabel('Number of Passengers')
# displays x-axis tick labels horizontally ( default behaviour is vertical )
pyplot.xticks(rotation='horizontal')  
# shows the bar chart
pyplot.show()
