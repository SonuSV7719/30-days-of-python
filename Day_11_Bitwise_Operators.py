# Bitwise operators
# --> &, |, ^, ~(not), <<, >>


# & (And)--> if values are 1 then 1 otherwise 0

# A         B         Ouput
# ---------------------------
# 1         1           1
# 1         0           0 
# 0         1           0
# 0         0           0

print( 1 & 2) # --> (01 & 10) --> Ouput --> 0

# | (OR)--> if all values are 0 then only 0
# otherwise 1

# A         B         Ouput
# ---------------------------
# 1         1           1
# 1         0           1 
# 0         1           1
# 0         0           0

print(1 | 2) # (01 | 10)->output--> 11(3)

# ^ (XOR) --> if all values are same then 
# output will be 0 otherwise 1

# A         B         Ouput
# ---------------------------
# 1         1           0
# 1         0           1 
# 0         1           1
# 0         0           0

print(2 ^ 2) # (10 ^ 10) --> (00)->output 0 

# ~(not)

# ~x == -x-1
print(~2) # -2-1->Ouput->(-3)
# <<(left shift)
print(5 << 2) # (101 << 2)->1010__10100(20)

# >> (right shift) 
print(5 >> 2) # (101 >> 2)-->001