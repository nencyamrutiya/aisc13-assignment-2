a = [1,2,3,4]
for idx, item in enumerate(a):
    print(item)

def is_odd_even(a):
    return a % 2 == 0

# function tests
# assert is_odd_even(2) == True
# assert is_odd_even(3) == False

def test_func():
    assert 1+1 == 2
    assert is_odd_even(2) == True
    assert is_odd_even(3) == False
    assert is_odd_even(10) != False