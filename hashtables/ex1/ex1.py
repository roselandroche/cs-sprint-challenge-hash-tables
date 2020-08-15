def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    weights_dict = {}

    for weight in weights:
        weights_dict[weight] = limit - weight

    for weight in weights:
        if limit - weight in weights_dict:
            first_index = weights.index(weight)
            second_index = weights.index(limit - weight, first_index + 1)
            if second_index > first_index:
                return((second_index, first_index))
            elif second_index < first_index:
                return((first_index, second_index))
            else:
                return None

'''
U
Input
    limit (weight limit)
    weights ( LIST of weights)
    length (length of weights list)
Output
    tuple of integers
        integers are INDICES of weights that add up to limit
        higher of two integers should be first in tuple
    if no pair exists
        return None
P
Create result tuple
Create dict
    key: weight
    value: limit - weight?
Iterate through range of length
    access dict
    if both key and value exist in list
        add larger index to result
        add other index to result
'''