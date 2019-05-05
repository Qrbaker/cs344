"""

Lab 6, Exercise 3

Author: Quentin Baker
Created: April 20, 2019
Based on examples from https://keras.io/datasets/#boston-housing-price-regression-dataset

"""

from keras.datasets import boston_housing

# Assuming this is similar to the other datasets, the _x_ value is the data and the _y_ is labels.
(x_train, y_train), (x_test, y_test) = boston_housing.load_data()

# a1
print("Number of test examples:\t\t%s" % len(x_train))
print("Number of training examples:\t%s\n" % len(x_test))


# a2
def print_data(data_set):
    print("Rank\t\t%s" % data_set.ndim)
    print("Shape:\t\t%s" % str(data_set.shape))
    print("Data Type:\t%s" % data_set.dtype)


print('=== Training Data ===')
print_data(x_train)

print('\n === Testing Data ===')
print_data(x_test)
