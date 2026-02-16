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
print("Titanic data before imputing Age")
print("--------------------------------")
print(titanic_data)
print("-------------------------------------")

# Calculate the median age
median_age = titanic_data['Age'].median()

# Impute missing values with the median age
# inplace=True modifies the original data frame
# inplace=False creates a new data frame with changes applied
titanic_data['Age'].fillna(median_age, inplace=True)

# Display the results
print("Titanic data after imputing Age")
print("-------------------------------")
print(titanic_data)
print("-------------------------------------")


