# Day 17 -->List

# 1. Declaration
# Syntax: 
# list_variable_name = [value1, value2,.....]
# values --> can be of any type

# index->0   1     2      3      4      5            6 --> +ve
list1 = [1, 2.2, "abc", (1,2), [1,2], {1,2}, {1:"abc", 2:"xyz"}]
#index->-7  -6    -5     -4     -3     -2           -1 --> -ve

# 2. Indexing
# I. Positive Indexing
# Start from 0 --> left to right of list 
print(list1[2]) #output-> abc
print(list1[0]) #output-> 1
print(list1[6]) #output-> {1:"abc", 2:"xyz"}

# II. Negative Indexing
# Start from -1 --> right to left of list
print(list1[-5]) #output-> abc
print(list1[-7]) #output-> 1
print(list1[-1]) #output-> {1:"abc", 2:"xyz"}

# 3. List Slicing->Breaking list into small parts
# Syntax:
# list_name[start(included):end(excluded):jump]

print(list1[0:3]) #output->[1, 2.2, "abc"]
print(list1[:])# default start->0 and end -> len(list)
#output-> [1, 2.2, "abc", (1,2), [1,2], {1,2}, {1:"abc", 2:"xyz"}]
print(list1[::])# default jump -> 1
#output-> [1, 2.2, "abc", (1,2), [1,2], {1,2}, {1:"abc", 2:"xyz"}]
print(list1[:2]) #output-> [1, 2.2]
print(list1[::2]) #output->[1, "abc", [1,2], {1:"abc", 2:"xyz"}]

# Negative 
print(list1[-6:-4]) # [2.2, "abc"]
# reverse
print(list1[::-1]) 
# [{1: 'abc', 2: 'xyz'}, {1, 2}, [1, 2], (1, 2), 'abc', 2.2, 1]
# reverse slicing
print(list1[-5:-8: -1]) # ['abc', 2.2, 1]

# 4. Insert
list2 = [1,2]
# Method 1 -->.append()-> Insert At last of list
list2.append(2)

# Method 2
list2.insert(0, [1,2])
print(list2) 
#output-> [[1, 2], 1, 2, 2]

# 5. Update
list3 = [1,2]
list3[0] = {1,23,4}
print(list3) #output-> [{1, 4, 23}, 2]

# 6. Delete
# Method 1
list4 = [1,2,3]
del list4[1]
print(list4) #output->[1, 3]

# Method 2
list5 = [1,2,3]
list5.remove(1)
print(list4) #output->[1, 3]

#Method 3
list5.clear()
print(list5) #output-> []

# Method 4
list6 = [1,2,3]
popped_item = list6.pop(0)
print(popped_item) #output-> 1
print(list6) #output-> [2, 3]
popped_item = list6.pop() #delete last item
print(list6)#output-> [2]

# 7. Functions
list7 = [1,2,3,3, 4, 2, 2, 2]
list7.count(2)

