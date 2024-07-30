from collections import Counter

def get_intersection_with_maintained_frequency(a, b):
    """
    Args:
     a(list_int32)
     b(list_int32)
    Returns:
     list_int32
    """
    return print(list((Counter(a) & Counter(b)).elements()))

get_intersection_with_maintained_frequency([1,2,2,3,2,1,5], [2, 2, 3, 5])