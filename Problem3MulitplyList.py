#Sara Margaret Rizzo
#2020-08-22

#Problem 3: Write a Python function to multiply all the numbers in a list. Use list [5, 2, 7, -1].

#function that multiplies all numbers in a list
def multiply(x):
    runningtotal = 1
    for x in numlist:
        runningtotal = runningtotal * x
    return runningtotal

#list of numbers to multiply
numlist = [5, 2, 7, -1]
#call the function to multiply the numbers in the list
multiplyResult = multiply(numlist)
#print the result
print(multiplyResult)