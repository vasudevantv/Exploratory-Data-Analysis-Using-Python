# Imports the pandas module, used for data manipulation and analysis
import pandas

# Store the url of the titanic data set
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
# Load Titanic dataset into a data frame
titanic_data = pandas.read_csv(url)

# len(titanic_data) returns the number of rows in the data frame
# Get the number of rows before dropping
rows_before = len(titanic_data)

# Drop rows where 'Age' is missing
titanic_data_cleaned = titanic_data.dropna(subset=['Age'])

# Get the number of rows after dropping
rows_after = len(titanic_data_cleaned)

# Set options to display the full DataFrame, otherwise display will be truncated
# pandas.set_option('display.max_rows', None)      # Show all rows
# pandas.set_option('display.max_columns', None)   # Show all columns

# Display the results
print("Titanic data before dropping")
print("----------------------------")
print(titanic_data)
print("-------------------------------------")
print("Number of rows before dropping = ", rows_before)
print("-------------------------------------")
print("Titanic data after dropping")
print("----------------------------")
print(titanic_data_cleaned)
print("-------------------------------------")
print("Number of rows after dropping = ", rows_after)
print("-------------------------------------")
