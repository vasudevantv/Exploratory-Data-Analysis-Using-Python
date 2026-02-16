# Imports the pandas module, used for data manipulation and analysis
import pandas

# Load Titanic dataset into a data frame
titanic_data = pandas.read_csv('titanic.csv')

# titanic_data.shape returns the number of rows and columns in the data frame
number_of_rows, number_of_columns = titanic_data.shape

# Print number of rows and columns 
print("Titanic data set")
print("----------------")
print("Number of rows:",number_of_rows)
print("Number of columns:", number_of_columns)

# Print column data types
print("Column data types")
print("-----------------")
print(titanic_data.dtypes)

# Calculate and print the number of missing values in each column
# titanic_data.isnull()creates a DataFrame of the same shape as titanic_data, but with True for missing values and False for non-missing values
# .sum() counts the number of True values (i.e., missing values) for each column
missing_values = titanic_data.isnull().sum()
print("Number of missing values")
print("------------------------")
print(missing_values)

# Print basic descriptive statistics
print("Basic Descriptive Statistics")
print("----------------------------")
descriptive_stats = titanic_data.describe()
print(descriptive_stats)


