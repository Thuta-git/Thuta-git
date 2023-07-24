'''
In this discussion, I will be distinguishing 
the difference between equivalent and identical within the examples.
'''
#example of equivalent
l1 = [1,2,3,4,5] 
l2 = [1,2,3,4,5]

if l1 is l2: # if l1 is l2, it will print True. Otherwise, it will print false
    print (True)
else:
    print(False) 

'''
'is' is used for comparing instances which means if
it is the same instance or the same exact object, it 
is going to evaluate value. In this case, our output is 
False since l1 is not entirely l2 and you can test it by 
checking their id().Value can be actually considered the equal
without being the same object in memory. Even if 
they are equal, they are still two different objects.
'''
print(id(l1)) # 2306597218560 (ID of l1)
print(id(l2)) # 2306598735552 (ID of L2)

#example of identical
l1 = [1,2,3,4,5] 
l2 = l1 #we will set that l2 is equal to l1, the second list l2 is now identical to the first list l1.

if l1 == l2: #if l1 is identical to l2, print True
    print (True)
else: #otherwise False
    print(False) 
# this will output True since we set the value of l2 as l1, now it is identical.
#Now that they are identical, we will comfirm it by using id().

print (id(l1)) #2306598737536 (ID of l1)
print (id(l2)) #2306598737536 (ID of l2)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''
Objects are data structures known as values as well as methods that can be used to manipulate that data. 
Each object is distinct in terms of identity, type, and value. 
An object's identity remains constant over the course of its existence and is used to set it apart from other items. 
An object's type determines the kind of data it can store and the activities it may carry out.
'''
#e.g.
# List object
my_list = [1, 2, 3, 4] # Everyting is an object in Python.
name = 'John'
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
References are used to access the object memory. Python keeps newly created objects in memory, 
and the variable you use to refer to them is actually a reference to where they are kept in memory. 
References are similar to connections to the actual object.
'''
#e.g.
# Creating a list object and assigning it to a variable
original_list = [1, 2, 3]

# Creating a reference to the same list object
ref_list = original_list # Now ref_list can be refer to the same list in object memory.

# Modifying the list through the reference
ref_list.append(4) 

# Printing both variables
print(original_list)  # Output: [1, 2, 3, 4]
print(ref_list)       # Output: [1, 2, 3, 4]
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
Aliasing can be done whenever two or more variables references to the same object memory. 
In other words, assigning one variable to another or passing objects to functions.
'''
#e.g.
list1 = [1, 2, 3]
list2 = list1

# Modify list2
list2.append(4)

# Print both lists
print(list1)  # Output: [1, 2, 3, 4]
print(list2)  # Output: [1, 2, 3, 4]
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def modify_list(input_list):
    input_list.append(42)
    input_list.remove(10)
    input_list.extend([100, 200, 300])

my_list = [1, 5, 10]
modify_list(my_list)
print(my_list)  # Output: [1, 5, 42, 100, 200, 300]

'''
In the above example, a string or word called 'input_list' is an argument for the function 'modify_list'. 
The list is modified inside the function by appending the value 42, removing the element 10, and extending the 
list with the values [100, 200, 300].
'''