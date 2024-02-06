print("Hello world")


a = [1,2,3,4]
for idx, item in enumerate(a):
    print(item)


def is_odd_even(a):
    return a % 2 == 0


# function tests
assert(2) == True
assert(2) == False