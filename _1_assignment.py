# 1)Fibonacci series between 0 to 50

no1 = 0 
no2 = 1 

while no2<50:
               count = no1 + no2
               no1 = no2
               no2 = count
               print(no1)   #output is 1 1 2 3 5 8 13 21 34   

# 2) word from the user and reverse it

name = str(input("enter the word "))
word = name
reverse = " "
for i in word:
	reverse = i + reverse

print(reverse) #output = enter the word Tharun
                              #nurahT


# 3) Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 

num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even = 0
odd = 0
for i in num:
               if i % 2 == 0:
                              even+=1
               else:
                              odd+=1
print("No. of even numbers = ", even)
print("No. of odd numbers = ", odd) 
                                    #output = No. of even numbers =  4
                                              #No. of odd numbers =  5