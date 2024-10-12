def sort(list):
    list.sort(reverse = True)
    return list

list = [2, 4, 23, 51, 1, 3, 5, 23]
list.sort()
print("The sorted values are ", list)

list.sort(reverse=True)
print("The reverse values are ", list)

list = [[2, 2], [4, 2], [0, 23], [2, 51], [1, 23], [3,1], [5, 4], [0, 23]]
list.sort()
print("The sorted values are ", list)

list.sort(reverse=True)
print("The reverse values are ", list)

def sort_alphabetically(list):
    list.sort(key=len)
    return list

print(sort_alphabetically(["abcd", "ab", "abc"]))