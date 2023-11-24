# Day 16 --> Strings

#1. Declaration and initialization
str1 = 'Abc is good boy.'
str2 = "Abc is good boy"
str3 = """Good!!"""

# Indexing --> To access specific Character of string
# --> "ABC" --> A --> First character --> Indexing

# --> Two types of Indexing 
# --> 1. Positive Indexing
# --> 2. Negative Indexing

# positive indexing start with -> 0 -> From front of string
print(str3[2]) # output --> o
print(str2[0]) # output -> A

# Negative Indexing Start with -> -1 -> Back of string
print(str3[-1]) # output-> !
print(str3[-4]) # output -> o

#2. String Slicing 
# Syntax 
# String_variable_name[start_idx:end_idx:jump] -> end(excluded)
str3 = "GOod!!" # -->len(str3) ->6
print(str3[:]) # --> output->GOod!!
# (start default ->0, end default ->len(str))

print(str3[:2]) # --> output->GO
print(str3[1:3]) # -> output->Oo
print(str3[::]) #output -> GOod!!(jump default ->1)
print(str3[::2]) #output-> Go!
print(str3[::-1]) # output -> reverse -> !!doOG
print(str3[-4:-1]) #output-> od!
print(str3[1::-1]) # output -> OG
print(str3[2:0:-1]) #output -> oO

#3. Iterating Over a String
# Method 1 using Index
str4 = "Sonu"
for i in range(len(str4)):
    print(str4[i])

# Output
# S
# o
# n
# u

# Method 2
for i in str4:
    print(i)
    
# Output
# S
# o
# n
# u

#3. String Concatenate
str5 = "Hello"
str6 = "Sonu!"
str7 = str5 + " " +str6
print(str7)
# Output -> Hello Sonu!

str8 = 'a'
print(str8 * 3)
# outuput-> aaa

#4. String Formating 
# ---> F string 
num = 2
str9 = f"Hello {num}"
print(str9)
# output -> Hello 2

# ---> format function
str10 = "Hello {}, {}, {}"
name1 = "Ram"
name2 = "Rahul"
name3 = "Radha"
str1 = str10.format(name1, name2, name3)
print(str1)
#output-> Hello Ram, Rahul, Radha
str10 = "Hello {1}, {0}, {2}"
name1 = "Ram"
name2 = "Rahul"
name3 = "Radha"
str1 = str10.format(name1, name2, name3)
print(str1)
#output-> Hello Rahul, Ram, Radha

#5. Functions of String
str1 = "hello"
cap = str1.capitalize()
print(cap) #Output -> Hello

upper = str1.upper()
print(upper) #Output -> HELLO

lower = str1.lower()
print(lower) #hello

str2 = "Hello->Boys"
split_list = str2.split("->")
print(split_list) #Output -> ['Hello', 'Boys']

cnt = str2.count('l')
print(cnt) # 2

target = "go"
str1 = "Hello where are you going"

yes_no = target in str1
print(yes_no) #True

yes_no = target not in str1
print(yes_no) # False

str1 = "He"
str2 = "He"
yes_no = str1 is str2
print(yes_no) # True

str.find()




