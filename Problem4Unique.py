#Sara Margaret Rizzo
#2020-08-22

#Problem 4: Write a Python function that takes a list of numbers and 
#returns a new list with unique elements of the first list.  
#Use list [1, 3, 3, 3, 6, 2, 3, 5]. Use the append function.

#function to get unique values and add them to new list using append function
def unique(numlist): 
    unique_list = [] 
    for x in numlist: 
        if x not in unique_list: 
            unique_list.append(x) 
    #return new list
    return unique_list  
    
  
#list to evaluate
numlist = [1, 3, 3, 3, 6, 2, 3, 5] 
#call function and print new list it created
print("The unique values in the list are", unique(numlist)) 