# Imports the pandas module, used for data manipulation and analysis
import pandas
# Load Titanic dataset into a data frame
titanic_data = pandas.read_csv('titanic.csv')
# Count the number of passengers in each class ordered by Pclass
class_passenger_count = titanic_data['Pclass'].value_counts().reindex([1,2,3])
# Calculate the average age
average_age = titanic_data['Age'].mean()
# Calculate the number of survivors
number_of_survivors = titanic_data['Survived'].sum()
# Output the results
print("Number of passengers in each class")
print("----------------------------------")
print(class_passenger_count)
# Prints with precision 2 after decimal point
print("Average age of passengers:","%.2f" % average_age)
print("Number of survivors:", number_of_survivors)