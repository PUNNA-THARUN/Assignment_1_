 #1)       #ASCII values fron "a" to "z"
##a) below program is with inbuit alphabets

alp = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
ascii = {}
for i in alp:
    ky = i
    value = ord(i)
    ascii[ky]=value
print(ascii)   
#output :- {'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104, 
# 'i': 105, 'j': 106, 'k': 107, 'l': 108, 'm': 109, 'n': 110, 'o': 111, 'p': 112, 'q': 113, 
# 'r': 114, 's': 115, 't': 116, 'u': 117, 'v': 118, 'w': 119, 'x': 120, 'y': 121, 'z': 122}


##b) below program is alphabets taken from user

alp = str(input("enter alphabets "))
ascii = {}
for i in alp:
    ky = i
    value = ord(i)
    ascii[ky]=value
print(ascii)
#output :- enter alphabets abcdefghijklmnopqrstuvwxyz
# {'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104, 
# 'i': 105, 'j': 106, 'k': 107, 'l': 108, 'm': 109, 'n': 110, 'o': 111, 'p': 112, 'q': 113, 
# 'r': 114, 's': 115, 't': 116, 'u': 117, 'v': 118, 'w': 119, 'x': 120, 'y': 121, 'z': 122}


#2) sorted in increasing order by the last element in each tuple

lst = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
lent = len(lst)
for i in range(0,lent):
    for j in range(0,lent):
        if lst[i][1]<lst[j][1]:
            lst[i],lst[j]=lst[j],lst[i]
print(lst)
#output:-[(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]