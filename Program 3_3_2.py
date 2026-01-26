# Imports the pandas module, used for data manipulation and analysis
import pandas

# Store the url of the titanic data set
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
# Load Titanic dataset into a data frame
titanic_data = pandas.read_csv(url)

# Set options to display the full DataFrame, otherwise display will be truncated
# pandas.set_option('display.max_rows', None)      # Show all rows
# pandas.set_option('display.max_columns', None)   # Show all columns

# Display the results
print("Titanic data before imputing Embarked")
print("-------------------------------------")
print(titanic_data)
print("-------------------------------------")

# Calculate the mode for the 'Embarked' column
# Get the first mode value, as mode() can return multiple values

mode_embarked = titanic_data['Embarked'].mode()[0]  

# Impute missing embarked with the most frequent value
titanic_data['Embarked'].fillna(mode_embarked, inplace=True)

# Display the results
print("Titanic data after imputing Embarked")
print("------------------------------------")
print(titanic_data)
print("-------------------------------------")



