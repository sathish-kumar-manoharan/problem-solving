
def find_first_occurrence(s, to_find):
    """
    Args:
     s(str)
     to_find(char)
    Returns:
     int32
    """
    # Write your code here.
    print(list(filter(lambda x: x == to_find, [char for char in s])))

find_first_occurrence('sathish', 'a')