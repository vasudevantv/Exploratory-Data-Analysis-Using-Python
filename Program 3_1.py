# Imports the pandas module, used for data manipulation and analysis
import pandas

# Store the url of the titanic data set
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
# Load Titanic dataset into a data frame
titanic_data = pandas.read_csv(url)

# Calculate missing values and percentage
missing_data = titanic_data.isnull().sum()
# len(titanic_data) returns the number of rows in the data frame
missing_percentage = (missing_data / len(titanic_data)) * 100


# Create a DataFrame to hold the missing data info
missing_info = pandas.DataFrame({'Missing Values': missing_data, 'Percentage': missing_percentage})

# Filter columns with missing values
missing_info = missing_info[missing_info['Missing Values'] > 0]

# Display the results
print(missing_info)
