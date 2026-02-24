# Imports the pandas module, used for data manipulation and analysis
import pandas
# imports pyplot, a module used in the package matplotlib to plot various figures
from matplotlib import pyplot
# Load Titanic dataset into a data frame
titanic_data = pandas.read_csv('titanic.csv')
# Count the number of survivors and non-survivors by sex
# The groupby() function groups the data by "Sex" and "Survived"
# size() counts the occurrences
# The resulting counts are unstacked to create a Data Frame suitable for plotting
survival_sex = titanic_data.groupby(['Sex', 'Survived']).size().unstack()
# Plotting the bar chart as a stacked one
survival_sex.plot(kind='bar', stacked=True, color=['red', 'green'])
# sets the title 
pyplot.title('Survival Count by Gender')
# sets the x-axis label
pyplot.xlabel('Sex')
# sets the y-axis label
pyplot.ylabel('Number of Passengers')
# displays x-axis tick labels horizontally ( default behaviour is vertical )
pyplot.xticks(rotation='horizontal')
# sets the legend
pyplot.legend(['Did Not Survive', 'Survived'])
# shows the bar chart
pyplot.show()
