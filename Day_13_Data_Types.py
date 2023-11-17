#(Day 13) Data Types in Python

# Text Type: String
# Numeric Types: int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray
# None Type:	NoneType

# 1. Number (int, float)
num = 2 #int
print(type(num)) #int

num1 = 2.2
print(type(num1)) #float

com = 2 + 3j
print(type(com)) # complex

# 2. String

str1 = "Hello World!"
str2 = 'He2#)'
str3 = """Doc String"""
print(type(str1)) # string(str)
 
# 3. Sequence Types
# i. list
list1 = [1, "Str", [1,3,5]]
print(type(list1))

# ii. tuple
tup1 = (1, 2, "sonu", ("h", "e"), [1,2])

# iii. Range
range1 = range(2, 7)
print(type(range1))

# Mapping Data types (dictionary)

student = {
    "abc":22,
    'xyz':55
}
print(type(student)) # Dict


# Set

set1 = {1, 2, "s", (1, 3)}
print(type(set1)) # set

f = frozenset({1, 4, 4 })
print(type(f)) # fronzenset

# Binary types

b = b"22"
print(type(b))

b = bytearray(6)
print(type(b))

# None
print(None)
print(type(None)) # NoneType