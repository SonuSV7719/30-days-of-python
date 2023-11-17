# -> IV .Logical operators
# --->	and, or, not

# To check Multiple Conditions at same time

# ---> Ouput Of Logical Operators is 
# True or False

# Used in if else and loops

# and Table --> If all conditions are True
# then only True Otherwise False

# A         B         Ouput
# ---------------------------
# T         T           T
# T         F           F 
# F         T           F
# F         F           F

# E.g.
print(2 < 4 and 5 <= 5) # output --> True
print(2 < 4 and 5 <= 5 and 7 > 11) # output --> False


# or Table --> If all conditions are False
# then only False Otherwise True

# A         B         Ouput
#----------------------------
# T         T           T
# T         F           T 
# F         T           T
# F         F           F

print(2 < 4 or 5 <= 5) # output --> True
print(2 < 4 or 5 <= 5 or 7 > 11) # output --> True

# not --> Toggle 

# A       Ouput
#----------------
# T         F
# F         T

print(not(2 > 1)) # (2 > 1)--> True --> not --> False