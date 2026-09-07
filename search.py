#Question 7

def recursive_search(numbers, target):
    if not numbers: 
        return False
    if numbers[0] == target:
        return True
    
    return recursive_search(numbers[1:], target)

my_numbers = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
user_input = int(input("Enter a number to search for: "))

if recursive_search(my_numbers, user_input):
    print("Number found")
else:
    print("Not in the list.")