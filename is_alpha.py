
def count_alphabets(s):
    """
    Args:
     s(str)
    Returns:
     int32
    """
    alpha = [c for c in s if c.isalpha()]
    print("The list is ", list(alpha))
    print("The number if alphabets found is ", len(alpha))

count_alphabets("sathish234320-2")