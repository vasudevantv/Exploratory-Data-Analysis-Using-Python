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
print("Titanic data before imputing Cabin")
print("----------------------------------")
print(titanic_data)
print("-------------------------------------")


# Fill missing values in 'Cabin' with the placeholder 'Unknown'
titanic_data['Cabin'].fillna('Unknown', inplace=True)

# Display the results
print("Titanic data after imputing Cabin")
print("---------------------------------")
print(titanic_data)
print("-------------------------------------")

