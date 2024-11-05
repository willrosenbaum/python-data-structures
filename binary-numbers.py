import random

n_values = 16

# generate a list of n_values non-repeating values between 0 and 31
values = random.sample(range(32), n_values)

# convert each value to binary and pad with zeros to make them 5 bits long
binary_values = [format(value, '05b') for value in values]

# generate a string representation of values separated by commas surrounded by curly braces 
values_str = '{{' + ','.join(str(x) for x in values) + '}}'

# generate a string representation of binary_values separated by commas surrounded by curly braces
binary_values_str = '{{' + ',\n'.join('{{' + ','.join(str(x)) + '}}' for x in binary_values) + '}}'

print(values_str)
print(binary_values_str)
