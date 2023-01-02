# Q1) Write a program to find all pairs of an integer array whose sum is equal to a given number

def Pair_of_integer (nums, sum):
     
    for i in range(len(nums) - 1):
 
        for j in range(i + 1, len(nums)):

                if nums[i] + nums[j] == sum:
                    print('Pair of integer is : ', (nums[i], nums[j]))
                    return
    print('pair of integers not found')
 
if __name__ == '__main__':
 
    nums = [5,7,3,9,8,1,2,4]
    sum = 10
Pair_of_integer (nums, sum)

# output:- Pair of integer is :  (7, 3)

"""======================================================================================================="""
# Q2) Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.

def reverse_array (nums):

    reverse = nums[::-1]
    print(reverse)

if __name__ == '__main__':
 
    nums = [5,7,3,9,8,1,2,4]
    
reverse_array (nums)

# Output:- 
# [4, 2, 1, 8, 9, 3, 7, 5]

"""======================================================================================================="""
# Q3) Write a program to check if two strings are a rotation of each other?

str1 = "EDYODA"
str2 = "YDEADO"

def string_Rotation(str1, str2):

    if len(str1) != len(str2):
        out = " "
        return False
  
    out = str1 + str1 
  
    if str1 in out: 
        print("\U0001F603 Strings are rotations of each other \U0001F603")
    else:
        print("\U0001F629 Strings are not rotations of each other \U0001F629")
  
string_Rotation(str1, str2)

# Output:- 
# 😃 Strings are rotations of each other 😃

"""======================================================================================================="""

# Q4) Write a program to print the first non-repeated character from a string?

str1 = "EEDYOODA"
order = []
counts = {}

for i in str1:
    if i in counts:
        counts[i] += 1
    else:
        counts[i] = 1
        order.append(i)
for j in order:
    if counts[j] == 1:
        break
print("first non-repeated character : ",j)

# Output:- first non-repeated character :  Y
"""======================================================================================================="""

# Q5) Read about the Tower of Hanoi algorithm. Write a program to implement it.

def Hanoi(disks, source, aux, output):
    if disks == 1:
        print('Move disk 1 from rod {} to rod {}.'.format(source, output))
        return
 
    Hanoi(disks - 1, source, output, aux)
    print('Move disk {} from rod {} to rod {}.'.format(disks, source, output))
    Hanoi(disks - 1, aux, source, output)
 
disks = int(input('Enter number of disks: '))
Hanoi(disks, 'A', 'B', 'C')

# output:- 
# Enter number of disks: 3
# Move disk 1 from rod A to rod C.
# Move disk 2 from rod A to rod B.
# Move disk 1 from rod C to rod B.
# Move disk 3 from rod A to rod C.
# Move disk 1 from rod B to rod A.
# Move disk 2 from rod B to rod C.
# Move disk 1 from rod A to rod C.
"""======================================================================================================="""

# Q6. Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.

class StackNode :
	def __init__(self, data, top) :
		self.data = data
		self.next = top
	
class MyStack :
	def __init__(self) :
		self.top = None
		self.count = 0
	
	def size(self) :
		return self.count
	
	def isEmpty(self) :
		if (self.size() > 0) :
			return False
		else :
			return True
		
	def push(self, data) :
		
		self.top = StackNode(data, self.top)
		self.count += 1
	
	def pop(self) :
		temp = ""
		if (self.isEmpty() == False) :
			temp = self.top.data
			self.top = self.top.next
			self.count -= 1
		return temp
	
	def peek(self) :
		if (not self.isEmpty()) :
			return self.top.data
		else :
			return ""
		
class Conversion :
	def isOperator(self, text) :
		if (text == '+'
			or text == '-'
			or text == '*'
			or text == '/'
			or text == '^'
			or text == '%') :
			return True
		
		return False

	def isOperands(self, text) :
		if ((text >= '0'
				and text <= '9') or(text >= 'a'
				and text <= 'z') or(text >= 'A'
				and text <= 'Z')) :
			return True
		
		return False
	
	def postfixToPrefix(self, postfix) :

		size = len(postfix)
		
		s = MyStack()

		auxiliary = ""
		isValid = True
		i = 0
		while (i < size and isValid) :
			
			if (self.isOperator(postfix[i])) :
				
				if (s.size() > 1) :
					auxiliary = s.pop()
					auxiliary = s.pop() + auxiliary
					auxiliary = postfix[i] + auxiliary
					s.push(auxiliary)
				else :
					isValid = False
				
			elif (self.isOperands(postfix[i])) :
				auxiliary = postfix[i]
				s.push(auxiliary)
			else :
				isValid = False
			
			i += 1
		
		if (isValid == False) :
			print("Invalid postfix : ", postfix)
		else :
			print(" Postfix : ", postfix)
			print(" Prefix  : ", s.pop())
		
def main() :
	task = Conversion()
	postfix = "ab+c*ef+g/+"
	task.postfixToPrefix(postfix)
	postfix = "abc*de-/+"
	task.postfixToPrefix(postfix)

if __name__ == "__main__": main()

# Output:- 
#  Postfix :  ab+c*ef+g/+
#  Prefix  :  +*+abc/+efg
#  Postfix :  abc*de-/+
#  Prefix  :  +a/*bc-de
"""========================================================================================================"""
# Q7. Write a program to convert prefix expression to infix expression.

operators = {'+': True, '-': True, '*': True, '/': True, '^': True}
precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

def prefix_to_infix(expression):
  stack = []
  
  for character in expression[::-1]:
    if character not in operators:
      stack.append(character)
    else:
      operand_1 = stack.pop()
      operand_2 = stack.pop()

      infix_expression = '(' + operand_1 + character + operand_2 + ')'
      stack.append(infix_expression)

  return stack[0]

print(prefix_to_infix('*+AB-CD'))

# Output:- ((A+B)*(C-D))
"""========================================================================================================"""
# Q8. Write a program to check if all the brackets are closed in a given code snippet.

def isMatch(X, x):
    if X == '(' and x == ')':
        return True
    if x == '[' and x == ']':
        return True
    if X == '{' and x == '}':
        return True
    return False

def isBalanced(sub):
    top = -1
    for i in range(len(sub)):
        if top < 0 or not isMatch(sub[top], sub[i]):
            top += 1
            sub[top] = sub[i]
        else:
            top -= 1
    return True if top == -1 else False


def main():
    sub = input("Enter Brackets : ")

    if isBalanced(list(sub)):
        print("\nIs Balanced\n")
    else:
        print("\nIs Not Balanced, Enter correctly\n")

main()

# Output:- 
# Enter Brackets : ()
# Is Balanced
"""========================================================================================================"""
# Q9. Write a program to reverse a stack.

class Reverse_Stack():
    def __init__(self):
        self.data = []
        self.reve = []

    def push(self, element):
        self.data.append(element)

    def rev(self):
        self.reverse = self.data[::-1]
        self.reve.append(self.reverse)

    def display(self):
        print("Correct stack : ", self.data)
        print("Reverse Stack : ", self.reve)

obj = Reverse_Stack()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
obj.rev()
obj.display()

# Output:-
# Correct stack :  [1, 2, 3, 4]
# Reverse Stack :  [[4, 3, 2, 1]]
"""========================================================================================================"""

# Q10. Write a program to find the smallest number using a stack.

class Reverse_Stack():
    def __init__(self):
        self.data = []
        self.smallest_num = []

    def push(self, element):
        self.data.append(element)

    def small(self):
            smal = min(self.data)
            self.smallest_num.append(smal)

    def display(self):
        print("Input stack : ", self.data)
        print("Smallest number in Stack : ", self.smallest_num)

obj = Reverse_Stack()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
obj.small()
obj.display()

# Output:- 
# Input stack :  [1, 2, 3, 4]
# Smallest number in Stack :  [1]
"""========================================================================================================"""
