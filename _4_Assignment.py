###1)Python program to create a lambda function that adds 25 to a given number passed in as an argument.
input = lambda a: a+25
print("output = ",input(10))

# output:- output =  35

###2)Python program to triple all numbers of a given list of integers. Use Python map.

lst = [1, 2, 3, 4, 5, 6, 7]
data = list(map(lambda data: data*3,lst))
print(data)

# output:- [3, 6, 9, 12, 15, 18, 21]

###3)Python program to square the elements of a list using map() function.

lst = [4, 5, 2, 9]
data = list(map(lambda data: data**2,lst))
print(data)

# output:- [16, 25, 4, 81]