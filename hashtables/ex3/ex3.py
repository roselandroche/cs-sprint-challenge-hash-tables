def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    count_dict = {}

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))


'''
U
Input
    List of lists (up to 10 lists) containing integers
Output
    List of integers that exist in all given lists

Task
    Find any integers that exist in all lists
    Save and return a list with just those integers
    Order NOT important

* RUNTIME COMPLEXITY VERY IMPORTANT

P
Create result list
Use a for loop to separate list of lists? destructure?
Create a dict
    key: integer
    value: count
Iterate over lists
    access key in dict
    if value > 1
        append to result list
Return result
'''