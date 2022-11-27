# 1)sum all the numbers in a list.

def sum_of_numbers(num):
    val = 0
    for x in num:
        val += x
    return val
print(sum((8, 2, 3, 0, 7)))   # out:- 20


# 2)Python program to reverse a string.

def reverse_string(object):
    object = object[::-1]
    return object
s = "1234abcd"
print("program to reverse a string: ", reverse_string(s))   

#output:- program to reverse a string:  dcba4321

# 3)the number of upper case letters and lower case letters.

sample_string = 'The quick Brow Fox'
def val(sample_string):
  upper = 0
  lower = 0
  for i in sample_string:
      if i>='A' and i<='Z':
            upper += 1
      if i >='a' and i<='z':
            lower += 1
  print("No. of Upper letters: ",upper)
  print("No. of Lower letters: ",lower)
val(sample_string)

# output: No. of Upper letters:  3
        # No. of Lower letters:  12
