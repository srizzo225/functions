#Sara Margaret Rizzo
#2020-08-22

#Problem 2: Write a Python function to check whether a number is in a given range. Use range(1,10). 
#Print whether the number is in or not in the range.
# Any other information throughout your code that is helpful

#function that checks if number is in range(1,10)
def test_range(n):
    if n in range(1,10):
        return True
    else:
        return False

#asks user for number and covert to integer
n = int(input("Enter a number. "))
#call function to check if number is in range
num = test_range(n)
if num is True:
    print("Yes,", n, "is in the range")
else:
    print("No,", n, "is not in the range")