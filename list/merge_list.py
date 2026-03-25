def merge_list(l1, l2):
    """
    Merge two lists into one list.

    Args:
        l1 (list): The first sorted list.
        l2 (list): The second sorted list.

    Returns:
        list: The merged sorted list.
    """

    sorted = list()

    l1_index, l2_index = 0, 0

    while l1_index < len(l1) and l2_index < len(l2):
        if l1[l1_index] < l2[l2_index]:
            sorted.append(l1[l1_index])
            l1_index += 1
        else:
            sorted.append(l2[l2_index])
            l2_index += 1

    # Append any remaining elements from either list
    sorted.extend(l1[l1_index:])
    sorted.extend(l2[l2_index:])

    return sorted

print(merge_list([1, 3, 5], [2, 4, 6]))