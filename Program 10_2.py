# imports the pandas module, used for data manipulation and analysis
import pandas
# imports the data visualisation library seaborn
import seaborn
# imports pyplot, a module used in the package matplotlib to plot various figures
from matplotlib import pyplot
# Load Titanic dataset into a data frame
titanic = pandas.read_csv('titanic.csv')
# Clean the data by dropping rows with missing age values
titanic = titanic.dropna(subset=['Age'])
# Create a violin plot
seaborn.violinplot(x='Survived', y='Age', data=titanic, palette={0: 'red', 1: 'green'}) 
# Set titles and labels
pyplot.title('Age Distribution by Survival Status on the Titanic - Violin Plot')
pyplot.xticks([0, 1], ['Not Survived', 'Survived'])
pyplot.xlabel('Survival Status')
pyplot.ylabel('Age')
# Show the plot
pyplot.show()


