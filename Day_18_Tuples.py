# Day 18
# Tuples 
# Imutable , ordered 

# 1. Creation of tuples 
# Syntax 

# tup_name = (item1, item2, item3, ....)

# Example
# index->0   1     2          3             4              5  --> + ve Indexing 
tup1 =  (1, 1.2, "Tuple", {1, 2, 4}, {"name" : "Hello"}, (1,2)) 
#index->-6  -5    -4         -3          -2               -1 --> -ve Indexing


# 2. Indexing
# I. Positive Indexing
# Start from 0 --> left to right of Tuple 
print(tup1[2]) #output-> Tuple
print(tup1[0]) #output-> 1
print(tup1[5]) #output-> (1, 2)
print(tup1[len(tup1) - 1])

# II. Negative Indexing
# Start from -1 --> right to left of Tuple
print(tup1[-5]) #output-> 1.2
print(tup1[-6]) #output-> 1
print(tup1[-1]) #output-> (1, 2)

# 3. Tuple Slicing->Breaking Tuple into small parts
# Syntax:
# tuple_name[start(included):end(excluded):jump]

print(tup1[0:3]) #output->(1, 1.2, "Tuple")
print(tup1[:])# default start->0 and end -> len(list)
#output-> (1, 1.2, "Tuple", {1, 2, 4}, {"name" : "Hello"}, (1,2))
print(tup1[::])# default jump -> 1
#output-> (1, 1.2, "Tuple", {1, 2, 4}, {"name" : "Hello"}, (1,2))
print(tup1[:2]) #output-> [1, 1.2]
print(tup1[::2]) #output->(1, "Tuple", {"name" : "Hello"})

# Negative 
print(tup1[-6:-4]) # (1, 1.2)
print(tup1[::-1]) 
# ((1, 2), {'name': 'Hello'}, {1, 2, 4}, 'Tuple', 1.2, 1)
# reverse slicing
print(tup1[-5:-7: -1]) # (1.2, 1)


# 4. we can't insert value, delete or change value

# change value Give error --> TypeError: 'tuple' object does not support item assignment
# tup1[0] = 2

# Delete give error --> TypeError: 'tuple' object doesn't support item deletion
# del tup1[0]



# 5. Iterating over tuple 

tup2 = (1, 2, 3, 4, 5)

# Method 1
for i in range(len(tup2)):
    print(tup2[i])

# Output
# 1
# 2
# 3
# 4
# 5

# Method 2
for i in tup2:
    print(i)
    
# Output
# 1
# 2
# 3
# 4
# 5