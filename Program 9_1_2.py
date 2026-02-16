# Imports the pandas module, used for data manipulation and analysis
import pandas

# Load Titanic dataset into a data frame
titanic_data = pandas.read_csv('titanic.csv')

# Calculating the most common passenger class
# mode()[0] get the first mode value, as mode() can return multiple values
most_common_class = titanic_data['Pclass'].mode()[0]

print("Most common passenger class:", most_common_class)
