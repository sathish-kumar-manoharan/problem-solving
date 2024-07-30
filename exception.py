a = input()
b = input()

try:
    c = a/b
except:
    print("Exception has occured")
else:
    print("No exception occured")
finally:
    print("try exception is completed")
