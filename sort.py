def sort(list):
    list.sort(key=len)
    return list

print(sort(["abcd", "ab", "abc"]))