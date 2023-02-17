import numpy as np

# ****************************** NumPy Coding Problems***********************************
## 1. Create a null vector of size 10 but the fifth value which is 1.

null_vector = np.zeros(10)
null_vector[4] = 1
print("Null indices is :",null_vector)

# Output:- 
# Null indices is : [0. 0. 0. 0. 1. 0. 0. 0. 0. 0.]

"""================================================================================================="""
## 2. Create a vector with values ranging from 10 to 49.

vector = np.arange(10,50)
print("Vector :", vector)

# Output:-
# Vector : [10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33
#  34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49]

"""================================================================================================="""
## 3. Create a 3x3 matrix with values ranging from 0 to 8

mat = np.random.randint(0,8,(3,3))
print("Matrix :", mat)

# Output:-
# Matrix : [[3 0 6]
#  [6 7 1]
#  [7 2 4]]

"""================================================================================================="""
## 4. Find indices of non-zero elements from [1,2,0,0,4,0]

arr = np.array([1,2,0,0,4,0])
a = np.nonzero(arr)
print(a)

# Output:-
# (array([0, 1, 4], dtype=int64),)

"""================================================================================================="""
## 5. Create a 10x10 array with random values and find the minimum and maximum values.

ary = np.random.rand(10,10)  # This will give random float values
max = np.max(ary)
min = np.min(ary)
print("Array :", ary)
print("Max Value :", max)
print("Min Value :", min)

# # output:- for float values
# Array : [[3.61442414e-02 2.76057822e-01 4.42076287e-01 2.17739520e-01
#   3.59956689e-01 4.86493082e-01 4.07397720e-01 4.77577056e-01
#   5.12940420e-01 2.39107700e-01]
#  [5.41873827e-01 1.29741488e-01 8.20610832e-01 9.36168751e-02
#   1.39892835e-01 8.32157761e-01 9.99797564e-01 9.80016530e-01
#   5.87441472e-01 2.20069325e-01]
#  [5.60879192e-01 3.01171297e-01 2.22999514e-01 2.51729453e-01
#   3.84710997e-01 3.59174831e-01 7.98835624e-01 7.23571095e-01
#   8.68915629e-01 2.78446786e-02]
#  [9.90611552e-01 5.26520047e-01 8.55562369e-01 6.99693197e-01
#   2.04846002e-02 9.05121819e-01 6.58571786e-01 1.62689416e-01
#   9.69495492e-01 4.17073314e-01]
#  [8.76054850e-01 1.67179957e-01 9.54755824e-02 9.91839865e-01
#   3.18282538e-01 1.07375593e-01 9.52586456e-01 6.93394658e-04
#   2.49408462e-01 7.63765277e-01]
#  [1.14295398e-01 6.10073911e-01 4.26690973e-01 2.22498307e-02
#   8.92790107e-01 3.94872079e-01 9.03506843e-02 7.54947767e-01
#   5.86057163e-01 2.82670030e-01]
#  [8.72132913e-01 8.22670787e-01 5.53682552e-01 1.92260457e-01
#   4.02006713e-01 7.17186520e-01 2.42898770e-01 7.52626996e-01
#   4.81435202e-01 7.25560144e-01]
#  [8.87124024e-02 1.48290333e-01 4.36633422e-01 2.86350112e-01
#   7.76533347e-01 3.86901259e-01 8.64392895e-01 3.26646811e-01
#   9.14745076e-02 3.36962778e-01]
#  [6.66558405e-01 2.38408621e-01 5.84610154e-01 2.61983224e-01
#   5.83106851e-01 5.06549970e-01 1.49336022e-01 3.11635721e-01
#   8.71563149e-01 2.27557468e-01]
#  [7.47455291e-02 6.77542606e-01 6.07889414e-01 3.47474762e-02
#   5.51855930e-01 8.77692955e-01 4.01129326e-01 6.30389857e-01
#   7.16306048e-01 9.04533300e-01]]
# Max Value : 0.9997975638932604
# Min Value : 0.0006933946577599714

"""================================================================================================="""
## 6. Create a random vector of size 30 and find the mean value.

ary = np.random.rand(30)
print("Array is :",ary)
men = ary.mean()
print("Mean of Array :",men)

# Output:- 
# Array is : [0.49606118 0.46147898 0.83271307 0.89246797 0.07723704 0.65525408
#  0.14251133 0.10735601 0.48507391 0.48635339 0.9795919  0.97954271
#  0.68082995 0.57998341 0.93267295 0.29155057 0.6383948  0.6921581
#  0.22397768 0.10370719 0.54189004 0.38041001 0.28522146 0.69968664
#  0.83132326 0.64212201 0.60419046 0.15161063 0.0731807  0.91988615]
# Mean of Array : 0.5289479201524785

"""================================================================================================="""
