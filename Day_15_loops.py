# Day 15 --> Loops 

# 1. for loop --> When we know where we want to end
# 2. while loop --> when we don't know end it's depend
# on user then use while loop 

# 1. Syntax of for loop
# for variable_name in range(start(included), end(excluded), jump):
#     your block of code 
#     any thing

# for variable_name in iterables[list, tuples, dic, string, range..etc]:
#     your block of code 
#     any thing
print("-----------------Simple loop-------------")
for i in range(1, 11):
    print(i)

#output-->   
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
print("-----------------Jump concept in loop-------------")
for even in range(1,11, 2):
    print(even)

#output
# 2
# 4
# 6
# 8
# 10 

print("-----------------Reverse loop-------------")
# reverse for loop
for i in range(10, 0, -1):
    print(i)

# output:
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1  

# 2. While loop

# start
# while condition:
#     Code 
#     increment start

num = 1
while num <= 10:
    print(num)
    num += 1
    
#output-->   
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10


