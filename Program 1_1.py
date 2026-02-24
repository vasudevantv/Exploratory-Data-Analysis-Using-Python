# Imports the numpy module, used for numeric computing
import numpy

# Create a NumPy array with values from 1 to 50
# Generates an array with values starting from 1 up to,but not including,51
array = numpy.arange(1, 51)

# Calculate the mean
mean_value = numpy.mean(array)

# Calculate the maximum
max_value = numpy.max(array)

# Calculate the minimum
min_value = numpy.min(array)

# Calculate the standard deviation
std_deviation = numpy.std(array)

# Output the results
print("Array:", array)
print("Mean:", mean_value)
print("Maximum:",max_value)
print("Minimum:",min_value)
print("Standard Deviation:","%.2f" % std_deviation)
