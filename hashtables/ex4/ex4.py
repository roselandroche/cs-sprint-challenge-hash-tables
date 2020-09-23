def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    a_dict = dict.fromkeys(a, 'I exist')
    for num in a:
        if num < 0:
            pos_num = 0 - num
            if a_dict.get(pos_num) is not None:
                result.append(pos_num)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

'''
U
Input
    list of integers
    positive and negative
Output
    list of integers
    positive only
Task
    return list of positive integers with corresponding negative values in input

P
Create a dict
    every integer in input
Iterate over given list
    check if dict[negative version of integer] exists
        dict.get(integer) - returns None if not there
        if exists
            add to result list
Return result
'''