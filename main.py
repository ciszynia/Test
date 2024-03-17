# A.
print("Task A")
# 1. Create a variable name first with value 7.
# 2. Create a variable name second with value 44.3.
# 3. Print the result of adding first to second.
# 4. Print the result of multiplying first by second.
# 5. Print the result of dividing second by first.
first = 7
second = 44.3
print(first + second)
print(first * second)
print(second / first)
# B.
# What will be the values of a, b, c at the end?
print("Task B")
print("a will be 9")
print("b will be 8")
print("c will be 15")
print("Let's check:")
a = 8
a = 17
a = 9
b = 6
c = a + b
b = c + a
b = 8
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
# C.
print("Task C")
# Is there a difference between the two lines below? Why?
name1 = "john"
name2 = 'john'
print(f"1) The difference is only in using \' or \" symbols. In fact both values are equal: {name1 == name2}")
# What is the issue with the code below?
my_number = 5 + 5
# print("result is: " + my_number)
print(f"2) The issue appeared because we are trying to add str to int. + operator in Python can not convert\n"
      f"int to str implicitly. To perform this we should convert int explisitly using str() function. Let's try: ")
print("result is: " + str(my_number))
# D.
print("Task D")
# What will be the output?
# x = 5
# y = 2.36
# print (x + int(y))
print("int(y) will convert float value 2.36 to int value 2 => x + int(y) = 7. Let's check:")
x = 5
y = 2.36
print(f"answer: {x + int(y)}")
# E.
print("Task E")
# 1. Create two variables named X and Y.
# 2. Print “BIG” if X is bigger than Y.
# 3. Print “small” if X is smaller than Y.
x = 3
y = 3.8
if x > y:
    print("BIG")
else:
    print("small")
# F.
print("Task F")
# 1. Create a variable and initialize it with a number 1-4.
# 2. Create 4 conditions (if-elif) which will check the variable.
# 3. Print the season name accordingly:
# - 1 = summer
# - 2 = winter
# - 3 = fall
# - 4 = spring
season = 3
if season == 1:
    print("summer")
elif season == 2:
    print("winter")
elif season == 3:
    print("fall")
elif season == 4:
    print("spring")
# CHALLENGE:
print("Task CHALLENGE")
# Fix the following code without changing a or b:
# a = 8
# b = "123"
# print(a+b)
print("fixed:")
a = 8
b = "123"
print(str(a)+b)
# Practice from class:
print("Task Practice from class")
# 1.
fiveInt = 5
fiveStr = "5"
# 2.
booleanResult1 = fiveInt > int(fiveStr)
booleanResult2 = str(fiveInt) > fiveStr
# 3.
sumResult1 = fiveInt + int(fiveStr)
sumResult2 = str(fiveInt) + fiveStr
# 4.
isLarger1 = 5 > 5.5
isLarger2 = 5.5 > 5
# 5.
trueIsFalse = True is False
# 6.
helloCompare1 = "hello" > "helloo"
helloCompare2 = "helloo" > "hello"
print(":)")
