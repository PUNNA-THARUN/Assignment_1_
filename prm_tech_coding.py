# Problem Statement - 1 (Python)
# sort the list based on 2nd last character of a string

no_words = int(input("Enter the number of words: "))
lst = []

for i in range(no_words):
    words = input("Enter words here: ")
    lst.append(words)

output = sorted(lst, key=lambda x: x[-2])
print(output)

# output:-
# Enter the number of words: 4
# Enter words here: tharun
# Enter words here: edyoda
# Enter words here: great
# Enter words here: hello
# ['great', 'edyoda', 'hello', 'tharun']


# Problem Statement - 2 (Python)
# our task is to complete the validate_triangle and validate_rectangle functions for the classes.
# Taking inputs individually from user
class Check:

    def tri(self):
        side1 = int(input("Enter value of side1 :"))
        side2 = int(input("Enter value of side2 :"))
        side3 = int(input("Enter value of side3 :"))
        if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
            print("\n!Valid Triangle!\n")
        else:
            print("\n!Invalid Triangle!\n")
        
    def rec(self):
        a = int(input("Enter value of length :"))
        b = int(input("Enter value of breadth :"))
        c = int(input("Enter value of length :"))
        d = int(input("Enter value of breadth :"))
        if (a == c and b == d):
            print("\n!Valid Rectangle!\n")
        else:
            print("\n!Invalid Rectangle!\n")

obj = Check()
obj.tri()
obj.rec()

# Output:-
# Enter value of side1 :3
# Enter value of side2 :4
# Enter value of side3 :5

# !Valid Triangle!

# Enter value of length :1
# Enter value of breadth :2
# Enter value of length :1
# Enter value of breadth :2

# !Valid Rectangle!

# Enter value of side1 :1
# Enter value of side2 :12
# Enter value of side3 :11

# !Invalid Triangle!

# Enter value of length :1 
# Enter value of breadth :2
# Enter value of length :3
# Enter value of breadth :4

# !Invalid Rectangle!

"""*** OR ***"""
# Taking inputs once from user
class Check:
    
    def tri(self):
        side = int(input("Enter value of sides :"))
        lst = [int(val) for val in str(side)]
        if lst[0] + lst[1] > lst[2] and lst[1] + lst[2] > lst[0] and lst[0] + lst[2] > lst[1]:
            print("\n!Valid Triangle!\n")
        else:
            print("\n!Invalid Triangle!\n")
        
    def rec(self):
        side = int(input("Enter value of values :"))
        l = [int(val) for val in str(side)]
        if (l[0] == l[2] and l[1] == l[3]):
            print("\n!Valid Rectangle!\n")
        else:
            print("\n!Invalid Rectangle!\n")

obj = Check()
obj.tri()
obj.rec()

# Output:-
# Enter value of sides :345

# !Valid Triangle!

# Enter value of values :1212

# !Valid Rectangle!

# Enter value of sides :325

# !Invalid Triangle!

# Enter value of values :1234

# !Invalid Rectangle!