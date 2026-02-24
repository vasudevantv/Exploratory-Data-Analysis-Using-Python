# Imports the pandas module, used for data manipulation and analysis
import pandas
# Load Titanic dataset
titanic = pandas.read_csv('titanic.csv')
# Display the first few rows of the original dataset
print("First few rows of the original data set")
print("---------------------------------------")
print(titanic.head())
# Create the FamilySize feature
titanic['FamilySize'] = titanic['SibSp'] + titanic['Parch'] + 1 # +1 for the individual themselves
# Create the IsAlone feature
titanic['IsAlone'] = (titanic['FamilySize'] == 1).astype(int) # 1 if alone, 0 otherwise
# Display the first few rows of the updated dataset with the new features
print("First few rows of the updated data set with the new features")
print("------------------------------------------------------------")
print(titanic[['SibSp', 'Parch', 'FamilySize', 'IsAlone']].head())
